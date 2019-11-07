# -*- encoding:utf8 -*-
import time
import urllib.parse
import urllib.request
import uuid
from datetime import timedelta
from decimal import Decimal

from bson import ObjectId
from flask import Flask, request, render_template, abort, session, send_from_directory, make_response, send_file
from flask_moment import Moment
from flask import redirect, url_for, jsonify
from pymysql import IntegrityError
from sqlalchemy import desc
from flask_wtf import CSRFProtect
import os
import time
from threading import Thread

from config import command_head
from get_image import func
from search import baidu_search_service
from util import decortor
from test import search1

from baidu_search import baidu_search_service2
from tool import is_url

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string '
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@192.168.3.84:3306/netta"  # mysql+pymysql://用户：密码@主机：端口/数据库

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

from model import *
from forms import *

db.init_app(app=app)
moment = Moment(app)
csrf = CSRFProtect(app)
# db.create_all()
ALLOWED_EXTENSIONS = ["jpg", "png", "jpeg", "gif"]  # 允许上传头像的文件类型
recommend_news_set = list()  # 用户鼠标行为捕捉新闻集合
operation = set()


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, Decimal):
            return str(o)
        return json.JSONEncoder.default(self, o)


app.json_encoder = JSONEncoder


# result = deque(maxlen=40)
# result = []
# to_bottom_left = deque(maxlen=10)


class SearchThread(Thread):
    def __init__(self, info, id):
        # 注意，super().__init__() 一定要写
        # 而且要写在最前面，否则会报错。
        super().__init__()
        self.info = info
        self.id = id

    def run(self):
        analysis(self.info, self.id)


def cal_interest(a):
    global operation
    if '/news/detail/' in a['url']:
        news_id = a['url'].replace('http://127.0.0.1:5000/news/detail/', '')
        news_detail = NewsDetail.query.filter(NewsDetail.news_id == news_id).first()
        try:
            words = eval(news_detail.words)
        except:
            words = []
        for i in words:
            operation.add(deal_word(i))
    for i in a['mousemove']:
        operation.add(deal_word(i[0]))
    for i in a['mouseclick']:
        operation.add(deal_word(i[1]))
    print(operation)
    # print(session.get('operation'))
    print()


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}


# def send_url(ip, ak="P6qbYQWetuIYljz9LCL9qc1Z71Pgnw8u"):
#     data = {"ip": ip, "ak": ak, "coor": "bd09ll"}
#     data = urllib.parse.urlencode(data).encode("utf-8")
#     url = "https://api.map.baidu.com/location/ip"
#     request = urllib.request.Request(url, data=data, headers=headers)
#     response = urllib.request.urlopen(request, timeout=10)
#     js = json.loads(response.read().decode("utf-8"))
#     return js.get("content", {}).get("point", "请求失败")


def send_url(ip, access_key='7d088ef64bff6de392f947e00d988cca'):
    url = 'http://api.ipstack.com/%s?access_key=%s' % (ip, access_key)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request, timeout=10)
    js = json.loads(response.read().decode("utf-8"))
    print(js)
    latitude = js.get('latitude')
    longitude = js.get('longitude')
    return [longitude, latitude]


@app.route('/')  # 首页
def index():
    top_news_list = search_news(num=7)
    hot_topic = [
        {
            'title': '忘买鸡腿被妻捅死',
            'url': '#'
        }, {
            'title': '大连一化工厂爆炸',
            'url': '#'
        }, {
            'title': '视觉中国恢复上线',
            'url': '#'
        }
    ]
    id = session.get('user', "")
    # if id:
    #     print(id)
    #     to_bottom_left = get_bottom_left(id["user_id"])
    # else:
    to_bottom_left = get_news()

    hot_24 = [
        {
            "news_id": "",
            "news_url": "http://news.163.com/19/0604/19/EGRNBDC30001875O.html",
            "img": "",
            "title": "澳大利亚达尔文市发生枪击事件致5人死 凶手已被捕"
        }
    ]
    near_news = [
        {
            "news_id": "",
            "news_url": "https://baijiahao.baidu.com/s?id=1635415248132259003&wfr=spider&for=pc",
            "img": "../static/img/95eef01f3a292df547567dd4a3bfb16436a873e9.jpeg",
            "title": "跟优衣库联名遭疯抢，KAWS的商业价值来自何处？"
        }
    ]
    hot_video = [
        {
            "video_id": "",
            "video_url": "https://www.iqiyi.com/v_19rre4x290.html",
            "img": "../static/img/video-1.jpg",
            "title": "前所未有！海绵宝宝变大肉饼"
        }, {
            "video_id": "",
            "video_url": "https://www.bilibili.com/video/av49775093/",
            "img": "../static/img/video-2.webp",
            "title": "吴亦凡《大碗宽面》MV（动画版）"
        }, {
            "video_id": "",
            "video_url": "https://www.bilibili.com/video/av49842011/",
            "img": "../static/img/video-3.webp",
            "title": "《复联4》前必看！一口气看完21部漫威电影，完整的时间线剧情讲解！"
        }, {
            "video_id": "",
            "video_url": "https://www.bilibili.com/video/av49868991/",
            "img": "../static/img/video-4.webp",
            "title": "【特效向】蔡徐坤VS全明星"
        }
    ]
    user = session.get('user')
    return render_template('index.html', top_news_list=top_news_list, hot_topic=hot_topic, bottom_left=to_bottom_left,
                           hot_24=hot_24, near_news=near_news, hot_video=hot_video, user=user)
    # return render_template('index.html', top_news_list=[], hot_topic=hot_topic, bottom_left=to_bottom_left,
    #                        hot_24=hot_24, near_news=near_news, hot_video=hot_video, user=user)


# +++++++++++++++++++++++++++++++++++++++++++ 详情页面以及该页面的评论和回复功能

