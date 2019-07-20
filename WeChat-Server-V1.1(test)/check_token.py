"""
    校验token
    author：mmciel
    time：2019年2月9日13:10:58
    update time:2019-7-12 09:40:59
"""
# -*- coding:utf-8 -*-
import hashlib


def get_result(data):
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
    list_data = [token, timestamp, nonce]
    list_data.sort()
    s = list_data[0] + list_data[1] + list_data[2]

    # sha1加密算法
    hash_code = hashlib.sha1(s.encode('utf-8')).hexdigest()

    # 如果是来自微信的请求，则回复echostr
    if hash_code == signature:
        return echostr
    else:
        return ""