# -*- encoding:utf8 -*-
# author: Shulei
# e-mail: 1191543592@qq.com
# time:  2019/4/2 11:56
import random
import re
from _datetime import datetime
from collections import Counter
import jieba
import operator
import pymysql
import requests
from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string '
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@192.168.3.84:3306/netta"
db = SQLAlchemy(app)
# db = SQLAlchemy()

# 新闻和用户中间表
middle_mylike = db.Table("middle_mylike",
                         db.Column("user_id", db.Integer, db.ForeignKey("users.user_id")),
                         db.Column("news_id", db.Integer, db.ForeignKey("news.news_id"))
                         )


# 用户表
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)  # 主键
    account = db.Column(db.String(32), unique=True, nullable=False)  # 添加索引，不能为空
    passwd = db.Column(db.String(32), nullable=False)
    nick_name = db.Column(db.String(32), unique=True)
    true_name = db.Column(db.String(32))
    sex = db.Column(db.String(32))
    head_pic = db.Column(db.String(255))
    birthday = db.Column(db.String(32))
    province = db.Column(db.String(32))
    country = db.Column(db.String(32))
    city = db.Column(db.String(32))
    description = db.Column(db.String(255))  # 个人描述内容
    is_administrator = db.Column(db.Boolean, default=False,
                                 nullable=False)  # 管理员或者普通用户， 默认是普通用户，当设置为True的时候为管理员（验证邮箱是否要设置成管理员用户）

    news = db.relationship("News",
                           secondary=middle_mylike,
                           backref=db.backref("users", lazy='dynamic'),
                           lazy='dynamic'
                           )

    comments = db.relationship("Comment", backref="users", lazy="dynamic")  # 评论的外链接

    give_likes = db.relationship("GiveLike", backref="users", lazy="dynamic")  # 点赞的外链接

    notifyreminds = db.relationship("NotifyRemind", backref="users", lazy="dynamic")  # 消息推送的外链接


def user_2_json(obj):
    return {'user_id': obj.user_id,
            'account': obj.account,
            'passwd': obj.passwd,
            'nick_name': obj.nick_name if obj.nick_name else '',
            'true_name': obj.true_name,
            'sex': obj.sex,
            'head_pic': obj.head_pic,
            "province": obj.province,
            "city": obj.city,
            "country": obj.country,
            "description": obj.description if obj.description else ""}


class Interest(db.Model):
    __tablename__ = 'interest'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    news_id = db.Column(db.Integer, db.ForeignKey("news.news_id"), index=True)
    interest = db.Column(db.String(64))


class UserInterest(db.Model):
    __tablename__ = 'user_interest'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    interest = db.Column(db.String(64), index=True, )
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))


class NewsDetail(db.Model):
    __tablename__ = 'news_detail'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    relation = db.Column(LONGTEXT)
    words = db.Column(LONGTEXT)
    weight = db.Column(LONGTEXT)
    event = db.Column(LONGTEXT)
    news_id = db.Column(db.Integer, db.ForeignKey("news.news_id"), index=True)


# 新闻表
class News(db.Model):
    __tablename__ = 'news'
    news_id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    news_time = db.Column(db.DateTime)
    author = db.Column(db.String(64))
    watch_num = db.Column(db.INTEGER)
    comment_num = db.Column(db.INTEGER)
    like_num = db.Column(db.INTEGER)
    img = db.Column(db.String(255))
    url = db.Column(db.Text)
    comments = db.relationship("Comment", backref="news", lazy="dynamic")
    interest = db.relationship("Interest", backref="news", lazy="dynamic")
    # interest_id = db.Column(db.Integer, db.ForeignKey('interest.id'))
    words = db.Column(db.Text)


def news_2_json(obj):
    return {'news_id': obj.news_id,
            'title': obj.title,
            'content': obj.content,
            'news_time': obj.news_time if obj.news_time else '',
            'author': obj.author,
            'watch_num': obj.watch_num,
            'comment_num': obj.comment_num,
            "like_num": obj.like_num,
            "img": obj.img,
            "url": obj.url}


# 搜索结果一条条新闻数据组成的集合
# news >>> 结果 一对多的关系
# 用户 >>> 结果 一对多的关系
class Search_result(db.Model):
    __tablename__ = 'search_result'
    id = db.Column(db.Integer, primary_key=True)  # 主键
    keyword = db.Column(db.String(255))
    maj_event = db.Column(db.Text)
    people_list = db.Column(db.Text)
    relation1 = db.Column(db.Text)
    relation2 = db.Column(db.Text)
    content = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default=datetime.now)


