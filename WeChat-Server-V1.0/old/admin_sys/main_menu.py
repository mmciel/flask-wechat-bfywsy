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
    set_url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + access_token
    menu_data = get_menu_data()
    r_set = request.urlopen(set_url,menu_data.encode('utf-8'))
    print(r_set.read())
    pass


def get_menu_data():
    '''构造菜单数据包'''
    str = '''
{
    "button": [
        {
            "name": "扫码", 
            "sub_button": [
                {
                    "type": "scancode_waitmsg", 
                    "name": "扫码带提示", 
                    "key": "rselfmenu_0_0", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "scancode_push", 
                    "name": "扫码推事件", 
                    "key": "rselfmenu_0_1", 
                    "sub_button": [ ]
                }
            ]
        }, 
        {
            "name": "发图", 
            "sub_button": [
                {
                    "type": "pic_sysphoto", 
                    "name": "系统拍照发图", 
                    "key": "rselfmenu_1_0", 
                   "sub_button": [ ]
                 }, 
                {
                    "type": "pic_photo_or_album", 
                    "name": "拍照或者相册发图", 
                    "key": "rselfmenu_1_1", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "pic_weixin", 
                    "name": "微信相册发图", 
                    "key": "rselfmenu_1_2", 
                    "sub_button": [ ]
                }
            ]
        }
    ]
}    
'''
    return str

    pass
if __name__ == "__main__":
    set_menu()