"""
已经停用：此机器人太过智障！
调用青云客智能聊天机器人实现自动聊天
author：mmciel
time：2019年2月10日13:27:26
"""
# -*- coding:utf-8 -*-
import requests

def get_chat(data):
    """
    获取聊天结果
    :param data:传入的参数
    :return: 机器人的回复
    """
    url_temp = "http://api.qingyunke.com/api.php?key=free&appid=0&msg="
    headers_temp = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',}
    r_data = requests.get(url_temp + data, headers = headers_temp)
    print(r_data.text)
    r_dict = dict(r_data.json())
    # print(r_dict['content'])
    return r_dict['content']
# get_chat("你好")