@app.route('/news/detail/<news_id>')  # 每则新闻的详情页
def news_detail(news_id):
    user = session.get('user', "")  # 当用户没有登录时，可以获取页面评论
    news_obj = db.session.query(News).filter_by(news_id=news_id).first()
    comments = news_obj.comments.order_by(desc("timestamp"))  # 将评论按照时间顺序进行排序

    comment_user_info = []
    for comment in comments:
        dic = {}
        replies_ = comment.replies.order_by(desc("timestamp"))  # 每条评论下面的回复内容
        reply_list = []  # 所有的回复内容
        for reply in replies_:
            to_user = db.session.query(User).get(reply.to_uid)
            from_user = db.session.query(User).get(reply.from_uid)
            agree_num = reply.agree_num
            reply_list.append((from_user, to_user, reply, agree_num))
        comment_user = db.session.query(User).get(comment.user_id)
        dic["comment"] = comment
        dic["comment_user"] = comment_user
        dic["comment_reply_list"] = reply_list
        dic["reply_length"] = len(reply_list)
        comment_user_info.append(dic)
    if news_obj:
        recommand = get_recommand(news_id)
        more_news = get_news()
        detail = NewsDetail.query.filter(NewsDetail.news_id == news_id).first()
        try:
            if eval(detail.relation):
                has_rel = True
            else:
                has_rel = False
        except:
            has_rel = False
        try:
            words = eval(detail.words)
        except:
            words = []

        return render_template('news-detail.html', news_obj=news_obj, comment_item=comment_user_info, user=user,
                               recommand=recommand, words=words, more_news=more_news, detail=has_rel)
    return abort(404)


@app.route("/post_comment", endpoint="post_comment", methods=["GET", "POST"])  # 发表评论
@decortor(session)
@csrf.exempt
def post_comment():
    if request.method == "POST":
        user_id = session.get("user").get("user_id")
        data = request.form
        if data.get("user_id") == str(user_id):  # 检查前端传过来的id是否和session中的id一致
            one_comment = Comment(user_id=user_id, news_id=data.get("news_id"), body=data.get("comment"))
            db.session.add(one_comment)
            db.session.commit()
            comment_id = one_comment.id
            pmu_head_pic = session.get("user").get("head_pic")
            description = "(" + session.get("user").get("description") + ")" if session.get("user").get(
                "description") else ""
            nickname = session.get("user").get("nick_name")
            comment_body = data.get("comment")
            agree_num = one_comment.agree_num
            timestamp = one_comment.timestamp

            # 将新闻数据表中的评论数进行更新
            news_obj = db.session.query(News).filter_by(news_id=data.get("news_id"))
            update_comment_num = news_obj.first().comment_num + 1
            news_obj.update({"comment_num": update_comment_num})
            db.session.commit()
            return jsonify({"comment_id": comment_id,
                            "pmu_head_pic": pmu_head_pic,
                            "comment_body": comment_body,
                            "agree_num": agree_num,
                            "description": description,
                            "nickname": nickname,
                            "timestamp": timestamp, })
        return abort(404)
    return abort(404)


@app.route("/delete_comment", endpoint="delete_comment", methods=["POST", "GET"])  # 删除评论
@decortor(session)
@csrf.exempt
def delete_comment():
    if request.method == "POST":
        data = request.form

        # 当删除的是评论的时候
        if data.get("delete_type") == "comment":
            delete_comment_id = data.get("delete_comment_id")
            delete_comment_ = db.session.query(Comment).get(delete_comment_id)
            relative_replies = delete_comment_.replies
            try:
                for one_reply in relative_replies:
                    db.session.delete(one_reply)
                db.session.delete(delete_comment_)
                db.session.commit()
            except Exception as e:
                print(e)
                pass

            # 将新闻数据表中的评论数进行更新
            news_obj = db.session.query(News).filter_by(news_id=data.get("news_id"))
            update_comment_num = news_obj.first().comment_num - 1
            news_obj.update({"comment_num": update_comment_num})
            db.session.commit()
            return "success"

        # 当删除是回复的时候
        if data.get("delete_type") == "reply":
            delete_reply_id = data.get("delete_reply_id")
            delete_reply_ = db.session.query(CommentReply).get(delete_reply_id)
            db.session.delete(delete_reply_)
            db.session.commit()
            return "success"
    return abort(404)


# 发表回复
@app.route("/post_reply", methods=["GET", "POST"])  # 发表回复
@csrf.exempt
def post_reply():
    if request.method == "POST":

        # 从前端获取新闻的id，主要用于将数据存入到推送消息的数据库中
        news_id = request.form.get("news_id")
        notify_content = db.session.query(News).get(news_id)

        user_id = session.get("user").get("user_id")
        if user_id == int(request.form.get("user_id")):
            from_user = session.get("user")
            reply_id_ = request.form.get("reply_id")
            if not reply_id_:
                comment_id = request.form.get("comment_id")
                reply_body = request.form.get("reply_body")
                to_uid = db.session.query(Comment).get(comment_id).user_id
                reply_id = comment_id
                reply_type = "comment"

                reply = CommentReply(from_uid=user_id, to_uid=to_uid, body=reply_body, comment_id=comment_id,
                                     reply_id=reply_id, reply_type=reply_type)
                db.session.add(reply)
                db.session.commit()

                head_pic = from_user.get("head_pic")
                nickname = from_user.get("nick_name")

                # 发表回复之后，将信息存入到推送消息的数据库中
                notifyremind = NotifyRemind(kind="comment", recipientID=to_uid, from_user_name=nickname,
                                            news_id=news_id, content=notify_content.title)
                db.session.add(notifyremind)
                db.session.commit()

                # 后台判断个人说明是否存在，存在则加上括号， 返回后台的信息
                description = "(" + from_user.get("description") + ")" if from_user.get("description") else ""
                to_user = db.session.query(User).get(to_uid)
                to_nickname = to_user.nick_name
                to_description = "(" + to_user.description + ")" if to_user.description else ""
                # 回复人头像、 回复人昵称、被回复人昵称
                # 均可在当前页面中进行获取
                return jsonify(
                    {"id": reply.id, "head_pic": head_pic, "nickname": nickname, "to_nickname": to_nickname,
                     "description": description,
                     "to_description": to_description})
            else:
                comment_id = request.form.get("comment_id")
                reply_body = request.form.get("reply_body")
                to_uid = db.session.query(CommentReply).get(reply_id_).from_uid
                reply_id = reply_id_
                reply_type = "reply"

                # 将回复插入到回复数据库
                reply = CommentReply(from_uid=user_id, to_uid=to_uid, body=reply_body, comment_id=comment_id,
                                     reply_id=reply_id, reply_type=reply_type)
                db.session.add(reply)
                db.session.commit()

                # 返回的数据是创建的该条回复的id
                nickname = from_user.get("nick_name")
                head_pic = from_user.get("head_pic")
                description = "(" + from_user.get("description") + ")" if from_user.get(
                    "description") else ""  # 回复人的信息，

                # 将回复信息加入到notifyremind数据库中，用于推送消息
                notifyremind = NotifyRemind(kind="comment", recipientID=to_uid, from_user_name=nickname,
                                            news_id=news_id,
                                            content=notify_content.title)
                db.session.add(notifyremind)
                db.session.commit()

                # 返回的前端的信息
                to_user = db.session.query(User).get(to_uid)
                to_nickname = to_user.nick_name
                to_description = "(" + to_user.description + ")" if to_user.description else ""  # 被回复人的信息
                return jsonify({"id": reply.id, "head_pic": head_pic, "nickname": nickname, "to_nickname": to_nickname,
                                "description": description,
                                "to_description": to_description})
        return abort(404)
    return abort(404)


