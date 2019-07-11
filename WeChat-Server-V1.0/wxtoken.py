"""
    校验token
    author：mmciel
    time：2019年2月9日13:10:58
"""
# -*- coding:utf-8 -*-

import hashlib


def check_token(data):
    """
    token校验
    :param data:传入 数据包
    :return: 返回指定算法生成的字符串到微信公众号平台进行比对
    """
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
    # 否则回复个无效的
    if hascode == signature:
        return echostr
    else:
        return ""