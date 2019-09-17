import os
from Params import tools1
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
"""
日常检查简易流程数据
"""
def get_parameter(name):
    #将tools封装成函数
    data = tools1.parse()
    param = data[name]["test"]["request"]
    return param

class Login_00():
    params = get_parameter('吕桂芬登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]

class createtask_01():
    params = get_parameter('创建发起流程')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class save_02():
    params = get_parameter('环节1保存')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_03():
    params = get_parameter('推送1')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class Login_04():
    params = get_parameter('缪军登录')
    url = params["url"]
    data = params["data"]
    header = params["headers"]


class qianshou_05():
    params = get_parameter('缪军岗位签收')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class save_06():
    params = get_parameter('缪军录入信息保存')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handleTask_07():
    params = get_parameter('缪军环节2推送')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class biaogeshuju_08():
    params = get_parameter('缪军环节3读取')
    url = params["url"]
    data = params["params"]
    header = params["headers"]

class save_09():
    params = get_parameter('缪军环节3保存')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handletask_10():
    params = get_parameter('缪军环节3推送')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handletask_11():
    params = get_parameter('缪军环节4推送')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class handletask_12():
    params = get_parameter('缪军环节5推送')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class save_13():
    params = get_parameter('缪军归档保存')
    url = params["url"]
    data = params["json"]
    header = params["headers"]

class save_14():
    params = get_parameter('缪军归档页面保存')
    url = params["url"]
    data = params["json"]
    header = params["headers"]