@app.route("/give_like", methods=["GET", "POST"])  # 点赞
@csrf.exempt
def give_like():
    if request.method == "POST":

        # 从前端获取新闻的id，主要用于将数据存入到推送消息的数据库中
        news_id = request.form.get("news_id")
        notify_content = db.session.query(News).get(news_id)
        title = notify_content.title
        user_id = session.get("user").get("user_id")
        nickname = session.get("user").get("nick_name")
        like_form = request.form
        # 点赞的内容是评论时
        if like_form.get("like_type") == "comment":
            like_comment_id = like_form.get("like_id")  # 前端传过来的评论id
            all_comment_like = db.session.query(GiveLike).filter_by(like_type="comment", user_id=user_id).all()
            con_id_list = [comment_like.con_rep_id for comment_like in all_comment_like]  # 该登录用户点赞过的评论id列表
            if int(like_comment_id) not in con_id_list:
                givelike = GiveLike(user_id=user_id, con_rep_id=like_comment_id, like_type="comment")
                db.session.add(givelike)
                db.session.commit()  # 将点赞的评论id和用户id加入到数据库中

                # 点赞之后，将信息存入到推送消息的数据库中
                to_uid = db.session.query(Comment).get(like_comment_id).user_id
                nickname = session.get("user").nick_name
                notifyremind = NotifyRemind(kind="like", recipientID=to_uid, from_user_name=nickname, news_id=news_id,
                                            content=notify_content.title)
                db.session.add(notifyremind)
                db.session.commit()

                like_comment = db.session.query(Comment).get(like_comment_id)  # 更新评论数据库的点赞数
                agree_num = like_comment.agree_num + 1
                db.session.query(Comment).filter_by(id=like_comment_id).update({"agree_num": agree_num})
                db.session.commit()
                return jsonify({"agree": agree_num})
            else:
                # 当comment_id 已经存在时，这是就为取消点赞, 同时删除数据库中的数据
                givelike = db.session.query(GiveLike).filter_by(user_id=user_id, con_rep_id=int(like_comment_id),
                                                                like_type="comment").first()
                db.session.delete(givelike)
                db.session.commit()  # 将点赞的评论id和用户id加入到数据库中

                like_comment = db.session.query(Comment).get(like_comment_id)  # 更新评论数据库的点赞数
                agree_num = like_comment.agree_num - 1
                db.session.query(Comment).filter_by(id=like_comment_id).update({"agree_num": agree_num})
                db.session.commit()
                return jsonify({"agree": agree_num})

        # 用户点赞的是回复的时候，此时依据回复进行
        if like_form.get("like_rep_type") == "reply":
            like_reply_id = like_form.get("like_rep_id")
            all_reply_like = db.session.query(GiveLike).filter_by(like_type="reply", user_id=user_id).all()
            rep_id_list = [reply_like.con_rep_id for reply_like in all_reply_like]
            if int(like_reply_id) not in rep_id_list:
                rep_givelike = GiveLike(user_id=user_id, con_rep_id=like_reply_id, like_type="reply")
                db.session.add(rep_givelike)

                # 点赞之后，将信息存入到推送消息的数据库中,主要是显示推送消息
                to_uid = db.session.query(CommentReply).get(like_reply_id).to_uid
                notifyremind = NotifyRemind(kind="like", recipientID=to_uid, from_user_name=nickname, news_id=news_id,
                                            content=title)
                db.session.add(notifyremind)

                like_reply = db.session.query(CommentReply).get(like_reply_id)
                reply_agree_num = like_reply.agree_num + 1
                db.session.query(CommentReply).filter_by(id=like_reply_id).update({"agree_num": reply_agree_num})

                db.session.commit()
                return jsonify({"agree": reply_agree_num})

            else:
                # 当数据库中该用户点赞已经存在时，这是就为取消点赞, 同时删除数据库中的数据
                givelike = db.session.query(GiveLike).filter_by(user_id=user_id, con_rep_id=int(like_reply_id),
                                                                like_type="reply").first()
                db.session.delete(givelike)
                db.session.commit()  # 将点赞的评论id和用户id加入到数据库中

                like_reply = db.session.query(CommentReply).get(like_reply_id)  # 更新评论数据库的点赞数
                agree_num = like_reply.agree_num - 1
                db.session.query(CommentReply).filter_by(id=like_reply_id).update({"agree_num": agree_num})
                db.session.commit()
                return jsonify({"agree": agree_num})

        return abort(404)


# ++++++++++++++++++++++++++++++++++++


# # ++++++++++++++++++++++++++主页的的登录、注册和搜索等内容+++++++++++++++++
# @app.route('/organization/<search_id>')  # 搜索
# def search_result1(search_id):
#     result_obj = db.session.query(search_result).filter_by(search_id=search_id).first()
#     user = session.get('user')
#     if result_obj:
#         return render_template('organization.html', result_obj=result_obj, user=user)
#     return abort(404)


