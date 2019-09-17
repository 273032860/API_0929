import os
from Params import tools1
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
"""
需求一体化查询统计类流程数据
"""
def get_parameter(name):
    #将tools封装成函数
    data = tools1.parse()
    param = data[name]["test"]["request"]
    return param

class Login():
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/login.yaml')
    params = get_parameter('账号登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]

class createtask():
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/createTask.yaml')
    params = get_parameter('创建发起流程')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class save1():
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/save1.yaml')
    params = get_parameter('环节1保存')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask1():
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/handleTask1.yaml')
    params = get_parameter('推送1')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

