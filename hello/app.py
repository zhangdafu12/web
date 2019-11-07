from flask import Flask, render_template
from flask import request
from testXml import writeXMLPoints
from deal4 import convert
import pymysql
import re

session_1, session_2, session_3 = 0, 0, 0

app = Flask(__name__)


@app.route('/', methods=['POST', "GET"])
def getpage1():
    if request.method == "GET":
        return render_template('page1.html')
    if request.method == "POST":
        if request.form.get("question", ""):  # 执行搜索操作
            target = request.form.get("question")
            db = pymysql.connect(host="localhost", user="root", password="123456", db="translation", port=3306)
            cursor = db.cursor()
            sql = "SELECT * FROM api WHERE describe_ LIKE '%{}%'".format(target)
            cursor.execute(sql)
            result = []
            for each in cursor.fetchall():
                each_dic = {}
                each_dic["apiname"] = each[1]
                each_dic["param"] = ",".join(each[2:5])
                each_dic["name"] = each[-1]
                each_dic["describe"] = each[5]
                each_dic["tag"] = ",".join(each[-4:-1])
                result.append(each_dic)
            return render_template("page1.html", data=result)
        else:  # 执行插入数据库操作
            apiname = request.form['apiName']
            parm1 = request.form['parm1']
            parm2 = request.form['parm2']
            parm3 = request.form['parm3']
            name = request.form['name']
            describe = request.form['describe']
            tag1 = request.form['tag1']
            tag2 = request.form['tag2']
            tag3 = request.form['tag3']

            db = pymysql.connect(host="localhost", user="root", password="root", db="translation", port=3306)

            sql = "INSERT INTO api(apiname, param1, param2, param3, name, describe_, tag1, tag2, tag3 ) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
                apiname, parm1, parm2, parm3, name, describe, tag1, tag2, tag3)
            cursor = db.cursor()
            try:
                cursor.execute(sql)
                db.commit()
                print("你的数据成功插入数据库！！！！")
            except Exception as e:
                print("你的数据插入数据库失败， 请重新录入！！！！")
                db.rollback()
            return render_template('page1.html')  # 返回到当前页面，可以继续输入


# @app.route('/page2', methods=["POST"])
# def page22():
#     if request.method == "POST":
#         hangye = request.form.get("hangye")
#         data = request.form.get("text")
#         each_line = re.split("\n", data)
#         print()
#         return
#
#     return render_template('page2.html')


@app.route('/page2', methods=['GET', "POST"])
def page2():
    if request.method == 'POST':
        consumer_name = request.values.get("text")
        hangye = request.values.get("hangye")
        print(hangye)
        writeXMLPoints(consumer_name, hangye)
        if consumer_name != "":
            return "success!"

    return render_template('page2.html')


@app.route("/page3", methods=["GET"])
def page3():
    return render_template("page3.html", hangye="服务", tag1="028", tag2="028", tag3="2105", nextName="账户",
                           tag1_1="微信转账", tag1_2="支付宝转账", tag1_3="红包转账",
                           tag1_4="028", tag1_5="028", can1="账户名", can2="账户余额")


@app.route("/page3", methods=['POST'])
def page33():
    if request.method == 'POST':
        searchText = request.values.get("searchText")
        if searchText != "":
            sql = "SELECT * FROM serverdescribe"

        s = []
        backstring = ""
        consumer_name = request.values.get("text")
        with open(consumer_name + ".xml", "r") as f:
            s = str(f.readlines())
        for i in s:
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("\"", "")
            i = i.replace(",", "")
            backstring += i
        backstring3 = backstring.replace("\\n", "</br>")
        print(backstring3)
    return render_template('page3.html', backString3=backstring3)


@app.route('/page4', methods=['POST', "GET"])
def getpage4():
    if request.method == 'POST':
        data = request.values.get("text")

        no_choice_list = re.findall("请选择", data)
        if len(no_choice_list) >= 1:
            print("请选择所有的数据！！！！！！！！！")
            return render_template('page4.html', tag1=session_1, tag2=session_2, tag3=session_3,
                                   account1="账户a", account2="账户b", account3="账户c")
        else:
            result = convert(data)
            if result:
                print(result)
                return "SUCCESS"
            else:
                print("选择数据有误，请重新选择！！！！！！！！")
                return render_template('page4.html', tag1=session_1, tag2=session_2, tag3=session_3,
                                       account1="账户a", account2="账户b", account3="账户c")
    return render_template('page4.html', tag1=session_1, tag2=session_2, tag3=session_3,
                           account1="账户a", account2="账户b", account3="账户c")


if __name__ == '__main__':
    app.run(debug=True)
