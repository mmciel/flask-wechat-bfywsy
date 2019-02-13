"""
处理回复规则相关数据
author：mmciel
time：2019年2月12日20:10:00

"""
# -*- codin:utf-8 -*-
import json

main_menu = """
【帮助：公众号使用帮助】\n
【内容：文章与教程导航】\n
【功能：公众号内置功能】\n
【资源：资源查看与下载】\n
"""
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
# 回复解释
reply_head = "可回复以下内容获取相关信息\n"
# json 工具字典
tools_dict = {}
# json 资源字典
# value1_dict
# value2_dict
# value3_dict
value1_dict = {}
value2_dict = {}
value3_dict = {}

def init_dict():
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
    # 读取文件并转化为字典
    f = open("value_file.json", encoding='utf-8')
    data = json.load(f)
    # 构造第一个字典（实际上是列表，作为下面字典的索引）
    temp_str = ""
    for temp in list(data.keys()):
        temp_str = temp_str + "【" + temp + "】" + '\n'
    main_menu_dict['资源'] = main_menu_dict['资源'] + temp_str
    # print(value1_dict)
    for key in data:
        # 构造第二层字典
        value1_dict[key] = list(data[key].keys())
        # print(value2_dict[key])
        for key2 in value1_dict[key]:
            # print(key,key2)
            # print(data[key][key2])

            temp_list = []
            for temp_dict in data[key][key2]:
                temp_list.append(temp_dict['name'])
                value3_dict[temp_dict['name']] = temp_dict['data']
            value2_dict[key2] = temp_list
        pass
    pass
# get_value_file()
# print(value1_dict)
# print(value2_dict)
# print(value3_dict)

def get_tool_file():
    # 读取文件并转化为字典
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
    1.读取json数据
    2.初始化字典
    3.判断是够含有这个字段，并返回结果
    :param text: 用户传过来的关键字
    :return: 返回字典中是否有此字段
    """
    init_dict()
    # 1 2
    get_tool_file()
    get_value_file()
    # 3
    keys_list = list(main_menu_dict.keys())+list(tools_dict.keys())+list(value1_dict.keys())+list(value2_dict.keys())+list(value3_dict.keys())
    # print(keys_list)
    return text in keys_list
    pass
# print(not_isempty("编程资源"))

def get_reply_menu(text):
    return main_menu_dict[text]
    pass


def get_reply_tools(text):
    return tools_dict[text]
    pass


def get_reply_value1(text):
    str = "可回复以下类别获取相应资源\n"
    temp = value1_dict[text]
    for i in temp:
        str = str + i + '\n'
    return str
    pass


def get_reply_value2(text):
    str = "此类别下有如下资源，回复资源名获取资源：\n"
    temp = value2_dict[text]
    for i in temp:
        str = str + i + '\n'
    return str
    pass


def get_reply_value3(text):
    return value3_dict[text]
    pass


def get_text(text):
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


