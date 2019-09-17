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
                pages[jkname]=jkdata[0]
                # print(page)
    return pages

    # pages = {}
    # for root, dirs, files in os.walk(path_ya):
    #     for name in files:
    #         watch_file_path = os.path.join(root, name)
    #         with open(watch_file_path, 'r',encoding='UTF-8') as f:
    #             page = yaml.safe_load(f)
    #             pages.update(page)
    #     print(pages)


# class GetPages:
#     @staticmethod
#     def get_page_list():
#         #抽掉dec、parameters 将数据打包成接口名[value]的字典数据
#         _page_list = {}
#         pages = parse()
#         for page, value in pages.items():
#             parameters = value['parameters']
#             data_list = []
#             for parameter in parameters:
#                 data_list.append(parameter)
#             _page_list[page] = data_list
#
#         return _page_list


if __name__ == '__main__':
    parse()
