"""
    传入知乎url，进行解析
    filename：zhihuD.py
    author:mmciel
    time：2019年2月9日16:05:12
"""
# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup


def get_download_url(url):
    zhihu_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',}
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
    ok = zhihu_pattern.search(zhihu_r.text)
    line2 = ok.group(0)
    zhihu_pattern2 = re.compile(r"[0-9]{10,}")
    ok = zhihu_pattern2.search(line2)
    mp4_url = 'https://lens.zhihu.com/api/v4/videos/' + ok.group(0)
    rmp4 = requests.get(mp4_url, headers=zhihu_headers)
    km = dict(rmp4.json())
    download_url = km['playlist']['LD']['play_url']
    return [title,download_url]
pass

# get_download_url('https://www.zhihu.com/question/46020782/answer/577812256')