class RecordSearch(db.Model):
    __tablename__ = "record_search"
    id = db.Column(db.Integer, primary_key=True)
    search_result_id = db.Column(db.Integer, db.ForeignKey("search_result.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    status = db.Column(db.Boolean, default=0)
    create_at = db.Column(db.DateTime, default=datetime.now)


# 评论模型， 评论和回复进行拆开，即此张评论表就是直接评论的新闻主题，不再需要目标用户字段
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    agree_num = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    news_id = db.Column(db.Integer, db.ForeignKey("news.news_id"))
    replies = db.relationship("CommentReply", backref="comments", lazy="dynamic")


# 回复表
class CommentReply(db.Model):
    __tablename__ = "replies"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now())
    from_uid = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    to_uid = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"))
    agree_num = db.Column(db.Integer, default=0)
    #
    reply_id = db.Column(db.Integer)  # 回复的回复id【当reply_type为reply时】或者回复的评论id(即评论挂载的第一个回复的情况)【当reply_type为comment】
    reply_type = db.Column(db.String(64))  # 回复的类型 comment 和reply 2种类型


# 评论回复点赞表
class GiveLike(db.Model):
    __tablename__ = "givelike"
    id = db.Column(db.Integer, primary_key=True)
    con_rep_id = db.Column(db.Integer)  # 评论或者回复的id,需要记录与点赞用户的关系
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))  # 用户和点赞的关系是一对多关系
    like_type = db.Column(db.String(64))  # comment/reply 给予点赞的是什么内容


# 消息通知系统


# 资源发布提醒（主要是针对自己发布过的资源进行评论、回复、点赞的消息推送）
class NotifyRemind(db.Model):
    __tablename__ = "notify_remind"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipientID = db.Column(db.Integer, db.ForeignKey("users.user_id"))  # 接受消息用户的id，一个用户对应多个推送消息
    kind = db.Column(db.String(64))  # 回复、点赞、删除
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)  # 消息创建的时间
    status = db.Column(db.Boolean, default=False)  # 该条提醒消息的状态，默认为未读状态
    from_user_name = db.Column(db.String(64))
    content = db.Column(db.Text)
    news_id = db.Column(db.Integer)

    def __repr__(self):
        return f"NotifyRemind 对象: {self}"


def search_news(num, key_word=''):
    db2 = pymysql.connect("192.168.3.84", "root", "123456", "netta", charset='utf8')
    cursor = db2.cursor()
    if key_word:
        sql = f"SELECT * From news where words like \'%{key_word}%\' limit {num}"
    else:
        sql = f"SELECT * From news limit {num}"
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    db2.close()
    return data


def filter_emoji(desstr, restr=''):
    # 过滤表情
    content = desstr
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    try:
        result = co.sub(restr, desstr)
    except:
        result = content
    return result


def deal_word(word):
    word = word.replace(' ', '').replace('\n', '').replace('\r\t', '')
    return word


def weighted_xigama_sorting(inters_wd_set, founded_info_li):
    weight_xigam_id_tp_li = []
    for ev_tp in founded_info_li:
        weight_xigam = 0
        ev_dic = ev_tp[1][0]
        for ev_wd in inters_wd_set:
            try:
                weight_xigam += ev_dic[ev_wd][0] * ev_dic[ev_wd][1]
            except Exception as te:
                continue
        weight_xigam_id_tp_li.append((ev_tp[0], weight_xigam))
    weight_xigam_id_tp_li = sorted(weight_xigam_id_tp_li, key=lambda x: x[1], reverse=True)
    return weight_xigam_id_tp_li


def get_recommand(id):
    # key = key.split(',')
    detail = NewsDetail.query.filter(NewsDetail.news_id == id).first()
    try:
        words = eval(detail.words)
    except:
        return []

    result = []
    ids = []
    for i in words:
        que = Interest.query.filter(Interest.interest == i).all()

        # print(result)
        for i in que:
            ids.append(i.news_id)
            # print(i.news_id)

    c_id = Counter(ids)
    ided = sorted(c_id.items(), key=operator.itemgetter(1), reverse=True)
    fin_id = []
    if len(ided) > 20:
        for i in ided[0:10]:
            fin_id.append(i[0])
    else:
        for i in ided:
            fin_id.append(i[0])
    words_detail = []  # 相关网页高频词权重集合
    for i in fin_id:
        w = NewsDetail.query.filter(NewsDetail.news_id == i).first()
        if w:
            words_detail.append((w.news_id, eval(w.weight)))
        # a = News.query.get(i)
        # result.append((a.news_id,a.title,a.content,a.news_time,a.author,a.watch_num,a.comment_num,a.like_num,a.img,a.url,a.words))
        # print(a.title)
    sorted_url_li = weighted_xigama_sorting(words, words_detail)
    max_urls_num = 5  # 设置最大推荐数
    if len(sorted_url_li) > 5:  # 选择 前若干个
        sorted_url_li = sorted_url_li[0:max_urls_num]
    # 收集网页结果
    for ev_tp in sorted_url_li:
        a = News.query.get(ev_tp[0])
        result.append((a.news_id, a.title, a.content, a.news_time, a.author, a.watch_num, a.comment_num, a.like_num,
                       a.img, a.url, a.words))
    # print()

    return result


