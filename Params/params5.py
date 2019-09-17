import os
from Params import tools1
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
"""
工单对接流程数据
"""
def get_parameter(name,case):
    #将tools封装成函数
    data = tools1.parse()
    # print(data)
    param = data[name][case]["request"]
    # # print(param)
    return param

class login():
    def __init__(self,case1):
        params = get_parameter("lgo",case1)
        self.url = params["url"]
        self.data = params["data"]
        self.header = params["headers"]

# class createtask_01():
#     params = get_parameter("wwww","testcase1")
#     url = params["url"]
#     data = params["json"]
#     header = params["headers"]
#
class casedata():
    def __init__(self,case1):
        params = get_parameter("wwww",case1)
        self.url = params["url"]
        self.data = params["json"]
        self.header = params["headers"]


#
# if __name__ == '__main__':
#     # get_parameter()
#     s = casedata("createTask1")

