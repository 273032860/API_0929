# -*- coding: utf-8 -*-
# @Time    : 2018/7/30 下午4:14
# @Author  : WangJuan
# @File    : Test_Basic.py
import os,sys
sys.path.append("C:/API_Automation-master")  #//path为你的工程根目录的绝对路径
import allure
import pytest
import requests
from Params.params1 import Login
# from Common import Request
# from Common import Consts
from Common import Assert


class TestLogin:

    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Login')
    def test_Login_01(self):
        """
            用例描述：账号登录
        """
        data = Login()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        headers = data.header
        response = requests.post(urls, params, headers)
        assert test.assert_code(response.status_code, 200)

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
    s=TestLogin()
    s.test_Login_01()