# -*- encoding:utf8 -*-
# author: Shulei
# e-mail: 1191543592@qq.com
# time:  2019/4/2 19:55
from flask import Flask, request, render_template, abort
from flask_wtf import CsrfProtect
import time

from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "13454578"
csrf = CsrfProtect(app)



@app.route('/')  # 首页
def index():
    print(time.time())
    time.sleep(60)
    print("=============================================")
    return render_template('test.html')


@app.route('/regist', methods=['POST'])  # 首页
def index1():
    form = RegistForm(request.form)
    print(form.name.data, form.email.data, form.password.data, form.confirm.data)
    print(form.validate_on_submit())
    print(form.validate())
    if request.method == 'POST' and form.validate():
        print(form.name.data, form.email.data, form.password.data)
        return 'ok'
    return 'err'


if __name__ == '__main__':
    app.run(debug=True)
