"""
                                           _oo0oo_
                                          o8888888o
                                          88" . "88
                                          (| -_- |)
                                          0\  =  /0
                                        ___/`---'\___
                                      .' \\|     |// '.
                                     / \\|||  :  |||// \
                                    / _||||| -:- |||||- \
                                   |   | \\\  -  /// |   |
                                   | \_|  ''\---/''  |_/ |
                                   \  .-\__  '-'  ___/-. /
                                 ___'. .'  /--.--\  `. .'___
                              ."" '<  `.___\_<|>_/___.' >' "".
                             | | :  `- \`.;`\ _ /`;.`/ - ` : | |
                             \  \ `_.   \_ __\ /__ _/   .-` /  /
                         =====`-.____`.___ \_____/___.-`___.-'=====
                                           `=---='


                         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                   佛祖保佑         永无BUG
"""
"""
微信公众号后台（公众号：并非一无所有）
                            
author:mmciel

final update time：2019年2月13日20:58:45

version:1.3

update：添加完整的关键字回复规则（未处理关于文章的关键字：内容）
update:增加机器人聊天功能
update:增加日志记录功能

files:
    value_file.json     “素材”的json数据包
    tool_file.json      “功能”的json数据包
    dict_solve:         处理关键字回复规则
    ibot：               xiaoi机器人爬虫实现消息回复
    server_main:        flask web、接收与发送用户xml数据、响应用户动作
    message_solve:      分析xml数据（响应text、img、语音、视频信息）
    wxtoken:            验证Tencent WeChat token
    zhihuD:             解析知乎url链接中视频媒体地址并返回
    weiD:               解析微博url链接中视频媒体地址并返回
    yunD:               解析网易云音乐url链接中音乐媒体地址并返回
    
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

            # 用户聊天记录写入日志
            message_solve.set_log(str(request.data.decode()), str(msg))
            return msg
        elif msg_type == 'event':# 事件响应类型
            event = xml.find('Event').text

            # 关注公众号事件
            if event == 'subscribe':
                msg = message_solve.subscribe_event(from_user, to_user)
                return msg
            # 取消关注微信公众号，先不做处理
            elif event== 'unsubscribe':
                # 这里是个bug，本来的接口大多用于处理数据库的，懒得写
                pass
        else:
            # 其他类型先空着，想写再写
            pass
    pass
pass

# 启动~
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug = True)


'''
[开发者文档：接收数据；文本数据]
参数	            描述
ToUserName	    开发者微信号
FromUserName	发送方帐号（一个OpenID）
CreateTime	    消息创建时间 （整型）
MsgType	        text
Content	        文本消息内容
MsgId	        消息id，64位整型
'''