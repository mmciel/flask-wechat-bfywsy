"""
    传入微博url，进行解析
    filename：weiD.py
    author:mmciel
    time：2019年2月9日16:05:12
"""
# -*- coding:utf-8 -*-
import json
import re
import requests

def get_download_url(url):
    weibo_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    weibo_r = requests.get(url,headers = weibo_headers)
    weibo_context = weibo_r.text
    # 获取媒体url
    weibo_pattern = re.compile(r"\"mp4_hd_mp4\": \".*\"")
    ok = weibo_pattern.findall(weibo_context)
    data = '{' + ok[0] + '}'
    data_dict = json.loads(data)
    download_url = data_dict['mp4_hd_mp4']
    # 获取标题
    weibo_pattern = re.compile(r"\"status_title\": \".*\"")
    ok = weibo_pattern.findall(weibo_context)
    data = '{' + ok[0] + '}'
    data_dict = json.loads(data)
    title = data_dict['status_title']
    return [title,download_url]
pass