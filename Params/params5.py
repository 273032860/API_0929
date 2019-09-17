import os
from Params import tools1
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
"""
工单对接流程数据
"""
def get_parameter(name,case):
    #将数据封装成只剩data、headers、url数据，传参yaml名，case名
    data = tools1.parse()
    # print(data)
    param = data[name][0][case]["request"]
    # print(param)
    return param

def caselist(yaml):
    #获取整理完的数据接口名，传yaml名
    data = tools1.parse()
    keylist=[]
    for n in data[yaml]:
        # list.append(n.keys())
        # print(list(n.keys()))
        keylist.extend(list(n.keys()))
    print(keylist)
    return keylist


def login1(case):
    params = get_parameter("lgo",case)
    url = params["url"]
    data = params["data"]
    header = params["headers"]
    return url,data,header

class casedata():
    #封装接口数据，传case名
    def __init__(self,case1):
        params = get_parameter("wwww",case1)
        self.url = params["url"]
        self.data = params["json"]
        self.header = params["headers"]

if __name__ == '__main__':
    login1("testcase1")
