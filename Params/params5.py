import os
from Params import tools1
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
"""
工单对接流程数据
"""
# def get_parameter(name):
#     #将数据封装成只剩data、headers、url数据，传参yaml名，case名
#     data = tools1.parse()
#     print(data)
#     # param = data[name]
#     # param = data[name][0][case]["request"]
#
#     # print(type(param))
#     # return param

def caselist():
    #获取整理完的数据接口名，传yaml名
    data = tools1.parse()
    keylist=[]
    for n in data[1:]:
        keylist.extend(list(n.keys()))
    return keylist


# def login1(case):
#     params = get_parameter("lgo",case)
#     url = params["url"]
#     data = params["data"]
#     header = params["headers"]
#     return url,data,header
#
def casedata(casename):
    #获取yaml文件中的casename的数据，传casename获得data数据
    data = tools1.parse()
    data1= data[caselist().index(casename)+1]
    url =data1[casename]["request"]["url"]
    data = data1[casename]["request"]["json"]
    header = data1[casename]["request"]["headers"]
    print(url,data,header)
    return url, data, header


if __name__ == '__main__':
    # login1("testcase1")
    # casedata("createTask1")
    casedata("createTask1")
