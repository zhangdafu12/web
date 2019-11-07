# coding:utf-8
# _author_:Junjie
# date:2018/10/25

# 本地节点:本地任务转发和执行结果请求转发
import hashlib
import time

from flask import Flask,request,json
from config import command_head
import requests
import uuid


app = Flask(__name__)

# global result_list
# result_list = {}


def create_task_id():
    return str(uuid.uuid1())


@app.route('/')
def hello_world():
    return 'command node'


@app.route('/set_task', methods=['POST', 'GET'])
def center_set_task():  # 向106 发送任务
    if request.method == "POST":
        data = {}
        try:
            head = request.form.get('head')
            # global result_list
            if head == command_head['send_sim_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'sim_' + hashlib.sha256(task_id).hexdigest()
                searResltList = request.form.get('searResltList')
                conten2bI = request.form.get('conten2bI')
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_sim_task'], 'task_id': task_id, 'searResltList': searResltList,
                        'conten2bI': conten2bI, 'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_sim_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_search_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'search_' + hashlib.sha256(task_id).hexdigest()
                searchlist = request.form.get('searchlist')
                keywordslist = request.form.get('keywordsList')
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')

                info = {'head': command_head['send_search_task'], 'task_id': task_id, 'searchlist': searchlist,
                        'keywordsList': keywordslist, 'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_search_task']
                data['task_id'] = task_id

                # result_list[task_id] = ''
                # r = requests.post("http://119.3.50.104:9100/set_task", data=info)

            elif head == command_head['send_textparse_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'textparse_' + hashlib.sha256(task_id).hexdigest()
                content = request.form.get('content')
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_textparse_task'], 'task_id': task_id, 'content': content,
                         'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_textparse_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''
                # r = requests.post("http://119.3.50.104:9100/set_task", data=info)

            elif head == command_head['send_deal_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'deal_' + hashlib.sha256(task_id).hexdigest()
                sentList = request.form.get('sentList')
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_deal_task'], 'task_id': task_id, 'sentList': sentList,
                        'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_deal_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_image_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'image_' + hashlib.sha256(task_id).hexdigest()
                # image = request.form.get("uploadfile")
                image = request.form.get("uploadfile")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_image_task'], 'task_id': task_id,
                        'destinip': destinip, 'destinport': destinport,'uploadfile': image}

                data['head'] = command_head['response_image_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_linkin_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'linkin_' + hashlib.sha256(task_id).hexdigest()
                url = request.form.get("url")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_linkin_task'], 'task_id': task_id, 'url': url,
                        'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_linkin_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_whois_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'whois_' + hashlib.sha256(task_id).hexdigest()
                key = request.form.get("searchkey")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_whois_task'], 'task_id': task_id, 'searchkey': key,
                        'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_whois_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''
            elif head == command_head['send_checkmate_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'checkmate_' + hashlib.sha256(task_id).hexdigest()
                first_name = request.form.get("first_name")
                last_name = request.form.get("last_name")
                city = request.form.get("city")
                location = request.form.get("location")
                sex = request.form.get("sex")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_checkmate_task'], 'task_id': task_id, 'first_name': first_name,
                        'last_name': last_name, 'city': city, 'location': location, 'sex': sex,
                        'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_checkmate_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''
            elif head == command_head['send_domain_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'domain_' + hashlib.sha256(task_id).hexdigest()
                key = request.form.get("searchkey")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_domain_task'], 'task_id': task_id, 'searchkey': key,
                        'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_domain_task']
                data['task_id'] = task_id

            elif head == command_head['send_beenverified_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'beenver_' + hashlib.sha256(task_id).hexdigest()
                first_name = request.form.get("first_name")
                last_name = request.form.get("last_name")
                city = request.form.get("city")
                location = request.form.get("location")
                age = request.form.get("age")
                middle_name = request.form.get("middle_name")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_beenverified_task'], 'task_id': task_id, 'first_name': first_name,
                        'last_name':last_name,'city':city,'location':location,'age':age,'middle_name':middle_name,
                        'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_beenverified_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_qqSpider_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'qqSpider_' + hashlib.sha256(task_id).hexdigest()
                qq = request.form.get("qq")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_qqSpider_task'], 'task_id': task_id, 'qq': qq,
                        'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_qqSpider_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_facebook_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'facebook_' + hashlib.sha256(task_id).hexdigest()
                name = request.form.get("name")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_facebook_task'], 'task_id': task_id, 'name': name,
                        'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_facebook_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_wechat_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'wechat_' + hashlib.sha256(task_id).hexdigest()
                number = request.form.get("number")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_wechat_task'], 'task_id': task_id, 'number': number,
                        'destinip': destinip, 'destinport': destinport}
                data['head'] = command_head['response_wechat_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_search2_task']:# 本地一个真实函数，如sendSimTask_test任务测试节点发送过来的参数
                task_id = str(create_task_id()).encode()#生成任务id
                task_id = 'search2_' + hashlib.sha256(task_id).hexdigest()#任务id前增加任务头
                search_word = request.form.get("search_word")# 获取本地传过来的任务值
                destinip = request.form.get('destinip')# 通知任务节点最重返回结果到的ip，现在暂时是固定在106上的
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_search2_task'], 'task_id': task_id, 'search_word': search_word,
                        'destinip': destinip, 'destinport': destinport}# 构造发给106的信息格式
                data['head'] = command_head['response_search2_task']# 构造返回给测试节点的消息内容，向测试节点表明，收到了任务
                data['task_id'] = task_id#向测试节点表明，收到了任务，以及对应的任务id，只有凭借这个task_id，索取任务执行结果
                # result_list[task_id] = ''
            elif head == command_head['evtrelner_task_request']:# 本地一个真实函数，如sendSimTask_test任务测试节点发送过来的参数，开始编写面向evtrelner的解析
                task_id = str(create_task_id()).encode()#生成任务id
                task_id = 'evtrelner_' + hashlib.sha256(task_id).hexdigest()#任务id前增加任务头　'evtrelner'
                # 进入参数解析，暂时保持与搜索任务的参数名一致，没有更改
                search_word = request.form.get("search_word")# 获取本地传过来的任务值
                destinip = request.form.get('destinip')# 通知任务节点最重返回结果到的ip，现在暂时是固定在106上的
                destinport = request.form.get('destinport')
                info = {'head': command_head['evtrelner_task_request'], 'task_id': task_id, 'search_word': search_word,
                        'destinip': destinip, 'destinport': destinport}# 构造发给106的信息格式
                data['head'] = command_head['response_evtrelner_task']# 构造返回给测试节点的消息内容，向测试节点表明，收到了任务
                data['task_id'] = task_id#向测试节点表明，收到了任务，以及对应的任务id，只有凭借这个task_id，索取任务执行结果
                # result_list[task_id] = ''

            elif head == command_head['send_nlp_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'nlp_' + hashlib.sha256(task_id).hexdigest()
                allevtList = request.form.get("allevtList")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_nlp_task'], 'task_id': task_id, 'allevtList': allevtList,
                        'destinip': destinip, 'destinport': destinport}
                print(allevtList)
                data['head'] = command_head['response_nlp_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_jinri_task_1']:
                task_id = str(create_task_id()).encode()
                task_id = 'jinri_1_' + hashlib.sha256(task_id).hexdigest()
                content = request.form.get("content")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_jinri_task_1'], 'task_id': task_id, 'content': content,
                        'destinip': destinip, 'destinport': destinport}
                print(content)
                data['head'] = command_head['response_jinri_task_1']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_jinri_task_2']:
                task_id = str(create_task_id()).encode()
                task_id = 'jinri_2_' + hashlib.sha256(task_id).hexdigest()
                content = request.form.get("content")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_jinri_task_2'], 'task_id': task_id, 'content': content,
                        'destinip': destinip, 'destinport': destinport}
                print(content)
                data['head'] = command_head['response_jinri_task_2']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_jinri_task_3']:
                task_id = str(create_task_id()).encode()
                task_id = 'jinri_3_' + hashlib.sha256(task_id).hexdigest()
                content = request.form.get("content")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_jinri_task_3'], 'task_id': task_id, 'content': content,
                        'destinip': destinip, 'destinport': destinport}
                print(content)
                data['head'] = command_head['response_jinri_task_3']
                data['task_id'] = task_id
                # result_list[task_id] = ''
            elif head == command_head['send_ltp_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'ltp_' + hashlib.sha256(task_id).hexdigest()
                content = request.form.get("content")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_ltp_task'], 'task_id': task_id, 'content': content,
                        'destinip': destinip, 'destinport': destinport}
                print(content)
                data['head'] = command_head['response_ltp_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            elif head == command_head['send_stan_nlp_task']:
                task_id = str(create_task_id()).encode()
                task_id = 'stan_nlp_' + hashlib.sha256(task_id).hexdigest()
                content = request.form.get("content")
                destinip = request.form.get('destinip')
                destinport = request.form.get('destinport')
                info = {'head': command_head['send_stan_nlp_task'], 'task_id': task_id, 'content': content,
                        'destinip': destinip, 'destinport': destinport}
                print(content)
                data['head'] = command_head['response_stan_nlp_task']
                data['task_id'] = task_id
                # result_list[task_id] = ''

            else:
                data['head'] = command_head['command_error']
                info=[]
                # return json.dumps(data, ensure_ascii=False)
            while True:
                try:
                    r = requests.post("http://119.3.50.104:9100/set_task", data=info)  # 向106发送任务
                    # r = requests.post("http://127.0.0.1:9100/set_task", data=info)  # 向106发送任务
                    break
                except:
                    time.sleep(5)
            # r = requests.post("http://119.3.50.104:9100/set_task", data=info)# 向106发送任务
            response = json.loads(r.text)  # 106返回受到任务的确认
            print(response)
            return json.dumps(data, ensure_ascii=False)  # 向本地测试节点发送任务id
        except Exception as e:
            print(e)
            data['head'] = command_head['command_error']
            return json.dumps(data, ensure_ascii=False)


@app.route('/take_final_result', methods=['POST', 'GET'])
def get_final_result():  # 从106请求任务结果
    if request.method == "POST":
        data = {}
        head = request.form.get('head')
        task_id = request.form.get('task_id')
        try:
            r = requests.post("http://119.3.50.104:9100/take_final_result", data={"head":head,"task_id":task_id})
            # r = requests.post("http://127.0.0.1:9100/take_final_result", data={"head":head,"task_id":task_id})
            response = json.loads(r.text)
            data['head'] = response['head']
            data['result'] = response['result']
        except Exception as e:
            data["head"] = "err"
        return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9200)
