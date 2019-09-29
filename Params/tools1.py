# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:56
# @Author  : WangJuan
# @File    : tools.py

"""
读取yaml测试数据

"""

import yaml
import os
import os.path


def parse():
    #读取所有yml数据并用字典形式保存
    # path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params/Param/xiugai'
    #市局-稽查局-分局
    # path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params/工单分局转简易/xiugai'
    #工单分局转简易
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params/工单市局/xiugai'
    #工单市局流程
    for root, dirs, files in os.walk(path_ya):
        #os.walk获取路径、[]、文件名
        for name in files:
            #只获取文件
            watch_file_path = os.path.join(root, name)
            #将root路径+files文件名做拼接C:/Users/Lenovo/Desktop/接口文档/har2case/工单对接\login.yaml
            with open(watch_file_path, 'r', encoding='UTF-8') as f:
                page = yaml.safe_load(f)
                return page
    # return pages


if __name__ == '__main__':
    parse()
    # caselist("wwww")
