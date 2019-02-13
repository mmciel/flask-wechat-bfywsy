"""
    接收用户发送的数据，处理并打包返回xml
    filename：message_solve.py
    author：mmciel
    time：2019年2月9日20:31:39
"""
# -*- coding:utf-8 -*-
import re
import time

import dict_solve
import ibot
import weiD
import zhihuD
import yunD

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

# 正则匹配模式串字典，用于匹配知乎串，微博串，云音乐串
pattern_dict = {
    'zhihu': r'https://www.zhihu.com/.*',
    'weibo': r'https://m.weibo.cn/.*',
    'yunmusic': r'http://music.163.com/.*',
    'none' : r'.*',
}

def subscribe_event(to_user,from_user):
    str = '欢迎关注mmciel的个人订阅号：\n并非一无所有\n'+'详细介绍请点击头像查看，回复以下关键词有惊喜~\n'+ menu_template
    result = text_message_template.format(to_user, from_user, int(time.time() * 1000), str)
    return result

def text_solve(to_user,from_user,context):
    """
    文本信息处理

    context是用户‘输入’的所有数据。通过对context的处理，可实现针对性的回复
    此解析当前分为两种：带链接的；不带链接的；
        带链接的：
            知乎下载；微博下砸；云音乐下载
        不带链接的：
            关键词处理
    """
    # 判断context是否含有链接
    # url = re.findall(pattern, string)
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    url = re.findall(url_pattern, context)

    # xml数据打包字符串
    result = ""
    # 含有链接
    if len(url) > 0:
        # 遍历字典，判断目前是否可解析这个链接
        for key in pattern_dict:
            temp_pattern = pattern_dict[key]
            # 匹配成功
            if len(re.findall(temp_pattern, url[0])) != 0:
                # 知乎
                if key == 'zhihu':
                    str = zhihuD.get_download_url(url[0])
                    str = "链接解析结果：" + str[0]+'\n'+str[1]
                    result = text_message_template.format(to_user, from_user, int(time.time() * 1000), str)
                    # print(result)
                    break;
                # 微博
                elif key == 'weibo':
                    str = weiD.get_download_url(url[0])
                    str = "链接解析结果：" + str[0] + '\n' + str[1]
                    result = text_message_template.format(to_user, from_user, int(time.time() * 1000), str)
                    break;
                # 云音乐
                elif key == 'yunmusic':
                    str = yunD.get_download_url(url[0])
                    str = "链接解析结果：" + str[0] + '\n' + str[1]
                    result = text_message_template.format(to_user, from_user, int(time.time() * 1000), str)
                    break;
            # 处理结尾（匹配失败）
            if key == 'none':
                result = text_message_template.format(to_user, from_user, int(time.time() * 1000), "链接暂时无法解析")
        pass
    # 不含链接
    else:
        """
            这里是处理指定消息回复的入口:
            处理思路：
            1. 构造关键字字典
                构造命令字典：例如帮助，内容，功能，资源等。
                构造数据字典：tool_file.json value_file.json中的字段提取
            2. 查询字典
                优先级：命令字典大于数据字典
            3.反馈
        """
        if dict_solve.not_isempty(context):
            str = dict_solve.get_text(context)
            result = text_message_template.format(to_user, from_user, int(time.time() * 1000), str)
            pass
        else:
            """调用聊天机器人敷衍用户"""
            str = ibot.get_ibot_reply(to_user,context)
            result = text_message_template.format(to_user, from_user, int(time.time() * 1000), str)
        pass
    return result
pass
# url = 'https://www.zhihu.com/question/46020782/answer/577812256'

def set_log(input,output):
    """公众号日志记录"""
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open('log.txt','a+',encoding="utf-8") as f:
        f.write("==========================================\n")
        f.write("time = "+timestr+"\n")
        f.write("input:\n")
        f.write(input)
        f.write("\noutput:\n")
        f.write(output)
        f.write("\n==========================================\n")