@app.route('/register', methods=['POST'])  # 注册
def register():
    form = RegistForm(request.form)
    if form.validate():
        try:
            db.session.add(User(account=form.account.data, passwd=form.password1.data, nick_name=form.nick_name.data))
            db.session.commit()
        except IntegrityError as e:
            err_infor = e.args[0].split('for key')[-1]
            if 'account' in err_infor:
                return 'account repeat'
            elif 'nick_name' in err_infor:
                return 'nick_name repeat'
        return 'success'
    return 'error'


@app.route('/login', methods=['POST', "GET"])  # 登录
def login():
    if request.method == "POST":
        form = LoginForm(request.form)
        if form.validate():
            user = db.session.query(User).filter_by(account=form.account.data, passwd=form.password.data).first()
            if user:
                user = user_2_json(user)
                session['user'] = user
                return 'success'
            return '账号或密码错误'
        return 'error'


@csrf.exempt
@app.route('/logout', methods=['POST', 'GET'])  # 退出
def logout():
    session.pop('user')
    return redirect(url_for(".index"))


@app.route("/")  # 权限管理
def admin():
    pass


# +++++++++++++++++++个人信息页面的我的喜欢、我的评论、消息通知、账号信息等功能+++++++++
@app.route('/manage/comment', endpoint="comment", methods=["GET", "POST"])  # 我的评论， 是个人中心的我的评论
@decortor(session)
def comment():
    user = session.get('user')
    comments = []
    user_id = user["user_id"]
    comments_model = db.session.query(Comment).filter_by(user_id=user_id).all()  # 查询到的所有评论
    for each in comments_model:
        comment_dic = {}
        news_model = db.session.query(News).filter_by(news_id=each.news_id).first()
        comment_dic["id"] = each.id
        comment_dic["news_id"] = each.news_id
        comment_dic["news_title"] = news_model.title
        comment_dic["news_url"] = news_model.url
        comment_dic["comment"] = each.body
        comment_dic["timestamp"] = each.timestamp
        comments.append(comment_dic)
    return render_template('comment.html', comments=comments, user=user)


@csrf.exempt
@app.route('/manage/favourite', endpoint="favourite", methods=["GET", "POST"])  # 我的喜欢
@decortor(session)
def favourite():
    # 当点击我的喜欢时，展示所有的新闻
    if request.method == "GET":
        user = session.get('user')
        user_id = user.get("user_id")
        user_ = db.session.query(User).filter_by(user_id=user_id).first()
        news_ = user_.news.all()
        return render_template('favourite.html', news=news_, user=user)

    # 当新增喜欢或者撤销喜欢时，发送的是post请求，接收news的Id建立连接
    if request.method == "POST":
        # 判断传过来的news_id在不在喜欢的列表中
        user = session.get('user')
        revocation_news_id = int(request.form.get("new_id"))

        exist_news_objs = db.session.query(middle_mylike).filter_by(user_id=user.get("user_id")).all()
        exist_news_ids = [obj.news_id for obj in exist_news_objs]

        # 撤销自己喜欢的新闻
        if revocation_news_id in exist_news_ids:
            news_ = db.session.query(News).filter_by(news_id=revocation_news_id).first()
            like_num = news_.like_num - 1
            db.session.query(News).filter_by(news_id=revocation_news_id).update({"like_num": like_num})
            user_id = user.get("user_id")
            user_ = db.session.query(User).filter_by(user_id=user_id).first()
            user_.news.remove(news_)
            db.session.commit()
            return jsonify({"like_num": like_num})

        # 增加自己喜欢的新闻
        else:
            news_ = db.session.query(News).filter_by(news_id=revocation_news_id).first()
            like_num = news_.like_num + 1
            db.session.query(News).filter_by(news_id=revocation_news_id).update({"like_num": like_num})
            user_id = user.get("user_id")
            user_ = db.session.query(User).filter_by(user_id=user_id).first()
            user_.news.append(news_)
            db.session.commit()
            return jsonify({"like_num": like_num})


@app.route('/manage/notice', endpoint="notice", methods=["GET", "POST"])  # 我的通知
@decortor(session)
def notice():
    if request.method == "GET":
        user = session.get('user')
        noticelist = db.session.query(NotifyRemind).filter_by(recipientID=user.get("user_id")).all()

        notices = []
        for one_notice in noticelist:
            if not one_notice.status:
                dic = dict()
                dic["kind"] = one_notice.kind
                dic["createdtime"] = one_notice.createdAt
                dic["from_user_name"] = one_notice.from_user_name
                dic["content"] = one_notice.content
                dic["news_id"] = one_notice.news_id
                dic["time"] = one_notice.createdAt
                notices.append(dic)

        return render_template('notice.html', notices=notices, user=user)
    if request.method == "POST":
        user_id = session.get("user").get("user_id")
        data = request.form.get("formdata")
        if data == "all_delete":
            db.session.query(NotifyRemind).filter(NotifyRemind.recipientID == user_id).delete()
            db.session.commit()
            return "success"
        if data == "all_read":
            db.session.query(NotifyRemind).filter(NotifyRemind.recipientID == user_id).update(
                {NotifyRemind.status: True}, synchronize_session=False)
            db.session.commit()
            return "success"


# @app.route("/manage/")


@app.route('/manage/information', endpoint="information")  # 我的资料
@decortor(session)
def information():
    user = session.get('user')
    return render_template('information.html', user=user)


