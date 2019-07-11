"""
微信公众号后台（公众号：并非一无所有）
                            
author:mmciel

files:


    ibot：               xiaoi机器人爬虫实现消息回复
    server_main:        flask web、接收与发送用户xml数据、响应用户动作
    message_solve:      分析xml数据（响应text、img、语音、视频信息）
    wxtoken:            验证Tencent WeChat token
    
github：https://github.com/mmciel/flask-wechat-bfywsy.git
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
    GET:用于进行token校验
    POST：与用户的信息交互
    :return:
    """
    if request.method == 'GET':
        return wxtoken.check_token(request.args)
    elif request.method == 'POST':
        # xml解析request.data，进行用户交互

        # 解析xml数据
        xml = ET.fromstring(request.data)

        # 获取通用xml数据: 服务器username 用户username 数据类型
        to_user = xml.find('ToUserName').text
        from_user = xml.find('FromUserName').text
        msg_type = xml.find('MsgType').text

        # 数据类型判断
        if msg_type == 'text':# 文本消息
            # context得到的是文本消息中的文本
            context = xml.find('Content').text

            # 数据传入message_solve进行分析响应
            msg = message_solve.text_solve(from_user, to_user, context)

            # 通过return可直接把xml回复包返回给微信，用户将看到了回复包中的text
            return msg
    pass
pass

# 启动~
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug = True)
