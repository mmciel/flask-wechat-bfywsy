"""
闲的没事，看看写了多少行代码
"""

# -*- coding:utf-8 -*-
import os

class Line(object):

    def __init__(self,path):
        self.path = path

    def get_lines(self):
        file_list = os.listdir(self.path)
        os.chdir(self.path)
        sum = 0
        for file in file_list:
            if file.endswith('.py'):
                count = 0
                lines = open(file, encoding='utf-8').readlines()
                for line in lines:
                    if line == '\n':
                        continue
                    else:
                        count += 1
                sum += count
                print('%s 有 %d 行' %(file,count))
        print('总行数: %d' %sum)

if __name__ == '__main__':
    line = Line('D:\PublicCode\PycharmWorkspace\wechat-python-server')
    line.get_lines()