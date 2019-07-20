"""
    传入微博url，进行解析
    author:mmciel
    time：2019年2月9日21:07:39
"""
# -*- coding:utf-8 -*-
import json
import re
import requests

class download_yun(object):
    def __init__(self,url):
        """
        传入微博url，进行解析
        :param url: 传入分享链接
        :return: 解析后的链接
        """
        # get 请求
        weibo_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        weibo_r = requests.get(url, headers=weibo_headers)
        weibo_context = weibo_r.text

        # 获取媒体url
        self.download_url = ""
        # 由于资源来源不同，真实的资源来源地址在json中的key有所不同
        video_title = [
            r"\"mp4_hd_mp4\": \".*\"",
            r"\"mp4_ld_mp4\": \".*\"",
            r"\"stream_url_hd\": \".*\"",
            r"\"stream_url\": \".*\"",
        ]
        for str in video_title:
            weibo_pattern = re.compile(str)
            ok = weibo_pattern.findall(weibo_context)
            if len(ok) != 0:
                data = '{' + ok[0] + '}'
                data_dict = json.loads(data)
                for key in data_dict:
                    self.download_url = data_dict[key]
                    break

        # 获取标题
        weibo_pattern = re.compile(r"\"status_title\": \".*\"")
        ok = weibo_pattern.findall(weibo_context)
        data = '{' + ok[0] + '}'
        data_dict = json.loads(data)
        self.title = data_dict['status_title']
        # print (download_url,title)
    def get_response_text(self):
        return [self.title, self.download_url]



# get_download_url("https://m.weibo.cn/1700648435/4337883920131682")