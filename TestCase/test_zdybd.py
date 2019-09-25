# -*- coding: utf-8 -*-

import os,sys
sys.path.append("C:/API_Automation-master")  #//path为你的工程根目录的绝对路径
import allure
import pytest
import requests
from Params import params6
# from TestCase import cookie
# from Common import Request
# from Common import Consts
from Common import Assert
import json
import datetime
import shelve

def Login(zhanghao):
    urls = "http://10.199.137.214:8080/swmh/login.action"
    params = {"loginParam": zhanghao+",123"}
    headers = {}
    test = Assert.Assertions()
    session = requests.session()
    response = session.post(urls, params, headers=headers)
    assert test.assert_code(response.status_code, 200)
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    # print(cookie)
    return cookie

def save(para):
    #接口容器
    urls,params,headers = para
    test = Assert.Assertions()
    #获取文件参数
    with open('t_s.txt', 'r') as f:
        js = f.read()
        dic = json.loads(js)
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


def createTask(para,zhanghao):
    urls,params,headers = para
    test = Assert.Assertions()
    nowTime = datetime.datetime.now().strftime('%m/%d %H:%M:%S')
    params["preSetTaskName"] = "{0}自动化测试-自定义表单推税务人员".format(nowTime)
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

def daoru(zhanghao):
    test = Assert.Assertions()
    urls = "http://10.199.137.214:8080/workflow/web/workflow/form/rwzx/zdybd/excel/import/swry/djxh"
    headers = {}
    # files = {"file": open("C:/Users/Lenovo/Desktop/3DJXH.xls", "rb")}
    fl = open('C:/Users/Lenovo/Desktop/3DJXH.xls', 'rb')
    files = {'files': ('3DJXH.xls', fl, 'multipart/form-data', {'Expires': '0'})}
    params = {}
    with open('t_s.txt', 'r') as f:
        js = f.read()
        dic = json.loads(js)
    params["taskId"] = dic["taskId"]
    params["processInsId"] = dic["processInsId"]
    # print(params)
    zhanghao = dic["login"]  # 读取文件内账号
    # print(zhanghao)
    response = requests.post(urls, params,files=files,headers=headers,cookies=Login(zhanghao))
    # print(response.text)
    assert test.assert_code(response.status_code, 200)
    assert 'SUCCESS' in response.text

def handleTask_cf(para):
    #接口容器
    urls,params,headers = para
    test = Assert.Assertions()
    #获取文件参数
    with open('t_s.txt', 'r') as f:
        js = f.read()
        dic = json.loads(js)
    params["taskId"] = dic["taskId"]
    if "processInstanceId" in params.keys():
        params["processInstanceId"] = dic["processInsId"]
    if "processInsId" in params.keys():
        params["processInsId"] = dic["processInsId"]
    zhanghao = dic["login"] #读取文件内账号
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    cflb = []
    for inx,nextrw in enumerate(response.json()["data"]["tasks"]):
        t_scf={}
        t_scf["taskId"] = nextrw["taskId"]
        t_scf["processInsId"] = nextrw['processInsId']
        # print(params["formDataSplitDto"]["formDataSplitRuleDtoList"][inx]["participantDTOList"][inx]["userId"])
        t_scf["login"] = params["formDataSplitDto"]["formDataSplitRuleDtoList"][inx]["participantDTOList"][0]["userId"]
        cflb.append(t_scf)
    with open('cflb.txt', 'w') as f:
        f.write(json.dumps(cflb))

class Test_zdybd:
    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Login')
    def test_createTask(self):
        """
            用例描述：发起流程
        """
        createTask(params6.casedata("createTask1"),"13100250014")
    #
    @pytest.mark.parametrize("casename1", params6.caselist()[1:4])
    def test_save(self,casename1):
        """
            用例描述：环节1保存意见
        """
        save(params6.casedata(casename1))

    def test_daoru(self):
        daoru("13100250014")

    @pytest.mark.parametrize("casename1", params6.caselist()[6:18])
    def test_sh(self,casename1):
        save(params6.casedata(casename1))

    def test_handleTask_cf(self,casename1):
        handleTask_cf(params6.casedata(casename1))



if __name__ == '__main__':
    # s.test_createTask()
    s = Test_zdybd()
    # s.test_createTask()
    # for n in params6.caselist()[1:4]:
    #     s.test_save(n)
    # s.test_daoru()
    # for j in params6.caselist()[6:18]:
    #     s.test_sh(j)
    # s.test_handleTask_cf("handleTask19")
