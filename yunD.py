"""
    传入网易云音乐url，进行解析
    filename：yunD.py
    author:mmciel
    time：2019年2月9日16:05:12
"""
# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

"""
    author:mmciel
    time:2019年2月9日19:27:15
"""

def get_download_url(url):
    yun_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',}
    yun_r = requests.get(url, headers=yun_headers)
    yun_r.encoding = "utf-8"
    # 获取标题
    bsObj = BeautifulSoup(yun_r.text, 'html.parser')
    # print(bsObj.title) 获得网页标题
    title = str(bsObj.title)
    title_pattern = re.compile(r'>.*<')
    title = re.findall(title_pattern, title)
    # print(url[0][1:-1]) 获得标题字符串
    title = title[0][1:-1]
    # print(title)
    #获取媒体链接
    yun_pattern = re.compile(r"song/[0-9]{2,}")
    ok = yun_pattern.findall(url)
    data = ok[0]
    music_num = data[5:]
    yun_url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(music_num)
    yun_r = requests.get(yun_url, headers=yun_headers)
    download_url = yun_r.url
    return [title,download_url]
pass
