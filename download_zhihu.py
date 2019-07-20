"""
    传入知乎url，返回解析url
    filename：zhihuD.py
    author:mmciel
    time：2019年2月9日16:05:12
"""
# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

class download_zhihu(object):
    def __init__(self,url):
        """
        传入知乎url，返回解析url
        :param url:传入的url
        :return: 解析后的url
        """
        # 发送get请求
        zhihu_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', }
        zhihu_r = requests.get(url, headers=zhihu_headers)
        zhihu_r.encoding = "utf-8"

        # 获取标题
        bsObj = BeautifulSoup(zhihu_r.text, 'html.parser')
        title = str(bsObj.title)
        title_pattern = re.compile(r'>.*<')
        title = re.findall(title_pattern, title)
        title = title[0][1:-1]

        # 获取媒体链接
        zhihu_pattern = re.compile(r"https://www.zhihu.com/video/[0-9]{10,}")
        video_lists = zhihu_pattern.findall(zhihu_r.text)
        video_list = []
        for i in video_lists:
            if i not in video_list:
                video_list.append(i)
        self.response_text = [title]
        zhihu_pattern2 = re.compile(r"[0-9]{10,}")
        # print(video_list)
        for item in video_list:
            ok = zhihu_pattern2.search(item)
            mp4_url = 'https://lens.zhihu.com/api/v4/videos/' + ok.group(0)
            rmp4 = requests.get(mp4_url, headers=zhihu_headers)
            km = dict(rmp4.json())
            download_url = km['playlist']['LD']['play_url']
            self.response_text.append(download_url)

        print(self.response_text)
    def get_response_text(self):
        return self.response_text
    pass

# download_zhihu('https://www.zhihu.com/question/304970889/answer/706296797').get_response_text()