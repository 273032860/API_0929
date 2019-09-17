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
    # path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params/Param'
    # print(path_ya)
    # path_ya = "C:/Users/Lenovo/Desktop/接口文档/har2case/工单对接流程/接口数据"
    # path_ya = "C:/Users/Lenovo/Desktop/接口文档/har2case/需求一体化查询统计类征科流程/接口数据"
    # path_ya = "C:/Users/Lenovo/Desktop/接口文档/har2case/日常检查简易流程/接口数据"
    path_ya = "C:/Users/Lenovo/Desktop/接口文档/har2case/工单对接流程市局_稽查局_分局/抓包数据"
    # print(path_ya)
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        #os.walk获取路径、[]、文件名
        for name in files:
            #只获取文件
            watch_file_path = os.path.join(root, name)
            #将root路径+files文件名做拼接C:/Users/Lenovo/Desktop/接口文档/har2case/工单对接\login.yaml
            with open(watch_file_path, 'r', encoding='UTF-8') as f:
                page = yaml.safe_load(f)
                jkname = page[0]["config"]
                # print(jkname)
                jkdata = page[1:]
                # print(jkdata)
                pages[jkname]=jkdata
    # print(pages["lgo"])
    # for n in pages["wwww"]:
    #     print(n.keys())
    # print(page)
    # print(pages)
    return pages

# def caselist(yaml):
#     data = parse()
#     keylist=[]
#     for n in data[yaml]:
#         # list.append(n.keys())
#         # print(list(n.keys()))
#         keylist.extend(list(n.keys()))
#     print(keylist)


if __name__ == '__main__':
    # parse()
    caselist("wwww")
