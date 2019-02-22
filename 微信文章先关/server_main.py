"""
                                           _oo0oo_
                                          o8888888o
                                          88" . "88
                                          (| -_- |)
                                          0\  =  /0
                                        ___/`---'\___
                                      .' \\|     |// '.
                                     / \\|||  :  |||// \
                                    / _||||| -:- |||||- \
                                   |   | \\\  -  /// |   |
                                   | \_|  ''\---/''  |_/ |
                                   \  .-\__  '-'  ___/-. /
                                 ___'. .'  /--.--\  `. .'___
                              ."" '<  `.___\_<|>_/___.' >' "".
                             | | :  `- \`.;`\ _ /`;.`/ - ` : | |
                             \  \ `_.   \_ __\ /__ _/   .-` /  /
                         =====`-.____`.___ \_____/___.-`___.-'=====
                                           `=---='


                         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                   佛祖保佑         永无BUG
"""
"""
微信公众号后台（公众号：并非一无所有）                         
author:mmciel
final update time：2019年2月13日20:58:45
version:
files:
    server_main:        flask web、接收与发送用户xml数据、响应用户动作
    wxtoken:            验证Tencent WeChat token

github：https://github.com/mmciel/flask-wechat-bfywsy.git
"""
# -*- coding:utf-8 -*-
from flask import Flask
from flask import request

import wxtoken

app = Flask(__name__)


@app.route('/wx', methods=['GET', 'POST'])
def wechat():
    """
    GET:用于进行token校验
    POST：与用户的信息交互
    :return:
    """
    if request.method == 'GET':
        return wxtoken.check_token(request.args)
    elif request.method == 'POST':
        pass
    pass
pass

# 启动~
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug = True)
