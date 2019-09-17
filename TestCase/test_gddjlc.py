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

def Login(para):
    urls,params,headers = para
    test = Assert.Assertions()
    session = requests.session()
    response = session.post(urls, params, headers=headers)
    assert test.assert_code(response.status_code, 200)
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    return cookie

def save(para,cook):
    data = para
    test = Assert.Assertions()
    urls = data.url
    params = data.data
    with open('t_s.txt', 'r') as f:
        js = f.read()
        dic = json.loads(js)
    params["taskId"] = dic["taskId"]
    params["processInsId"] = dic["processInsId"]
    headers = data.header
    print(params)
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=cook)
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")

def handleTask(para,cook):
    urls,params,headers = para
    test = Assert.Assertions()
    with open('t_s.txt', 'r') as f:
        js = f.read()
        dic = json.loads(js)
    params["taskId"] = dic["taskId"]
    params["processInstanceId"] = dic["processInsId"]
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=cook)
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    t_s = {}
    t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
    t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
    with open('t_s.txt', 'w') as f:
        f.write(json.dumps(t_s))

def createTask(para,cook):
    nowTime = datetime.datetime.now().strftime('%m/%d %H:%M:%S')
    urls,params,headers = para
    test = Assert.Assertions()
    params["preSetTaskName"] = "{0}测试-工单对接流程".format(nowTime)
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers, cookies=cook)
    assert test.assert_code(response.status_code, 200)
    assert 'SUCCESS' in response.text
    t_s = {}
    t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
    t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
    with open('t_s.txt', 'w') as f:
        f.write(json.dumps(t_s))
    assert test.assert_code(response.status_code, 200)

class Testgddj:
    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Login')
    def test_Login_00(self):
        """
            用例描述：张越冀登录
        """
        return Login(Login(params5.login1("testcase1")))

    def test_createTask(self):
        """
            用例描述：创建发起流程
        """
        pass

    def test_save_03(self):
        """
            用例描述：环节1保存意见
        """
        pass

    def handleTask(self):
        pass
        # handleTask(params5)



if __name__ == '__main__':
    s = Testgddj()
    # Login(params5.login1("testcase1"))
