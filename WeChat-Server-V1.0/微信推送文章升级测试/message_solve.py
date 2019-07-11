"""
    接收用户发送的数据，处理并打包返回xml
    filename：message_solve.py
    author：mmciel

"""
# -*- coding:utf-8 -*-
import time

import dict_solve
import ibot

# 文本信息回传模板：发送者；接收者；时间；内容
text_message_template = """
<xml>
    <ToUserName><![CDATA[{}]]></ToUserName>
    <FromUserName><![CDATA[{}]]></FromUserName>
    <CreateTime>{}</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[{}]]></Content>
</xml>
"""
# 从dict_solve中获取主菜单字符串
menu_template = dict_solve.main_menu

def text_solve(to_user,from_user,context):
    """

    :param to_user: 发送者
    :param from_user: 接收者
    :param context: 用户数据
    :return:xml回复包
    """
    # 调用ibot中的爬虫
    str = ibot.get_ibot_reply(to_user, context)
    # 构造回复包
    result = text_message_template.format(to_user, from_user, int(time.time() * 1000), str)

    return result
pass
