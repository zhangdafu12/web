# -*- coding: utf-8 -*-

from flask import redirect, url_for, request


# 验证登录装饰器
def decortor(sess):
    def wrapper(func):
        def nett(*args, **kwargs):
            if not sess.get("user"):

                # 当有ajax请求的时候，返回None可以进入ajax的error函数
                if request.method == "POST":
                    return
                else:
                    return redirect(url_for(".index"))
            return func(*args, **kwargs)
        return nett
    return wrapper


