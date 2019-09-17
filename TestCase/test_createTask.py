# -*- coding: utf-8 -*-

import os,sys
sys.path.append("C:/API_Automation-master")  #//path为你的工程根目录的绝对路径
import allure
import pytest
import requests
from Params.params1 import CreateTask
from TestCase import cookie
# from Common import Request
# from Common import Consts
from Common import Assert
import json


class TestcreateTask:
    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Login')
    def test_createTask_01(self):
        """
            用例描述：袁渊账号发起12366工单流程
        """
        data = CreateTask()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        headers = data.header
        response = requests.request("POST", urls, data=json.dumps(params), headers=headers,cookies=cookie.get_session())
        assert test.assert_code(response.status_code, 200)
        taskId = response.json()["data"]["tasks"][0]['taskId']
        processInsId = response.json()["data"]["tasks"][0]['processInsId']
        print(taskId,processInsId)
        assert 'SUCCESS' in response.text
        # Consts.RESULT_LIST.append('True')

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
if __name__ == '__main__':
    s = TestcreateTask()
    s.test_createTask_01()