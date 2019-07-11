"""
测试脚本，无用
实现个微信机器人练练手，采用图灵机器人api，此脚本实现转发功能
author：mmciel
2019年2月9日13:05:07
version：#
"""
# -*- coding:utf-8 -*-
from flask import Flask
from flask import request
import hashlib
import requests
import json
import time
import re
import xml.etree.ElementTree as ET


app = Flask(__name__)
app.debug = True


@app.route('/wx', methods=['GET', 'POST'])
def wechat():
    if request.method == 'GET':
        token = 'mmciel'
        # 获取输入参数
        data = request.args
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
    else:
        # 解析xml
        xml = ET.fromstring(request.data)
        toUser = xml.find('ToUserName').text
        fromUser = xml.find('FromUserName').text
        msgType = xml.find("MsgType").text
        createTime = xml.find("CreateTime")
        # 判断类型并回复
        if msgType == "text":
            content = xml.find('Content').text
            return reply_text(fromUser, toUser, reply(fromUser, content))
        else:
            return reply_text(fromUser, toUser, "000")

def reply_text(to_user, from_user, content):
    """
    以文本类型的方式回复请求
    """
    return """
        <xml>
            <ToUserName><![CDATA[{}]]></ToUserName>
            <FromUserName><![CDATA[{}]]></FromUserName>
            <CreateTime>{}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{}]]></Content>
        </xml>
        """.format(to_user, from_user, int(time.time() * 1000), content)

def reply(openid, msg):
    '''
    使用图灵机器人
    '''
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '453b2da4ec4f4bec947fda36f6e1eedf',
        'info': msg,
        'userid': openid,
    }
    r = requests.post(api_url, data=data).json()
    print(r.get('text'))
    return r.get('text')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)