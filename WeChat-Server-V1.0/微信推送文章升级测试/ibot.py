"""
爬虫实现XiaoI聊天机器人
author：mmciel
filename:ibot.py
"""
# -*- coding:utf-8 -*-
import json
import time
import requests
import hashlib
import re
from urllib.parse import quote

def get_ibot_reply(user,data):
    """
    转发用户聊天记录，回传机器人聊天结果
    :param user: 用户名加密串
    :param data: 用户发送过来的字符串
    :return:回复字符串
    """

    # 构造请求
    api_url = 'http://i.xiaoi.com/robot/webrobot?'
    utl_headers = {
        "Accept - Encoding": "gzip, deflate",
        "Connection": "keep - alive",
        "Host": "i.xiaoi.com",
        "Referer": "http: // i.xiaoi.com /",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }
    # 构造json数据包
    json_data ={
        "sessionId":"4e9dc926d163470eb99b33ad1a18c6d9",# 需要填充
        "robotId":"webbot",
        "userId":"c20ad4d76fe97759aa27a0c99bff6710",# 需要填充
        "body":{
            "content":"none"# 需要填充
        },
        "type":"txt"
    }
    # 静态参数字符串
    parameter_str1 = "&callback=__webrobot_processMsg"
    parameter_str2 = "&data="
    parameter_str3 = "&ts="

    # 处理时间戳
    timeStamp = str(int(time.time() * 1000))

    # 用户名进行MD5加密
    user = hashlib.md5(user.encode(encoding='UTF-8')).hexdigest()

    # 通过时间戳构造出sessionId 就这么敷衍下
    sessionId = hashlib.md5(timeStamp.encode(encoding='UTF-8')).hexdigest()

    # 用户名填入json数据包
    json_data["userId"] = user

    # 填充sessionId
    json_data["sessionId"] = sessionId

    # 聊天数据填入json数据包
    json_data["body"]["content"] = data

    # 生成json串
    json_data = json.dumps(json_data)

    # url code 处理 json串
    json_data = quote(json_data)

    # 构造get请求地址
    url = api_url+parameter_str1+parameter_str2+json_data+parameter_str3+str(timeStamp)
    r = requests.get(url, headers=utl_headers)

    reply_pattern = re.compile(r"__webrobot_processMsg\(.*?\)")
    ok = reply_pattern.findall(r.text)

    len_ok = len(ok)-1
    if len(ok)>0:
        data5_pattern = re.compile(r"\"content\":\".*?\"")
        ok = data5_pattern.findall(ok[len_ok])
        reply_data = ok[0][11:-1]

        reply_data = reply_data.replace("\\"+"r","").replace("\\n","\n").replace("\\u","")

    else:# 没查到数据
         reply_data = "听不懂呢···,不过我会一直努力学习的。"# 继续敷衍

    # 处理语料：详情请看右侧页面
    reply_data.replace("详情请看右侧页面","你应该知道的对吧~")# 疯狂敷衍
    return reply_data
pass

