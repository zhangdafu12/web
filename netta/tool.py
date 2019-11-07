# coding:utf-8
# _author_:Junjie
# date:2019/7/14

import re


def is_url(urlStr):
    isurl = False

    regex1 = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    regex2 = re.compile(
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if regex1.match(urlStr) != None:
        regexp = re.compile(u'[\u4e00-\u9fa5]|[\*\!\@\#\$\%\^\&\(\)\=\+\[\]\{\}\|\;\"\'\‘\’\”\、\“\?\<\>\,\，\~\`]')
        if not regexp.search(urlStr):
            isurl = True
    else:
        if regex2.match(urlStr) != None:
            regexp = re.compile(u'[\u4e00-\u9fa5]|[\*\!\@\#\$\%\^\&\(\)\=\+\[\]\{\}\|\;\"\'\‘\’\”\、\“\?\<\>\,\，\~\`]')
            if not regexp.search(urlStr):
                isurl = True
    return isurl