@csrf.exempt
@app.route('/manage/update_info', methods=["GET", "POST"])  # 我的资料
def update_info():
    if request.method == "POST":
        user_obj = session.get("user")
        user_id = user_obj.get("user_id")
        head_pic = user_obj.get("head_pic")

        # 判断是否上传图片，没上传时使用原图片
        img = request.files.get('img')
        if img:
            suffix = img.filename.rsplit(".", 1)[-1]
            if suffix not in ALLOWED_EXTENSIONS:
                return redirect(url_for(".information"))

            filename = str(user_id) + "." + suffix
            filepath = os.path.join("head_pic/", filename)
            print(filepath)
            img.save("static/" + filepath)
        else:
            if head_pic:
                filepath = head_pic
            else:
                filepath = os.path.join("head_pic/", "default.jpg")

        # 修改昵称，查询数据库, 判断昵称是否重复
        nick_name = request.form.get("username")
        if not nick_name:
            nick_name = user_obj.get("nick_name")
        else:
            all_user_name = [user_obj.nick_name for user_obj in db.session.query(User).all() if
                             user_obj.user_id != user_id]
            if nick_name in all_user_name:
                return redirect(url_for(".information"))

        true_name = request.form.get("true_name") if request.form.get("true_name") else user_obj.get("true_name")
        birthday = request.form.get("birthday") if request.form.get("birthday") else user_obj.get("birthday")
        sex = request.form.get("sex") if request.form.get("sex") else user_obj.get("sex")
        country = request.form.get("country") if request.form.get("country") else user_obj.get("country")
        province = request.form.get("prov") if request.form.get("prov") else user_obj.get("province")
        city = request.form.get("city") if request.form.get("city") else user_obj.get("city")

        update_detail = {
            "nick_name": nick_name,
            "true_name": true_name,
            "head_pic": filepath,
            "birthday": birthday,
            "sex": sex,
            "country": country,
            "province": province,
            "city": city,
        }

        db.session.query(User).filter_by(user_id=user_id).update(update_detail)
        db.session.commit()

        # 将更新的用户资料重新更新到session中
        update_user = db.session.query(User).filter_by(user_id=user_id).first()
        session["user"] = user_2_json(update_user)
        return "success"
    return "error"


@csrf.exempt
@app.route("/info", methods=["POST", "GET"])
def info():
    print(request.get_data())
    data_dic = json.loads(request.get_data())
    # print(data_dic)
    # news_list = data_dic.get("mousemove", [])
    # print(news_list)
    # print(data_dic)
    cal_interest(data_dic)

    # 将兴趣点加入 recommend_news_set 传输给爬虫节点进行搜索
    # if len(news_list) > 0:
    #     for each in news_list:
    #         print(each)
    #         news = re.sub("\s+", "", each[0])
    #         if news not in recommend_news_set:
    #             recommend_news_set.append(news)

    # realUrl, realtitle, web_time, page_text,title,description

    return json.dumps("{}")


def get_news_from_database():
    global operation
    while True:
        try:
            if len(operation) != 0:
                keyword = list(operation)[-1]
                search1(keyword)
                # time.sleep(5)
                # # search_database_result = [('www.baidu.com', 'aaa', '', 'asdasdas','aaaaaa','aaaaaa'),('www.baidu.com', 'aaa', '', 'asdasdas','aaaaaa','aaaaaa')]
                # recommend_news_set.pop(-1)
                # for tup in search_database_result:
                #     result.append(tup)
            time.sleep(20)
        except Exception as e:
            print(e)
            time.sleep(20)


@csrf.exempt
@app.route("/search", methods=["POST", "GET"])
def search():
    #
    # # 获取前几项的搜索内容
    # if request.method == "GET":
    #     keyword = request.args.get("kw")
    #     # news_list = db.session.query(News).filter(News.title.like("%{}%".format(keyword))).all()
    #     news_list = db.session.query(News).filter(News.title.like("%{}%".format(keyword))).limit(10)
    #
    #     user = session.get("user")
    #     if user:
    #         user_obj = db.session.query(User).filter_by(user_id=user.get("user_id")).first()
    #         like_newses = user_obj.news.all()
    #
    #         # 将搜索到的新闻并同时是当前用户喜欢的新闻加上{“in”: 1}标识，同时必须转为json格式，否则无法加入session
    #         after_news_list = []
    #         for single in news_list:
    #             if single in like_newses:
    #                 in_single = news_2_json(single)
    #                 in_single.update({"in": 1})
    #                 after_news_list.append(in_single)
    #             else:
    #                 after_news_list.append(news_2_json(single))
    #         session["after_news_list"] = after_news_list
    #         back_news = after_news_list[:3]
    #         return render_template("search-result.html", user=user, news=back_news)
    #     else:
    #         news_list = [news_2_json(news) for news in news_list]
    #         session["news_list"] = news_list
    #         back_news = news_list[:3]
    #         return render_template("search-result.html", user=user, news=back_news)
    #
    # # loadmore部分的内容
    # if request.method == "POST":
    #     user = session.get("user")
    #     num = int(request.form.get("num"))
    #     # 向上取整然后，判断
    #     length = math.ceil(len(session["news_list"]) / 3)
    #     if user:
    #         if num == length - 1:
    #             back_news = session["after_news_list"][num * 3:]
    #             # 返回的数据num是判断是否是完全取出数据的用处
    #             return jsonify({"result": back_news, "flag": 0, "has_user": 1})
    #         else:
    #             back_news = session["after_news_list"][num * 3: num * 3 + 3]
    #             return jsonify({"result": back_news, "flag": 1, "has_user": 1})
    #     else:
    #         if num == length - 1:
    #             back_news = session["news_list"][num * 3:]
    #             return jsonify({"result": back_news, "flag": 0, "has_user": 0})
    #         else:
    #             back_news = session["news_list"][num * 3: num * 3 + 3]
    #             return jsonify({"result": back_news, "flag": 1, "has_user": 0})
    user = session.get('user', "")  # 当用户没有登录时，可以获取页面评论
    keyword = request.args.get("kw")
    print(keyword)
    if is_url(keyword):
        content = baidu_search_service(keyword)
        news_obj = {'title': content[0][1], 'url': content[0][0]}
    else:
        content = baidu_search_service2(keyword, 10)
        news_obj = {'title': keyword, 'url': content[0][0]}

    info = {'data': str(content)}

    # 将keyword content 存入数据库 获得新闻id
    search = Search_result(keyword=keyword, content=str(content))

    db.session.add(search)
    db.session.flush()
    search_id = search.id
    print(search_id)

    user = session.get("user")
    if user:
        record_search = RecordSearch(user_id=user.get("user_id"), search_result_id=search_id)
        db.session.add(record_search)
        db.session.commit()
    db.session.commit()

    # 新开线程 发送信息至处理节点
    searchThread = SearchThread(content, search_id)
    searchThread.start()

    return render_template('news-detail.html', user=user, final_maj_event=[], web_url=keyword, people_list=[],
                           relation=[], relation2=[], news_obj=news_obj, id=search_id)


