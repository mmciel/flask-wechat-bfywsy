"""
    author:mmciel
    create time: 2019-7-12 09:31:55
    Version: V1.4
    update:
        后台重构
"""

from flask import Flask
from flask import request
import xml.etree.ElementInclude as ET

import check_token
from wx_message import user_mess_img
from wx_message import user_mess_text
from wx_message import user_mess_voice

app = Flask(__name__)


@app.route('/wx', method=['GET','POST'])
def wechat():
    """
    get: token校验
    post：消息处理
    :return:
    """

    # 如果是get请求
    if request.method == "GET":
        # 返回校验结果
        return check_token.get_result(request.args)
    elif request.method == "POST":
        # 对请求包进行xml解析
        xml_message_data = ET.fromstring(request.data)
        # 获取消息类型
        message_type = xml_message_data.find('MsgType').text

        # 判断消息类型并处理
        if message_type == 'text':
            # 文本消息

            # 创建文本消息对象
            message = user_mess_text(
                xml_message_data.find('ToUserName').text,
                xml_message_data.find('FromUserName').text,
                xml_message_data.find('CreateTime').text,
                xml_message_data.find('MsgType').text,
                xml_message_data.find('Context').text,
                xml_message_data.find('MsgId').text
            )
            # 解析文本消息对象


        # elif message_type == 'event':
        #     # 事件响应类型
        # pass
        # elif message_type == 'image'：
        #     # 图片类型
        # pass
        # elif message_type == 'voice':
        #     # 语音类型
        # pass
        # else：
        #     # 其他类型
        # pass


# 启动~
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80,debug = True)