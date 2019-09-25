# -*- coding: utf-8 -*-

import os,sys
sys.path.append("C:/API_Automation-master")  #//path为你的工程根目录的绝对路径
import allure
import pytest
import requests
from Params import params5
# from TestCase import cookie
# from Common import Request
# from Common import Consts
from Common import Assert
import json
import datetime

def Login(zhanghao):
    urls = "http://10.199.137.214:8080/swmh/login.action"
    params = {"loginParam": zhanghao+",123"}
    headers = {}
    test = Assert.Assertions()
    session = requests.session()
    response = session.post(urls, params, headers=headers)
    assert test.assert_code(response.status_code, 200)
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    return cookie

def save(para):
    #接口容器
    urls,params,headers = para
    test = Assert.Assertions()
    #获取文件参数
    with open('t_s.txt', 'r') as f:
        js = f.read()
        dic = json.loads(js)
    if urls.split('/')[-1] == "updateGddjxx": #判断保存，传gddjId
        if params["gddjId"] is not None:
            with open('gddjId.txt', 'r') as f:
                js = f.read()
                dic1 = json.loads(js)
            params["gddjId"] = dic1["gddjId"]
    params["taskId"] = dic["taskId"]
    if "processInstanceId" in params.keys():
        params["processInstanceId"] = dic["processInsId"]
    if "processInsId" in params.keys():
        params["processInsId"] = dic["processInsId"]
    zhanghao = dic["login"] #读取文件内账号
    # print(params)
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    if urls.split('/')[-1] == "handleTask":
        t_s = {}
        t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
        t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
        t_s["login"] = params["nextParticipantMap"][list(params["nextParticipantMap"])[0]][0]["userId"]
        with open('t_s.txt', 'w') as f:
            f.write(json.dumps(t_s))
    if urls.split('/')[-1] == "updateGddjxx":
        gddjId = {}
        gddjId["gddjId"] = response.json()["data"]
        with open('gddjId.txt', 'w') as f:
            f.write(json.dumps(gddjId))

def createTask(para,zhanghao):
    urls,params,headers = para
    test = Assert.Assertions()
    nowTime = datetime.datetime.now().strftime('%m/%d %H:%M:%S')
    params["preSetTaskName"] = "{0}自动化测试-市局流程".format(nowTime)
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers, cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert 'SUCCESS' in response.text
    t_s = {}
    t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
    t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
    t_s["login"] = zhanghao
    with open('t_s.txt', 'w') as f:
        f.write(json.dumps(t_s))
    assert test.assert_code(response.status_code, 200)

class Testgddj:
    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Login')
    def test_createTask(self):
        """
            用例描述：发起流程
        """
        createTask(params5.casedata("createTask1"),"13100570043")

    @pytest.mark.parametrize("casename1", params5.caselist()[1:])
    def test_save(self,casename1):
        """
            用例描述：环节1保存意见
        """
        save(params5.casedata(casename1))



if __name__ == '__main__':
    # s.test_createTask()
    s = Testgddj()
    s.test_createTask()
    s.test_save()
