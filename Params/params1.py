# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午11:32
# @Author  : WangJuan
# @File    : datas.py

"""
定义所有测试数据

"""
import os
from Params import tools1
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    #将tools封装成函数
    data = tools1.parse()
    param = data[name]["test"]["request"]
    return param


class Login:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/login.yaml')
    params = get_parameter('账号登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]

class CreateTask:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/createTask.yaml')
    params = get_parameter('创建发起流程')
    url = params["url"]
    data = params["json"]
    header = params["headers"]










# class Basic:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Basic.yaml')
#     params = get_parameter('Basic')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])
#
#
# class Collections:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Collections.yaml')
#     params = get_parameter('Collections')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])
#
#
# class Personal:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Personal.yaml')
#     params = get_parameter('Personal')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])
#
#
# class Login:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Login.yaml')
#     params = get_parameter('Login')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])

if __name__ == '__main__':
    print(Login.header)