#!user/bin/env python
# -*- coding: utf-8 -*-
' utils : 下载函数 '
import urllib2
'''此函数用于捕获异常、重试下载并设置代理用户'''
def download(url, user_agent='wswp', num_retries = 2):
    print 'Downloading: ', url
    headers = {'User_agent' : user_agent}
    request = urllib2.Request(url, headers = headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error: ', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <=600:
                return download(url, user_agent, num_retries-1)
    return html

if __name__ == '__main__':
    print download('http://tech.17lhd.com/')
