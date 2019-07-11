"""
处理回复规则相关数据
author：mmciel
time：2019年2月13日21:44:05

"""
# -*- coding:utf-8 -*-
import json


# 用户关注后发这个
main_menu = """
【帮助】：公众号使用帮助\n
【内容】：文章与教程导航\n
【功能】：公众号内置功能\n
【资源】：资源查看与下载\n
"""

# 帮助
help_menu_str = """
emmm。。。\n
回复【内容】，可查看本公众号的各类文章、教程、博客等，具体由文章前面“【】”的标识决定。（例如回复：【python】，即可获得此系列文章）\n
回复【功能】，可查看本公众号实现的所有小功能，再次回复相应功能名称，即可查看功能使用方式。\n
回复【资源】，可查看本公众号所收集的所有资源，根据相应分类，即可查看相应资源。（例如依次回复：编程资源  python，即可查看python所有的资源列表)\n
"""

# 菜单命令字典
main_menu_dict = {
    "帮助": help_menu_str,
    "内容": "emmm, >_< 我太菜了,还没有实现这个功能,可以点击头像查看所有文章~\n",# "内容": "回复以下关键字获取相应类别：\n",
    "功能": "回复以下关键字展示相应功能：\n",
    "资源": "回复以下关键字获得相应资源：\n"
}

# 这个忘了是干啥的了。。。先留着
reply_head = "可回复以下内容获取相关信息\n"
# 功能字典
tools_dict = {}

# 资源.json文件内的三层字典
value1_dict = {}
value2_dict = {}
value3_dict = {}

def init_dict():
    """
    清空下面的字典（叫初始化比较好）
    :return:
    """
    global  main_menu_dict
    global tools_dict
    global value1_dict
    global value2_dict
    global value3_dict
    main_menu_dict = {
        "帮助": help_menu_str,
        "内容": "emmm, >_< 我太菜了,还没有实现这个功能,可以点击头像查看所有文章~\n",  # "内容": "回复以下关键字获取相应类别：\n",
        "功能": "回复以下关键字展示相应功能：\n",
        "资源": "回复以下关键字获得相应资源：\n"
    }
    tools_dict = {}
    value1_dict = {}
    value2_dict = {}
    value3_dict = {}

def get_value_file():
    """
    读取文件并转化为字典
    :return:
    """
    f = open("value_file.json", encoding='utf-8')
    data = json.load(f)
    # 构造菜单字典中的资源键（作为下面字典的索引）
    temp_str = ""
    for temp in list(data.keys()):
        temp_str = temp_str + "【" + temp + "】" + '\n'
    main_menu_dict['资源'] = main_menu_dict['资源'] + temp_str
    # print(value1_dict)

    # 嘤嘤嘤，这里写N^3复杂度的算法真得好羞耻
    # 下次就把这个三层循环优化掉 flaging！！！
    for key in data:
        value1_dict[key] = list(data[key].keys())# 构造第1层字典
        for key2 in value1_dict[key]:
            temp_list = []
            for temp_dict in data[key][key2]:
                temp_list.append(temp_dict['name'])
                value3_dict[temp_dict['name']] = temp_dict['data']# 构造第3层字典
            value2_dict[key2] = temp_list# 构造第2层字典
        pass
    pass


def get_tool_file():
    """
    读取文件并转化为字典
    :return:
    """
    f = open("tool_file.json", encoding='utf-8')
    data = json.load(f)
    for key in data:
        tools_dict[data[key]["name"]] = data[key]["data"]
        pass
    temp_str = ""
    for temp in list(tools_dict.keys()):
        temp_str = temp_str + "【" + temp + "】" + "=>>" +tools_dict[temp] + '\n'
    main_menu_dict['功能'] = main_menu_dict['功能'] + temp_str
    # print(main_menu_dict['功能'])
    pass



def not_isempty(text):
    """
    判断是否文本是否属于以上字典的key
    :param text: 用户传过来的关键字
    :return: 返回字典中是否有此字段
    """
    # 这里有极其严重的效率问题，以后改。
    # 清空字典
    init_dict()
    # 重新从json文件导入字典
    get_tool_file()
    get_value_file()
    # 所有字典的key构造一个列表，并检查text是否在里面
    keys_list = list(main_menu_dict.keys())+list(tools_dict.keys())+list(value1_dict.keys())+list(value2_dict.keys())+list(value3_dict.keys())
    # print(keys_list)
    return text in keys_list
    pass
# print(not_isempty("编程资源"))

def get_reply_menu(text):
    """
    返回value
    :param text:
    :return:
    """
    return main_menu_dict[text]
    pass


def get_reply_tools(text):
    """
    返回value
    :param text:
    :return:
    """
    return tools_dict[text]
    pass


def get_reply_value1(text):
    """
    处理前缀，列表累加成字符串
    :param text:
    :return:
    """
    str = "可回复以下类别获取相应资源\n"
    temp = value1_dict[text]
    for i in temp:
        str = str + "【" + i + "】" + '\n'
    return str
    pass


def get_reply_value2(text):
    """
    处理前缀，列表累加成字符串
    :param text:
    :return:
    """
    str = "此类别下有如下资源，回复资源名获取资源：\n"
    temp = value2_dict[text]
    for i in temp:
        str = str + "【" + i + "】" + '\n'
    return str
    pass


def get_reply_value3(text):
    """
    返回value
    :param text:
    :return:
    """
    return value3_dict[text]
    pass


def get_text(text):
    """
    在所有的字典中查一遍key 并通过相应函数处理形成字符串
    :param text: 用户的输入
    :return: 处理成的字符串
    """
    # print(main_menu_dict)
    # print(tools_dict)
    # print(value1_dict)
    # print(value2_dict)
    # print(value3_dict)
    # print(text)
    if text in main_menu_dict.keys():
        reply_text = get_reply_menu(text)
        # print(reply_text)
    elif text in tools_dict.keys():
        reply_text = get_reply_tools(text)
        # print(reply_text)
    elif text in value1_dict.keys():
        reply_text = get_reply_value1(text)
        # print(reply_text)
    elif text in value2_dict.keys():
        reply_text = get_reply_value2(text)
        # print(reply_text)
    elif text in value3_dict.keys():
        reply_text = get_reply_value3(text)
        # print(reply_text)
    return reply_text
    pass
# not_isempty('')
# print(get_text('资源'))
#
# print(get_text('内容'))


