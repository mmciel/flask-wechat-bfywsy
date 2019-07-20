"""
 author:mmciel
 time:2019-7-12 09:45:15
 消息对象
"""
import re
import time

import download_zhihu
import download_yun
import download_weibo
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
        self.ToUserName = FromUserName
        self.FromUserName = ToUserName
        self.CreateTime = CreateTime
        self.MsgType = MsgType
        self.Context = Context
        self.MsgId = MsgId
        self.text_template = """
        <xml>
            <ToUserName><![CDATA[{}]]></ToUserName>
            <FromUserName><![CDATA[{}]]></FromUserName>
            <CreateTime>{}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{}]]></Content>
        </xml>
        """

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
        response_text = "没有明白您的意思呢~"
        # 含有链接
        if len(url) > 0:
            # 送入链接解析对象
            response_xml = self.parsing_url(url)
            # print(url)
            return [response_xml]
        else:
            # 调用消息字典接口
            response_text = message_dict.link_massage.get_value(self.Context)
            # 生成回复信息
            response_xml = self.create_response_xml(response_text)
            return response_xml

        

    def create_response_xml(self, context):

        temp_xml = self.text_template.format(self.ToUserName, self.FromUserName, int(time.time() * 1000), context)

        # 返回一个列表，为了同步多链接现象
        response_xml = [temp_xml]
        return response_xml

    def parsing_url(self,url):
        """
        链接解析工具
        :param url:链接
        :param to_user:发送者
        :param from_user:接受者
        :return:打包好的xml数据 含已经解析的链接
        """
        result = []
        pattern_dict = {
            'zhihu': r'https://www.zhihu.com/.*',
            'weibo': r'https://m.weibo.cn/.*',
            'yunmusic': r'http://music.163.com/.*',
            'none': r'.*',
        }
        response_text = []
        # 遍历字典，判断目前是否可解析这个链接
        for key in pattern_dict:
            temp_pattern = pattern_dict[key]
            # 匹配成功
            if len(re.findall(temp_pattern, url[0])) != 0:
                # 知乎
                if key == 'zhihu':
                    response_text = download_zhihu.download_zhihu(url[0]).get_response_text()

                    break
                # 微博
                elif key == 'weibo':
                    response_text = download_weibo.download_weibo(url[0]).get_response_text()

                    break
                # 云音乐
                elif key == 'yunmusic':
                    response_text = download_yun.download_yun(url[0]).get_response_text()
                    break
            # 处理结尾（匹配失败）
            if key == 'none':
                response_text = ["对不起，链接暂时无法解析"]
        items = ""
        for item in response_text:
            items = items + '\n\n'+ item
            # temp_xml = self.text_template.format(self.ToUserName, self.FromUserName, int(time.time() * 1000), item)
            # result.append(temp_xml)

        temp_xml = self.text_template.format(self.ToUserName, self.FromUserName, int(time.time() * 1000),items)
        # result[0] = temp_xml
        return temp_xml

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