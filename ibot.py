"""
爬虫实现XiaoI聊天机器人
author：mmciel
time：2019-2-10 17:59:10
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
        "sessionId":"4e9dc926d163470eb99b33ad1a18c6d9",
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

    # 用户名进行MD5加密
    user = hashlib.md5(user.encode(encoding='UTF-8')).hexdigest()

    # 用户名填入json数据包
    json_data["userId"] = user
    # 聊天数据填入json数据包
    json_data["body"]["content"] = data
    # 生成json串
    json_data = json.dumps(json_data)
    # url code 处理 json串
    json_data = quote(json_data)
    # 处理时间戳
    timeStamp = int(time.time()*1000)
    # 构造get请求地址
    url = api_url+parameter_str1+parameter_str2+json_data+parameter_str3+str(timeStamp)
    r = requests.get(url, headers=utl_headers)

    # 返回数据分析：   print(r.text)
    '''
    __webrobot_processMsg({"robotId":"webbot","userId":"3de9483d302449cc8ace19a5b11a7c5b","sessionId":"b768443a92e7460a876900638396c59d","type":"openresp","body":{"status":1}});__webrobot_processMsg({"robotId":"webbot","userId":"3de9483d302449cc8ace19a5b11a7c5b","sessionId":"b768443a92e7460a876900638396c59d","type":"updaterobot","body":{"displayName":"小i机器人"}});__webrobot_processMsg({"robotId":"webbot","userId":"3de9483d302449cc8ace19a5b11a7c5b","sessionId":"b768443a92e7460a876900638396c59d","type":"ex","body":{"name":"initconfig","data":{"homeP4Path":"home/index.html","inputPrompt":"请在这里输入您的消息","helpP4Path":"http://www.xiaoi.com","messageDateFormat":"HH:mm:ss","speechAddr":"","dn":"小i机器人","speechEnabled":"false"}}});__webrobot_processMsg({"robotId":"webbot","userId":"3de9483d302449cc8ace19a5b11a7c5b","sessionId":"b768443a92e7460a876900638396c59d","type":"txt","body":{"fontStyle":0,"fontColor":0,"content":"Hi，我是小i机器人，我可以查天气，讲笑话，订机票哦~ 除此之外还有几十项实用好玩的功能哦~ 快来试试吧\n\r\n","emoticons":{}}});__webrobot_processMsg({"robotId":"webbot","userId":"3de9483d302449cc8ace19a5b11a7c5b","sessionId":"b768443a92e7460a876900638396c59d","type":"txt","body":{"fontStyle":0,"fontColor":0,"content":"你好，我是小i机器人，很高兴认识你。\r\n","emoticons":{}}});

    - 提取json数据并分析：json太多，太慢
    - 正则提取字段（√）
    '''
    reply_pattern = re.compile(r"\"content\": \".*\"")
    ok = reply_pattern.findall(r.text)
    if len(ok) != 0:
        data = '{' + ok[0] + '}'
        data_dict = json.loads(data)
    else:







pass
get_ibot_reply("123","你好")

