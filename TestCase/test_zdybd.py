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

def Login(login):
    data = params5.login(login)
    test = Assert.Assertions()
    urls = data.url
    params = data.data
    headers = data.header
    session = requests.session()
    response = session.post(urls, params, headers=headers)
    assert test.assert_code(response.status_code, 200)
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    return cookie

def onlyt_s(para,cook):
    data = para()
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

def save_form(para,cook):
    data = para()
    test = Assert.Assertions()
    urls = data.url
    params = data.data
    with open('t_s.txt', 'r') as f:
        js = f.read()
        dic = json.loads(js)
    params["taskId"] = dic["taskId"]
    params["processInsId"] = dic["processInsId"]
    with open('formSimpleId.txt', 'r') as f:
        form1 = f.read()
        fordic = json.loads(form1)
    params["formSimpleId"]=fordic["formSimpleId"]
    headers = data.header
    print(params)
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=cook)
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    formId={}
    formId["formSimpleId"] = response.json()["data"]["formSimpleId"]
    with open('formSimpleId.txt', 'w') as f:
        f.write(json.dumps(formId))


def save_updata(para,cook):
    data = para()
    test = Assert.Assertions()
    urls = data.url
    params = data.data
    with open('t_s.txt', 'r') as f:
        js = f.read()
        dic = json.loads(js)
    params["taskId"] = dic["taskId"]
    params["processInsId"] = dic["processInsId"]
    headers = data.header
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=cook)
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")

def handleTask(para,cook):
    data = para()
    test = Assert.Assertions()
    urls = data.url
    params = data.data
    with open('t_s.txt', 'r') as f:
        js = f.read()
        dic = json.loads(js)
    params["taskId"] = dic["taskId"]
    params["processInstanceId"] = dic["processInsId"]
    headers = data.header
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=cook)
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    t_s = {}
    t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
    t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
    with open('t_s.txt', 'w') as f:
        f.write(json.dumps(t_s))

class Testzdybd:
    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Login')
    def test_Login_00(self):
        """
            用例描述：张越冀登录
        """
        return Login("testcase1")

    def test_createTask_01(self):
        """
            用例描述：创建发起流程
        """
        nowTime = datetime.datetime.now().strftime('%m/%d %H:%M:%S')  # 现在
        data = params5.casedata("createTask1")
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        params["preSetTaskName"] = "{0}测试-工单对接流程".format(nowTime)
        headers = data.header
        response = requests.request("POST", urls, data=json.dumps(params), headers=headers,cookies=Login("testcase1"))
        assert test.assert_code(response.status_code, 200)
        assert 'SUCCESS' in response.text
        t_s = {}
        t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
        t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
        with open('t_s.txt', 'w') as f :
            f.write(json.dumps(t_s))
        assert test.assert_code(response.status_code, 200)

    def test_param_02(self):
        """
            用例描述：环节1保存意见
        """
        onlyt_s(params5.casedata("param2"),self.test_Login_00)

    def test_save_03(self):
        """
            用例描述：环节1保存表单
        """
        onlyt_s(params5.casedata("save3"),self.test_Login_00)

    def test_updateGddjxx_04(self):
        """
            用例描述：环节1保存更新
        """
        save_updata(params5.casedata("updateGddjxx4"),self.test_Login_00)

    def test_type5(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        handleTask(params5.type5,self.test_Login_00)

    def test_get6(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.get6,self.test_Login_00)

    def test_lszDm7(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.lszDm7,self.test_Login_00)

    def test_save8(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.save8,self.test_Login_00)

    def test_handleTask9(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        handleTask(params5.handleTask9,self.test_Login_00())

    def test_Login_02(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        return Login("testcase2")

    def test_queryJcjksSwjg10(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.queryJcjksSwjg10,self.test_Login_02())

    def test_param11(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.param11,self.test_Login_02())

    def test_save12(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.save12,self.test_Login_02())

    def test_updateGddjxx13(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.updateGddjxx13,self.test_Login_02())

    def test_type14(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.type14,self.test_Login_02())

    def test_get15(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.get15,self.test_Login_02())

    def test_lszDm16(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.lszDm16,self.test_Login_02())

    def test_save17(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.save17,self.test_Login_02())

    def test_handleTask18(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        handleTask(params5.handleTask18,self.test_Login_02())

    def test_queryJcjksSwjg19(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.queryJcjksSwjg19,self.test_Login_02())

    def test_param20(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.param20,self.test_Login_02())

    def test_save21(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.lszDm16,self.test_Login_02())

    def test_lszDm16(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.lszDm16,self.test_Login_02())

    def test_lszDm16(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.lszDm16,self.test_Login_02())

    def test_lszDm16(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        onlyt_s(params5.lszDm16,self.test_Login_02())





if __name__ == '__main__':
    s = Testzdybd()
    s.test_createTask_01()