@csrf.exempt
@app.route("/manage/record/", endpoint="record", methods=["POST", "GET"])
@decortor(session)
def record():
    if request.method == "GET":
        user = session.get('user')
        total_record = RecordSearch.query.filter_by(user_id=user.get("user_id"))

        data = []
        for record_ in total_record:
            search_result = Search_result.query.get(record_.search_result_id)
            record_id = record_.id
            keyword = search_result.keyword
            search_time = search_result.create_at
            status = "已完成" if record_.status else "正在搜索..."
            try:
                search_href = eval(search_result.content)[0][0]
            except Exception as e:
                print(e)
                search_href = "#"
            data.append({"record_id": record_id,
                         "keyword": keyword,
                         "search_time": search_time,
                         "status": status,
                         "search_href": search_href})

        return render_template("search-recode.html", user=user, searches=data)
    else:
        status = request.form.get("status")
        record_id = request.form.get("record_id")
        if record_id and int(status):
            RecordSearch.query.filter_by(id=record_id).update({"status": int(status)})
            db.session.commit()
            return "success"
        else:
            return "error"

# 接口调用 http://127.0.0.1:5000/manage/record/  类型post: 数据form表单格式 status:1, reecord_id:记录的id



@csrf.exempt
@app.route("/news_detail/<id>", methods=["POST", "GET"])
def news_details(id):
    user = session.get('user', "")  # 当用户没有登录时，可以获取页面评论
    search = Search_result.query.filter_by(id=id).first()
    print()
    final_maj_event = search.maj_event
    if final_maj_event:
        final_maj_event = eval(final_maj_event)
    keyword = search.keyword
    people_list = search.people_list
    if people_list:
        people_list = eval(people_list)
    relation1 = search.relation1
    if relation1:
        relation1 = eval(relation1)
    relation2 = search.relation2
    if relation2:
        relation2 = eval(relation2)
    content = eval(search.content)
    if is_url(keyword):
        news_obj = {'title': content[0][1], 'url': content[0][0]}
    else:
        news_obj = {'title': keyword, 'url': content[0][0]}
    return render_template('news-detail.html', user=user, final_maj_event=final_maj_event, web_url=keyword,
                           people_list=people_list, relation1=relation1, relation2=relation2, news_obj=news_obj, id=id)


