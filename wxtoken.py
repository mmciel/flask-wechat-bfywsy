# -*- coding:utf-8 -*-

import hashlib
"""
    校验token
    author：mmciel
    time：2019年2月9日13:10:58
"""

def check_token(data):
    token = "mmciel"
    signature = data.get('signature', '')
    timestamp = data.get('timestamp', '')
    nonce = data.get('nonce', '')
    echostr = data.get('echostr', '')
    # 字典排序
    list = [token, timestamp, nonce]
    list.sort()
    s = list[0] + list[1] + list[2]
    # sha1加密算法
    hascode = hashlib.sha1(s.encode('utf-8')).hexdigest()
    # 如果是来自微信的请求，则回复echostr
    if hascode == signature:
        return echostr
    else:
        return ""