def get_news_by_word(word):
    ids = []
    result = []
    que = Interest.query.filter(Interest.interest == word).all()

    # print(result)
    for i in que:
        ids.append(i.news_id)
        # print(i.news_id)

    c_id = Counter(ids)
    ided = sorted(c_id.items(), key=operator.itemgetter(1), reverse=True)
    fin_id = []
    if len(ided) > 20:
        for i in ided[0:10]:
            fin_id.append(i[0])
    else:
        for i in ided:
            fin_id.append(i[0])

    for i in fin_id:
        a = News.query.get(i)
        result.append((a.news_id, a.title, a.content, a.news_time, a.author, a.watch_num, a.comment_num, a.like_num,
                       a.img, a.url, a.words))

    return result


def get_bottom_left(id):
    result = []
    a = UserInterest.query.filter(UserInterest.user_id == id).all()
    print(a)
    for i in a:
        print(i.interest)
        if i.interest:
            result += get_news_by_word(i.interest)
    random.shuffle(result)
    return random.sample(result, 20)


def get_news():
    return get_bottom_left(1)


def add_interset(user_id, words):
    a = UserInterest.query.filter(UserInterest.user_id == user_id).all()
    interests = []
    for i in a:
        interests.append(i.interest)
    for word in words.split(','):
        if word not in interests:
            inter = UserInterest(interest=word, user_id=user_id)
            db.session.add(inter)
            db.session.commit()


def add_news_detail(id, relation, words, event, weight):
    # news = News.query.get(id)
    # relation = deal(news.content)
    detail = NewsDetail(news_id=id, relation=relation, words=words, event=event, weight=weight)
    db.session.add(detail)
    db.session.commit()


if __name__ == '__main__':
    # a = search_news(num=7)
    # print(a)
    # db.drop_all()
    db.create_all()
    # for i in range(2013,10000):
    #     try:
    #         news = News.query.get(i)
    #     except:
    #         continue
    #     if news:
    #         if news.news_time:
    #             if not type(news.news_time) == str:
    #                 web_time = news.news_time.strftime("%Y%m%d%H%M%S")
    #         else:
    #             web_time = ''
    #         data = [(news.url,news.title,web_time,news.content,news.title,'')]
    #         info = {"content":str(data)}
    #         r = requests.post("http://192.168.3.134:9988/", data=info)
    #         response = json.loads(r.text)
    #         print(response)
    #         try:
    #             if eval(response['relL']):
    #                 relation = [i for i in eval(response['relL'])[0] if i]
    #             else:
    #                 relation = []
    #         except:
    #             relation = []
    #         words = []
    #         for j in eval(response['reuslt_dict_tuple']):
    #             if type(j)==dict:
    #                 for key,value in j.items():
    #                     words.append(key)
    #             elif type(j)==list:
    #                 words += j
    #         add_news_detail(i,str(relation),str(words),response['mergedEvt_li'],response['reuslt_dict_tuple'])
    #         for x in words:
    #             print(x)
    #             interest = Interest(interest=x, news_id=i)
    #             db.session.add(interest)
    #             db.session.commit()

    # db.create_all()
    # app.run()
    # file = r'D:\Junjie_Space\git\soloTaskCapsulation\test_search2\data\-7755379329499152025\data.txt'
    # with open(file,'r',encoding='utf8') as f:
    #     data = eval(f.read())
    #     print(data)
    #     result = []
    #     url = set()
    #     for i in data:
    #         if not i[0] in url:
    #             result.append(i)
    #     for i in result:
    #         news = News(title=i[1],url=i[0],content=filter_emoji(i[2]),words='猪疫情')
    #         db.session.add(news)
    #         db.session.flush()
    #         # 输出新插入数据的主键
    #         news_id = news.news_id
    #         # print(news_id)
    #         interest = Interest(interest='猪疫情',news_id=news_id)
    #         db.session.add(interest)
    #         # interest = Interest(interest='虐待',news_id=news_id)
    #         # db.session.add(interest)
    #         # interest = Interest(interest='腐败',news_id=news_id)
    #         # db.session.add(interest)
    #
    #         db.session.commit()
    # app.run()
    # a = get_recommand('华为')
    # print(a)
    # words = 'aaa,aaa'
    # words = words.split(',')
    # print(words)
    # interest = Interest(interest='台湾')
    # db.session.add(interest)

    # for i in a:
    #     print(i)
    #     news = News(title=i['title'], author='a', img=i['img'], url=i['news_url'],
    #                 words=','.join(i['key_word']))
    #     db.session.add(news)
    #
    # db.session.commit()
    # app.run()
    # a = get_bottom_left(1)
    # print(a)
