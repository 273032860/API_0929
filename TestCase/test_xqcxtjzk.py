# -*- coding: utf-8 -*-

import os,sys
sys.path.append("C:/API_Automation-master")  #//path为你的工程根目录的绝对路径
import allure
import pytest
import requests
from Params import params2
from TestCase import cookie
# from Common import Request
# from Common import Consts
from Common import Assert
import json



# def formSimpleId():
#     url = 'http://10.199.137.214:8080/workflow/web/workflow/form/simple/query/by/processInsId'
#     with open('t_s.txt', 'r') as f:
#         js = f.read()
#         dic = json.loads(js)
#     data={"taskId": 31432, "processInsId": 23230}
#     headers = {}
#     res = requests.get(url=url, params=data, headers=headers, cookies=cookie.get_session())
#     print(res.text)
#     if res.status_code == 200:
#         print(res.json()["data"]["formSimpleId"])
#         return res.json()["data"]["formSimpleId"]
#     else:
#         print("formSimpleId获取失败")

class Testxqcxzk:
    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Login')
    def test_createTask_01(self):
        """
            用例描述：袁渊账号发起需求一体化查询统计类(征科)流程
        """
        data = params2.createtask()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        headers = data.header
        response = requests.request("POST", urls, data=json.dumps(params), headers=headers,cookies=cookie.get_session())
        assert test.assert_code(response.status_code, 200)
        assert 'SUCCESS' in response.text
        t_s = {}
        t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
        t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
        with open('t_s.txt', 'w') as f :
            f.write(json.dumps(t_s))

    def test_save1(self):
        """
            用例描述：保存第一个环节表单
        """
        data = params2.save1()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        print(params)
        with open('t_s.txt', 'r') as f:
            js = f.read()
            dic = json.loads(js)
        params["taskId"] = dic["taskId"]
        params["processInsId"] = dic["processInsId"]
        headers = data.header
        print(params)
        response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                    cookies=cookie.get_session())

        print(response.text)
        assert test.assert_code(response.status_code, 200)
        assert test.assert_code(response.json()["code"], "SUCCESS")

    def test_handleTask1(self):
        """
            用例描述：第一个环节推送到袁渊账号
        """
        data = params2.handleTask1()
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
                                    cookies=cookie.get_session())
        assert test.assert_code(response.status_code, 200)
        assert test.assert_code(response.json()["code"], "SUCCESS")
        # Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    s = Testxqcxzk()
    s.test_createTask_01()
    # s.test_save1()
    s.test_handleTask1()
    # formSimpleId()









    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Basic')
    # def test_basic_02(self, action):
    #     """
    #         用例描述：登陆状态下查看基础设置
    #     """
    #     data = Login()
    #     test = Assert.Assertions()
    #     urls = data.url
    #     params = data.data
    #     headers = data.header
    #     response = requests.post(urls, params, headers)
    #     assert test.assert_code(response.status_code, 200)
    #
    #     assert test.assert_code(response['code'], 401)
    #     assert test.assert_text(response['text'], '{"error":"继续操作前请注册或者登录."}')
    #     Consts.RESULT_LIST.append('True')
