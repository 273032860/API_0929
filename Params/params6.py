import os
from Params import tools2
from Common import Log
log = Log.MyLog()
# path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
"""
自定义流程数据
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
    data = tools2.parse()
    keylist=[]
    for n in data[1:]:
        keylist.extend(list(n.keys()))
    # print(keylist)
    return keylist

def casedata(casename):
    #获取yaml文件中的casename的数据，传casename获得data数据
    data = tools2.parse()
    data1= data[caselist().index(casename)+1]
    # print(data1)
    url =data1[casename]["request"]["url"]
    if "json" in data1[casename]["request"].keys():
        data = data1[casename]["request"]["json"]
    else:
        data = data1[casename]["request"]["data"]
    header = data1[casename]["request"]["headers"]
    # a = data["gddjId"]
    # print("processInstanceId" in data.keys())
    # print(a is not None)
    # print(data)
    return url, data, header


if __name__ == '__main__':
    casedata("saveCjlxx15")
    # print("handleTask2" in "handleTask")
    # caselist()