def analysis(info, id):
    destinip = '127.0.0.1'
    destinport = '9000'
    info = {'head': command_head['send_nlp_task'], 'allevtList': str(info), 'destinip': destinip,
            'destinport': destinport}
    r = requests.post("http://" + destinip + ":9200/set_task", data=info)  # 指令节点发送任务
    response = json.loads(r.text)
    print(response)

    if response['head'] == command_head['response_nlp_task']:
        task_id = response['task_id']
        while True:
            try:
                info = {'head': command_head['take_nlp_result'], 'task_id': task_id}
                r = requests.post("http://" + destinip + ":9200/take_final_result", data=info)
                response = json.loads(r.text)
                if response['head'] == command_head['final_nlp_result']:
                    print(response['result'])
                    break
            except Exception as e:
                print(e)
                pass
            time.sleep(1)
    else:
        print('指令出错')
    result1 = eval(response['result']['result'])
    result2 = result1['result']
    mainBoneTxt4_ltp_nlp = result1['mainBoneTxt4_ltp_nlp']
    result_tuple = result1['result_tuple']

    result = (result2, mainBoneTxt4_ltp_nlp, result_tuple)
    people_list = []
    relation1 = deal_relation(result[2][1])
    relation2 = deal_relation(result[2][2])

    people_info_words = result[2][9]
    maj_event = result[2][0]
    print(maj_event)
    final_maj_event = []
    for i in maj_event:
        people_pic = []
        if not i[1]:
            continue
        for people in i[1]:
            if not people in people_list:
                has_pic = False
                image_result = func(people)
                for j in image_result:
                    pic = j[0]
                    html = j[1]
                    for word in people_info_words[people]:
                        if word in html:
                            people_pic.append(pic)
                            has_pic = True
                            people_list.append(people)
                            break
                    if has_pic:
                        break
        i = list(i)
        i[1] = people_pic
        final_maj_event.append(i)
    print()

    # final_maj_event = [['据香港媒体报道，随后陈冠希通过经纪公司回应', ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562839706949&di=cd39cf4927f3808b8449b0cabb738556&imgtype=0&src=http%3A%2F%2Fimg1.utuku.china.com%2F542x0%2Fnews%2F20170503%2F5b6d2d3f-a964-4294-95e4-10099b86efb4.jpg'], ['陈冠希', '香港']], ['陈冠希默认恋情新女友曝光系离婚超模', [], ['陈冠希']], ['陈冠希热吻认恋情，因为“艳照门”低调做人多年的陈冠希，最近出现的越来越频繁，除了即将出演内地著名导演娄烨新片《风中有朵雨做的云》，恋情动向也日趋明朗', ['https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=467729446,3084458073&fm=26&gp=0.jpg'], ['艳照门', '娄烨', '陈冠希']], ['据香港媒体报导，陈冠希日前和一群朋友聚会，先是被拍到在路边放松地抽烟、抓裤档，接着又和一位白衣女子亲密打闹，霸气勾住对方的腰拉到身边，说话时还伸手拍女方屁股，公开打情骂俏', [], ['陈冠希', '香港']], ['聚会结束后，陈冠希把女子送回酒店，又在路边大方接吻，对于新恋情似乎毫不避讳，事后也向港媒默认', [], ['陈冠希']], ['秦舒培是09春夏纽约时装周杀出的一匹黑马，从此成为海报网编编最为关注的中国超模之一', ['https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3505792986,2726148285&fm=26&gp=0.jpg'], ['中国', '秦舒培', '纽约']], ['她当时并未证实和陈冠希的绯闻，不过如今被拍到接吻亲密照，恋情终于坐实', [], ['陈冠希']], ['恋情秦舒培个人资料', [], ['秦舒培']], ['恋情秦舒培', [], ['秦舒培']], ['秦舒培是什么咖位的名模?和赵磊有什么纠葛?和陈冠希又是何时搭上的?现在开扒', ['https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1259532195,3076912740&fm=26&gp=0.jpg'], ['赵磊', '陈冠希', '秦舒培']], ['陈冠希又恋爱了，这次的对象是人妻名模秦舒培', [], ['陈冠希', '秦舒培']], ['据港媒报道，陈冠希已经默认了这次的恋情', [], ['陈冠希']], ['而现年26岁的秦舒培4年前就嫁给了自己的老板赵磊，至于离没离婚，两人也是各执一词', [], ['赵磊', '秦舒培']], ['相关推荐陈冠希新女友秦舒培陈冠希新女友是谁秦舒培个人资料', ['https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1523397831,641206919&fm=26&gp=0.jpg'], ['秦舒培陈冠希', '陈冠希']], ['2009年底香奈儿(CHANEL)巴黎-上海高级手工坊大秀上，秦舒培第3位出场，受到“老佛爷”KarlLagerfeld垂青，更令她成为笑傲国际T台的中国超模新势力', [], ['Karl Lagerfeld', '老佛爷', '巴黎', '秦舒培', 'CHANEL', '上海', '中国']], ['事实上，该名女子是25岁的大陆名模秦舒培，曾在纽约、巴黎等各大国际秀场走秀，2012年嫁给华谊兄弟总经理赵磊，但2015年被曝光一张坐陈冠希大腿的亲密照，传出已经跟老公离婚', ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562840104133&di=24d6f5d9318b71340e71b0a216ab50f6&imgtype=0&src=http%3A%2F%2Fatt2.citysbs.com%2Fhangzhou%2F2019%2F07%2F10%2F09%2Fmiddle_960x720-094821_v2_17951562723301603_715d59cbff2a195b469dc9105899c33b.jpg'], ['陈冠希', '巴黎', '纽约', '赵磊', '秦舒培', '老公', '华谊']], ['女方的身份随后也被证实，正是2015年因为“坐大腿”照而和陈冠希传过绯闻的25岁超模秦舒培', [], ['陈冠希', '秦舒培', '坐大腿']], ['两人被拍到在街头亲吻，陈冠希还轻拍女方臀部，2015年两人就被传出同游美国，还有坐大腿的亲密合照在网络流传，如今这桩绯闻再添铁证', [], ['陈冠希', '美国']], ['2016年5月30日，据台湾媒体报道，陈冠希和一群朋友外出聚餐时，与一名长发长腿的女性互动亲密，在大街上便毫不避讳地对其摸臀揽腰，甜蜜热吻', [], ['2016年5月30日', '陈冠希', '台湾']]]
    # keyword = 'http://bj.bendibao.com/news/201661/226473.shtm'
    # people_list = ['陈冠希', '娄烨', '秦舒培', '赵磊', '秦舒培陈冠希', '老公']
    # relation1 = {'data': {'nodes': [{'id': '1', 'labels': ['item'], 'properties': {'logo': '', 'name': '台湾', 'ntype': 'f'}}, {'id': '2', 'labels': ['item'], 'properties': {'logo': '', 'name': '陈冠希', 'ntype': 'f'}}, {'id': '3', 'labels': ['item'], 'properties': {'logo': '', 'name': '香港', 'ntype': 'f'}}, {'id': '4', 'labels': ['item'], 'properties': {'logo': '', 'name': '赵磊', 'ntype': 'f'}}, {'id': '5', 'labels': ['item'], 'properties': {'logo': '', 'name': '秦舒培', 'ntype': 'f'}}, {'id': '6', 'labels': ['item'], 'properties': {'logo': '', 'name': '纽约', 'ntype': 'f'}}], 'relationships': [{'id': '1000', 'startNode': '1', 'endNode': '2', 'properties': {'labels': ['朋友']}, 'type': 'BRANCH'}, {'id': '1001', 'startNode': '3', 'endNode': '2', 'properties': {'labels': ['朋友']}, 'type': 'BRANCH'}, {'id': '1002', 'startNode': '4', 'endNode': '5', 'properties': {'labels': ['离婚']}, 'type': 'BRANCH'}, {'id': '1003', 'startNode': '5', 'endNode': '4', 'properties': {'labels': ['嫁给']}, 'type': 'BRANCH'}, {'id': '1004', 'startNode': '2', 'endNode': '5', 'properties': {'labels': ['恋爱']}, 'type': 'BRANCH'}, {'id': '1005', 'startNode': '5', 'endNode': '6', 'properties': {'labels': ['嫁给']}, 'type': 'BRANCH'}]}}
    # relation2 = {'data': {'nodes': [{'id': '1', 'labels': ['item'], 'properties': {'logo': '', 'name': '香港', 'ntype': 'f'}}, {'id': '2', 'labels': ['item'], 'properties': {'logo': '', 'name': '陈冠希', 'ntype': 'f'}}, {'id': '3', 'labels': ['item'], 'properties': {'logo': '', 'name': '秦舒培', 'ntype': 'f'}}, {'id': '4', 'labels': ['item'], 'properties': {'logo': '', 'name': '老佛爷', 'ntype': 'f'}}], 'relationships': [{'id': '1000', 'startNode': '1', 'endNode': '2', 'properties': {'labels': ['公司']}, 'type': 'BRANCH'}, {'id': '1001', 'startNode': '2', 'endNode': '3', 'properties': {'labels': ['绯闻']}, 'type': 'BRANCH'}, {'id': '1002', 'startNode': '4', 'endNode': '3', 'properties': {'labels': ['国际']}, 'type': 'BRANCH'}]}}
    # news_obj = {'title': '陈冠希新女友秦舒培是谁?个人资料背景大揭秘(组图)- 北京本地宝', 'url': 'http://bj.bendibao.com/news/201661/226473.shtm'}

    try:
        relation_list = session.get('relation')
    except:
        relation_list = {}
    if not relation_list:
        relation_list = {}
    relation_list[id] = {'relation1': relation1, 'relation2': relation2}
    session['relation'] = relation_list

    search = Search_result.query.filter_by(id=id).first()
    search.relation1 = relation1
    search.relation2 = relation2
    search.maj_event = final_maj_event
    search.people_list = people_list
    db.session.add(search)
    db.session.commit()


