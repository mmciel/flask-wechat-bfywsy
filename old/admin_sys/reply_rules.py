
"""
设置公众号主菜单
author：mmciel
time：2019年2月11日21:25:54

"""
# -*- coding:utf-8 -*-
import json

import requests
from urllib import request

def set_menu():
    '''设置菜单'''
    # 初始化微信提供的必要参数
    appid = "wx090c2fcb5db15ac2"
    secret = "6f107548a662bbf823c6b6b90d6c9269"
    get_access_token_url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + secret

    # 发起请求，获得数据包
    token_data_temp = request.urlopen(get_access_token_url)
    # print(token_data_temp.read())
    # bytes转string
    r_token_data = token_data_temp.read().decode()
    # 提取access_token
    access_token = json.loads(r_token_data)['access_token']
    set_url = "https://api.weixin.qq.com/cgi-bin/get_current_autoreply_info?access_token=" + access_token
    r_set = request.urlopen(set_url)
    print(r_set.read())
    pass

if __name__ == "__main__":
    set_menu()