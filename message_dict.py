"""
    author:mmciel
    time:2019-7-16 18:10:48
    连接到数据库 messagedict 获取消息回复字典
"""

import pymysql


class message_dict(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='bfywsy')
        self.cursor = self.conn.cursor()

    def get_value(self, kkey):
        sql = 'select * from messagedict where (kkey = "%s")' % kkey
        self.cursor.execute(sql)
        print(self.cursor)
        for d in self.cursor:
            print(d)
        return self.cursor


d = message_dict()
d.get_value('你好')