# @app.route('/topic/<id>')  # 话题
# def topic(id):
#     result_obj = db.session.query(search_result).filter_by(search_id=id).first()
#     user = session.get('user')
#     if result_obj:
#         return render_template('topic.html', result_obj=result_obj, user=user, id=id)
#     return abort(404)


@app.route('/source/<id>')
def source(id):
    detail = NewsDetail.query.filter(NewsDetail.news_id == id).first()

    relation = deal_relation(eval(detail.relation))
    return render_template('source.html', relation=relation)


@app.route('/source_show/<id>&<kind>')
def source2(id, kind):
    search = Search_result.query.filter_by(id=id).first()
    # relation1 = search.relation1
    # relation2 = search.relation2
    if kind == 'relation1':
        relation = eval(search.relation1)
    elif kind == 'relation2':
        relation = eval(search.relation2)
    else:
        relation = []
    # try:
    #     relation_list = session.get('relation')
    # except:
    #     relation_list = {}
    # if not relation_list:
    #     relation_list = {}
    # if kind=='relation1':
    #     relation = relation_list[id]['relation1']
    # elif kind=='relation2':
    #     relation = relation_list[id]['relation2']
    # else:
    #     relation = []
    return render_template('source.html', relation=relation)


@app.route('/download')
def download():
    destinip = '127.0.0.1'
    destinport = '9113'
    r = requests.get("http://" + destinip + ":" + destinport + "/nodes")  # 发送搜索结果
    response = json.loads(r.text)
    print(response)

    return render_template('download.html', nodes=response)


@app.route('/map')
def map():
    # while True:
    #     try:
    #         response = requests.get(url="http://119.3.50.104:9100/get_node_list", timeout=10)
    #         if response.status_code == 200:
    #             break
    #     except:
    #         time.sleep(2)
    #         continue
    # data = json.loads(response.text)
    # nodes = eval(data.get("node"))
    while True:
        try:
            r = requests.get("http://www.heiyunworld.com:90/task/all_node_info/")
            break
        except:
            time.sleep(5)
    node_list = json.loads(r.text).get('msg')
    # for i in node_list:
    #     print(i)

    if len(node_list) != 0:
        back_data = {}
        name_value_list = []
        for node in node_list:
            node_ip = node[2]
            node_name = node[0]
            origin_type = node[1]
            longitude = node[3]
            latitude = node[4]
            # if "x" in longitude_latitude:
            if node_name in back_data:
                i = 1
                while True:
                    node_name_ = node_name + str(i)
                    i += 1
                    if node_name_ not in back_data:
                        node_name = node_name_
                        break
            # back_data[node_type] = [longitude_latitude.get("x"), longitude_latitude.get("y")]
            back_data[node_name] = [longitude, latitude]
            name_value_list.append({"name": node_name, "value": 10, 'type': origin_type})
        print(back_data)
        print(name_value_list)
        # return render(request, "2222散点.html", {"back_data": json.dumps(back_data), "name_value": json.dumps(name_value_list)})
        return render_template('map.html', back_data=json.dumps(back_data), name_value=json.dumps(name_value_list))
    else:
        # return render(request, "2222散点.html")
        return render_template('map.html')


def deal_relation(data):
    relation = {'data': {'nodes': [], 'relationships': []}}
    node_id = 1
    rela_id = 1000
    node = {}
    # data = data[0]
    for i in data:
        if not i:
            continue
        # i = i[0]
        if not i[0]:
            continue
        if i[0] == i[2]:
            continue
        if i[0] not in node:
            relation['data']['nodes'].append(
                {'id': str(node_id), 'labels': ['item'], 'properties': {'logo': '', 'name': i[0], 'ntype': 'f'}})
            node[i[0]] = node_id
            node_id += 1
        if i[2] not in node:
            relation['data']['nodes'].append(
                {'id': str(node_id), 'labels': ['item'], 'properties': {'logo': '', 'name': i[2], 'ntype': 'f'}})
            node[i[2]] = node_id
            node_id += 1
        relation['data']['relationships'].append(
            {'id': str(rela_id), 'startNode': str(node[i[0]]), 'endNode': str(node[i[2]]),
             'properties': {'labels': [i[1]]}, 'type': 'BRANCH'})
        rela_id += 1
    print(relation)
    return relation


# 搜索兴趣点相关内容
# t = threading.Thread(target=get_news_from_database, )
# t.start()

@app.route("/download_file/<filename>", methods=['GET'])
def download_file(filename):
    # # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    # directory = '../static/file'
    # return send_from_directory(directory, filename, as_attachment=True)
    # filename = taskid + 'xxx.xlsx'
    directory = 'file/' + filename
    # response = make_response(send_from_directory(directory, filename, mimetype='application/octet-stream'))
    # return response
    # file_name = safe_join(directory, filename)
    # print(flask.safe_join(UPLOAD_FOLDERS, secure_filename(filename)))
    # print(os.path.isfile(filename))
    return send_file(directory, as_attachment=True)


@app.route('/location/<id>', methods=['GET'])
def location(id):
    ip = request.remote_addr
    # ip = '49.51.40.176'
    result = send_url(ip)
    data = {
        "node_id": id,
        "latitude": result[1],
        "longitude": result[0]
    }

    while True:
        try:
            try:
                r = requests.post("http://www.heiyunworld.com:90/task/add_node_location/", data=data)
                print(r.text)
                break
            except:
                return 'error'
        except:
            time.sleep(5)
    return 'success'


if __name__ == '__main__':
    app.run(threaded=True)
