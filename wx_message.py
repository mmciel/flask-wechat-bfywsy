"""
 author:mmciel
 time:2019-7-12 09:45:15
 消息对象
"""
import re
import time

import message_dict


class user_mess_text(object):
    """
        用户发送的文本消息
        消息格式：
            ToUserName	    开发者微信号
            FromUserName	发送方帐号（一个OpenID）
            CreateTime	    消息创建时间 （整型）
            MsgType	        消息类型，文本为text
            Content	        文本消息内容
            MsgId	        消息id，64位整型
    """
    def __init__(self, ToUserName, FromUserName,
                 CreateTime, MsgType,
                 Context, MsgId):
        self.ToUserName = ToUserName
        self.FromUserName = FromUserName
        self.CreateTime = CreateTime
        self.MsgType = MsgType
        self.Context = Context
        self.MsgId = MsgId

    def parse(self):
        """
            文本消息解析
            带链接消息
            纯文本消息
            混合消息
        :return:
        """
        # 尝试取得链接
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        url = re.findall(url_pattern, self.Context)
        response_text = "没有明白你的意思呢~"
        # 含有链接
        if len(url) > 0:
            # 送入链接解析对象
            
            print(url)
        else:
            # 调用消息字典接口
            response_text = message_dict.message_link.get_value('self.Context')

        # 生成回复信息
        response_xml = self.create_response_xml(response_text)
        return response_xml

    def create_response_xml(self, context):

        text_template = """
        <xml>
            <ToUserName><![CDATA[{}]]></ToUserName>
            <FromUserName><![CDATA[{}]]></FromUserName>
            <CreateTime>{}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{}]]></Content>
        </xml>
        """
        response_xml = text_template.format(self.ToUserName, self.FromUserName, int(time.time() * 1000), context)
        return response_xml


class user_mess_img(object):
    """
        用户发送的图片消息
        消息格式：
            ToUserName	    开发者微信号
            FromUserName	发送方帐号（一个OpenID）
            CreateTime	    消息创建时间 （整型）
            MsgType	        消息类型，图片为image
            PicUrl	        图片链接（由系统生成）
            MediaId	        图片消息媒体id，可以调用获取临时素材接口拉取数据。
            MsgId	        消息id，64位整型
    """
    def __init__(self, ToUserName, FromUserName,
                 CreateTime, MsgType,
                 PicUrl, MediaId, MsgId):
        self.ToUserName = ToUserName
        self.FromUserName = FromUserName
        self.CreateTime = CreateTime
        self.MsgType = MsgType
        self.PicUrl = PicUrl
        self.MediaId = MediaId
        self.MsgId = MsgId

class user_mess_voice(object):
    """
        用户发送的语音消息
        消息格式：
            ToUserName	    开发者微信号
            FromUserName	发送方帐号（一个OpenID）
            CreateTime	    消息创建时间 （整型）
            MsgType	        语音为voice
            MediaId	        语音消息媒体id，可以调用获取临时素材接口拉取数据。
            Format	        语音格式，如amr，speex等
            MsgID	        消息id，64位整型
    """
    def __init__(self, ToUserName, FromUserName,
                 CreateTime, MsgType,
                 MediaId, Format, MsgId):
        self.ToUserName = ToUserName
        self.FromUserName = FromUserName
        self.CreateTime = CreateTime
        self.MsgType = MsgType
        self.Format = Format
        self.MediaId = MediaId
        self.MsgId = MsgId