"""
    传入网易云音乐url，进行解析
    author:mmciel
    time：2019年2月9日16:05:12
    time:2019-7-20 10:42:21重构
"""
# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

class download_yun(object):
    def __init__(self,url):
        # get请求
        yun_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', }
        yun_r = requests.get(url, headers=yun_headers)
        yun_r.encoding = "utf-8"
        # 获取标题
        bsObj = BeautifulSoup(yun_r.text, 'html.parser')
        # print(bsObj.title) 获得网页标题
        self.title = str(bsObj.title)
        title_pattern = re.compile(r'>.*<')
        title = re.findall(title_pattern, self.title)[0][1:-1]
        # print(url[0][1:-1]) 获得标题字符串
        # title = title
        # print(title)

        # 获取媒体链接
        music_num = re.compile(r"song/[0-9]{2,}").findall(url)[0][5:]
        yun_url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(music_num)
        self.download_url = requests.get(yun_url, headers=yun_headers).url

    def get_response_text(self):
        return [self.title, self.download_url]

#
#
# u = download_yun("http://music.163.com/song/1327456179/?userid=495697406").get_response_text()
# print(u)