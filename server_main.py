"""
微信公众号后台（公众号：并非一无所有）
author:mmciel
final update time：2019年2月9日13:02:42
version：1.0
files:
    server_main:flask web、接收与发送用户xml数据、响应用户动作
    message_solve:分析xml数据（响应text、img、语音、视频信息）
    wxtoken:验证Tencent WeChat token
    zhihuD:解析知乎url链接中视频媒体地址并返回
    weiD:解析微博url链接中视频媒体地址并返回
    yunD:解析网易云音乐url链接中音乐媒体地址并返回
python3 package：
    Package        Version
    -------------- ----------
    beautifulsoup4 4.7.1
    Flask          1.0.2
    requests       2.21.0
    urllib3        1.24.1
github：
"""
# -*- coding:utf-8 -*-
from flask import Flask
from flask import request
import xml.etree.ElementTree as ET

import message_solve
import wxtoken

app = Flask(__name__)


@app.route('/wx', methods=['GET', 'POST'])
def wechat():
    """
    GET:token check
    POST: deal with user order
    """
    if request.method == 'GET':
        return wxtoken.check_token(request.args)
    elif request.method == 'POST':
        '''收集post data，根据用户发送的数据类型进行相应的响应'''
        # 解析xml数据
        xml = ET.fromstring(request.data)
        # 获取通用xml数据: 服务器username 用户username 数据类型
        to_user = xml.find('ToUserName').text
        from_user = xml.find('FromUserName').text
        msg_type = xml.find('MsgType').text
        # 数据类型判断
        if msg_type == 'text':
            # 文本消息
            '''
            [开发者文档：文本数据]
            参数	            描述
            ToUserName	    开发者微信号
            FromUserName	发送方帐号（一个OpenID）
            CreateTime	    消息创建时间 （整型）
            MsgType	        text
            Content	        文本消息内容
            MsgId	        消息id，64位整型
            '''
            context = xml.find('Content').text
            # 数据传入message_solve进行分析响应
            msg = message_solve.text_solve(from_user,to_user,context)

        else:
            pass
        message_solve.set_log(str(xml),str(msg))
        return msg
    pass
pass
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug = True)