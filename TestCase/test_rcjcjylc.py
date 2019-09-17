# -*- coding: utf-8 -*-

import os,sys
sys.path.append("C:/API_Automation-master")  #//path为你的工程根目录的绝对路径
import allure
import pytest
import requests
from Params import params3
# from TestCase import cookie
# from Common import Request
# from Common import Consts
from Common import Assert
import json



class Testrcjcjy:
    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Login')
    def test_Login_00(self):
        """
            用例描述：吕桂芬登录
        """
        data = params3.Login_00()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        headers = data.header
        # response = requests.post(urls, params, headers)
        session = requests.session()
        response = session.post(urls, params, headers=headers)
        # print(response.text)
        assert test.assert_code(response.status_code, 200)
        cookie = requests.utils.dict_from_cookiejar(response.cookies)
        return cookie

    def test_createTask_01(self):
        """
            用例描述：吕桂芬账号发起日常检查简易流程
        """
        data = params3.createtask_01()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        headers = data.header
        response = requests.request("POST", urls, data=json.dumps(params), headers=headers,cookies=self.test_Login_00())
        assert test.assert_code(response.status_code, 200)
        assert 'SUCCESS' in response.text
        t_s = {}
        t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
        t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
        with open('t_s.txt', 'w') as f :
            f.write(json.dumps(t_s))
        assert test.assert_code(response.status_code, 200)

    def test_save_02(self):
        """
            用例描述：保存第一个环节表单
        """
        data = params3.save_02()
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
                                    cookies=self.test_Login_00())

        print(response.text)
        assert test.assert_code(response.status_code, 200)
        assert test.assert_code(response.json()["code"], "SUCCESS")

    def test_handleTask_03(self):
        """
            用例描述：推送1
        """
        data = params3.handleTask_03()
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
                                    cookies=self.test_Login_00())
        assert test.assert_code(response.status_code, 200)
        assert test.assert_code(response.json()["code"], "SUCCESS")
        t_s = {}
        t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
        t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
        with open('t_s.txt', 'w') as f:
            f.write(json.dumps(t_s))
        # Consts.RESULT_LIST.append('True')


    def test_Login_04(self):
        """
            用例描述：缪军登录
        """
        data = params3.Login_04()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        headers = data.header
        session = requests.session()
        response = session.post(urls, params, headers=headers)
        assert test.assert_code(response.status_code, 200)
        cookie = requests.utils.dict_from_cookiejar(response.cookies)
        return cookie


    def test_qianshou_05(self):
        """
            用例描述：缪军岗位签收
        """
        data = params3.qianshou_05()
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
                                    cookies=self.test_Login_04())
        # print(response.text)
        assert test.assert_code(response.status_code, 200)
        # assert test.assert_code(response.json()["code"], "SUCCESS")

    def test_save_06(self):
        """
            用例描述：缪军录入信息保存
        """
        data = params3.save_06()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        headers = data.header

        response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                    cookies=self.test_Login_04())
        assert test.assert_code(response.status_code, 200)
        assert test.assert_code(response.json()["code"], "SUCCESS")

    def test_handleTask_07(self):
        """
            用例描述：缪军环节2推送
        """
        data = params3.handleTask_07()
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
                                    cookies=self.test_Login_04())
        assert test.assert_code(response.status_code, 200)
        assert test.assert_code(response.json()["code"], "SUCCESS")
        t_s = {}
        t_s["taskId"] = response.json()["data"]["tasks"][0]['taskId']
        t_s["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
        with open('t_s.txt', 'w') as f:
            f.write(json.dumps(t_s))


    def test_biaogeshuju_08(self):
        """
            用例描述：缪军环节3读取
        """
        data = params3.biaogeshuju_08()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        # data={"taskId": 31432, "processInsId": 23230}
        headers = {}
        response = requests.get(url=urls, params=params, headers=headers, cookies=self.test_Login_04())
        # print(res.text)
        if response.status_code == 200:
            print(response.json()["data"]["formSimpleId"])
            return response.json()["data"]["formSimpleId"]
        else:
            print("formSimpleId获取失败")
        assert test.assert_code(response.status_code, 200)

    def test_save_09(self):
        """
            用例描述：缪军环节3保存
        """
        data = params3.save_09()
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
                                    cookies=self.test_Login_04())
        assert test.assert_code(response.status_code, 200)

    def test_handleTask_10(self):
        """
            用例描述：缪军环节3推送
        """
        data = params3.handleTask_10()
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
                                    cookies=self.test_Login_04())
        assert test.assert_code(response.status_code, 200)
        assert test.assert_code(response.json()["code"], "SUCCESS")
        # Consts.RESULT_LIST.append('True')

    def test_handleTask_11(self):
        """
            用例描述：缪军环节4推送
        """
        data = params3.handleTask_11()
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
                                    cookies=self.test_Login_04())
        assert test.assert_code(response.status_code, 200)
        assert test.assert_code(response.json()["code"], "SUCCESS")
        # Consts.RESULT_LIST.append('True')

    def test_handleTask_12(self):
        """
            用例描述：缪军环节5推送
        """
        data = params3.handleTask_12()
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
                                    cookies=self.test_Login_04())
        assert test.assert_code(response.status_code, 200)
        assert test.assert_code(response.json()["code"], "SUCCESS")
        # Consts.RESULT_LIST.append('True')

    def test_save_13(self):
        """
            用例描述：缪军归档资料新增
        """
        data = params3.save_13()
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
                                    cookies=self.test_Login_04())
        assert test.assert_code(response.status_code, 200)

    def test_save_14(self):
        """
            用例描述：缪军归档页面保存
        """
        data = params3.save_14()
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
                                    cookies=self.test_Login_04())
        assert test.assert_code(response.status_code, 200)



if __name__ == '__main__':
    s = Testrcjcjy()
    # s.test_Login_00()
    s.test_createTask_01()
    # s.test_save_02()
    # s.test_handleTask_03()
    # s.test_Login_04()
    # s.test_qianshou_05()
    # s.test_save_06()
    # s.test_handleTask_07()
    # s.test_biaogeshuju_08()