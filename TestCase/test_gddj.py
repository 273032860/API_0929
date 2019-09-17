# -*- coding: utf-8 -*-

import os,sys
sys.path.append("C:/API_Automation-master")  #//path为你的工程根目录的绝对路径
import allure
import pytest
import requests
from Params import params4
# from TestCase import cookie
# from Common import Request
# from Common import Consts
from Common import Assert
import json
import datetime

def Login(param):
    data = param()
    test = Assert.Assertions()
    urls = data.url
    params = data.data
    headers = data.header
    session = requests.session()
    response = session.post(urls, params, headers=headers)
    assert test.assert_code(response.status_code, 200)
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    return cookie

def save_ty(para,cook):
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

class Testgddj:
    # @pytest.allure.feature('Home')
    # @allure.severity('blocker')
    # @allure.story('Login')
    def test_Login_00(self):
        """
            用例描述：张越冀登录
        """
        return Login(params4.Login_00)

    def test_createTask_01(self):
        """
            用例描述：创建发起流程
        """
        nowTime = datetime.datetime.now().strftime('%m/%d %H:%M:%S')  # 现在
        data = params4.createtask_01()
        test = Assert.Assertions()
        urls = data.url
        params = data.data
        params["preSetTaskName"] = "{0}测试-工单对接流程".format(nowTime)
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

    def test_save_03(self):
        """
            用例描述：环节1保存意见
        """
        save_ty(params4.savety_03,self.test_Login_00())

    def test_save_04(self):
        """
            用例描述：环节1保存表单
        """
        save_form(params4.saveform_04,self.test_Login_00())

    def test_save_05(self):
        """
            用例描述：环节1保存更新
        """
        save_updata(params4.saveupdate_05,self.test_Login_00())

    def test_handleTask_06(self):
        """
            用例描述：推送到个人、企业处理岗
        """
        handleTask(params4.handleTask_06,self.test_Login_00())

    def test_Login_07(self):
        """
            用例描述：袁渊账号登录
        """
        return Login(params4.Login_07)

    def test_save_08(self):
        """
            用例描述：市局接收岗保存意见
        """
        save_ty(params4.savety_08,self.test_Login_07())

    def test_saveupdata_08(self):
        """
            用例描述：市局接收岗保存表单
        """
        save_updata(params4.saveupdata_08,self.test_Login_07())

    def test_handleTask_09(self):
        """
            用例描述：推送到市局处理岗
        """
        handleTask(params4.handleTask_09,self.test_Login_07())

    def test_Login_10(self):
        """
            用例描述：徐俊账号登录
        """
        return Login(params4.Login_10)

    def test_save_11(self):
        """
            用例描述：市局处理岗保存意见
        """
        save_ty(params4.savety_11,self.test_Login_10())

    def test_save_12(self):
        """
            用例描述：市局处理岗保存表单
        """
        save_form(params4.saveform_12,self.test_Login_10())

    def test_save_13(self):
        """
            用例描述：市局处理岗保存更新
        """
        save_updata(params4.saveupdate_13,self.test_Login_10())

    def test_handleTask_14(self):
        """
            用例描述：推送到市局处理岗
        """
        handleTask(params4.handleTask_14,self.test_Login_10())

    def test_Login_15(self):
        """
            用例描述：王毅平账号登录
        """
        return Login(params4.Login_15)

    def test_save_16(self):
        """
            用例描述：市局签发岗保存意见
        """
        save_ty(params4.savety_16,self.test_Login_15())

    def test_saveupdata_16(self):
        """
            用例描述：市局接收岗保存表单
        """
        save_updata(params4.saveupdata_16,self.test_Login_15())

    def test_handleTask_17(self):
        """
            用例描述：推送校稿
        """
        handleTask(params4.handleTask_17,self.test_Login_15())

    # def test_formSimpleId_18(self):
    #     """
    #         用例描述：获取新的form
    #     """
    #     data = params4.getform_18()
    #     test = Assert.Assertions()
    #     urls = data.url
    #     params = data.data
    #     with open('t_s.txt', 'r') as f:
    #         js = f.read()
    #         dic = json.loads(js)
    #     params["taskId"] = dic["taskId"]
    #     params["processInsId"] = dic["processInsId"]
    #     headers = data.header
    #     print(params)
    #     response = requests.request("GET", urls, params=params, headers=headers,
    #                                 cookies=self.test_Login_00())
    #     assert test.assert_code(response.status_code, 200)
    #     assert test.assert_code(response.json()["code"], "SUCCESS")
    #     formId={}
    #     formId["formSimpleId"] = response.json()["data"]["formSimpleId"]
    #     print(response.json()["data"]["formSimpleId"])
    #     print(formId)
    #     with open('formSimpleId.txt', 'w') as f:
    #         f.write(json.dumps(formId))

    def test_save_19(self):
        """
            用例描述：汇总校稿保存意见
        """
        save_ty(params4.savety_19,self.test_Login_00())

    def test_save_20(self):
        """
            用例描述：保存汇总校稿form
        """
        save_form(params4.saveform_20,self.test_Login_00())

    def test_save_21(self):
        """
            用例描述：保存汇总校稿工单数据
        """
        save_updata(params4.saveupdate_21,self.test_Login_00())

    def test_handleTask_22(self):
        """
            推送到稽查局13100540666江帆
        """
        handleTask(params4.handleTask_22,self.test_Login_00())

    def test_Login_23(self):
        """
            用例描述：王毅平账号登录
        """
        return Login(params4.Login_23)

    def test_savety_24(self):
        """
            用例描述：稽查局不同意
        """
        save_ty(params4.savety_24,self.test_Login_23())

    def test_saveupdata_24(self):
        """
            用例描述：稽查局不同意保存表单
        """
        save_updata(params4.saveupdata_24,self.test_Login_23())

    def test_handleTask_25(self):
        """
            用例描述：稽查局不同意
        """
        handleTask(params4.handleTask_25,self.test_Login_23())

    def test_handleTask_26(self):
        """
            用例描述：再次转给稽查局
        """
        handleTask(params4.handleTask_26,self.test_Login_00())

    def test_savety_27(self):
        """
            用例描述：稽查局接收岗同意
        """
        save_ty(params4.savety_27,self.test_Login_23())

    def test_saveupdata_27(self):
        """
            用例描述：稽查局接收岗保存表单
        """
        save_updata(params4.saveupdata_27,self.test_Login_23())

    def test_handleTask_28(self):
        """
            用例描述：推送到稽查处理岗
        """
        handleTask(params4.handleTask_28, self.test_Login_23())

    def test_savety_29(self):
        """
            用例描述：稽查处理岗同意
        """
        save_ty(params4.savety_29,self.test_Login_23())

    def test_saveupdata_29(self):
        """
            用例描述：稽查局处理岗保存表单
        """
        save_updata(params4.saveupdata_29,self.test_Login_23())

    def test_handleTask_30(self):
        """
            用例描述：推送到稽查局签收岗
        """
        handleTask(params4.handleTask_30, self.test_Login_23())

    def test_savety_31(self):
        """
            用例描述：稽查局签发岗同意
        """
        save_ty(params4.savety_31,self.test_Login_23())

    def test_saveupdata_31(self):
        """
            用例描述：稽查局签发岗保存表单
        """
        save_updata(params4.saveupdata_31,self.test_Login_23())

    def test_handleTask_32(self):
        """
            用例描述：稽查局签发岗推送汇总校稿
        """
        handleTask(params4.handleTask_32, self.test_Login_23())

    def test_savety_33(self):
        """
            用例描述：转分局流程同意
        """
        save_ty(params4.savety_33,self.test_Login_00())

    def test_save_34(self):
        """
            用例描述：转分局流程保存表单
        """
        save_ty(params4.saveupdate_34,self.test_Login_00())

    def test_handleTask_35(self):
        """
            用例描述：汇总分发继续转分局接收岗
        """
        handleTask(params4.handleTask_35, self.test_Login_00())

    def test_Login_36(self):
        """
            用例描述：潘耀平登录
        """
        return Login(params4.Login_36)

    def test_savety_37(self):
        """
            用例描述：分局接收岗保存
        """
        save_ty(params4.savety_37,self.test_Login_36())

    def test_save_38(self):
        """
            用例描述：分局接收岗保存表单
        """
        save_ty(params4.saveupdate_38,self.test_Login_36())

    def test_handleTask_39(self):
        """
            用例描述：分局接收岗浦东转其他科室
        """
        handleTask(params4.handleTask_39, self.test_Login_36())

    def test_savety_40(self):
        """
            用例描述：业务科室接收岗保存同意
        """
        save_ty(params4.savety_40,self.test_Login_36())

    def test_saveupdata_40(self):
        """
            用例描述：业务科室接收岗保存表单
        """
        save_updata(params4.saveupdata_40,self.test_Login_36())

    def test_handleTask_41(self):
        """
            用例描述：业务科室接收岗推送处理岗
        """
        handleTask(params4.handleTask_41, self.test_Login_36())

    def test_save_42(self):
        """
            用例描述：业务处理岗保存表单
        """
        save_ty(params4.saveupdate_42,self.test_Login_36())

    def test_savety_43(self):
        """
            用例描述：业务处理岗保存同意
        """
        save_ty(params4.savety_40,self.test_Login_36())

    def test_handleTask_44(self):
        """
            用例描述：业务科室处理岗推送签发岗
        """
        handleTask(params4.handleTask_44, self.test_Login_36())

    def test_savety_45(self):
        """
            用例描述：业务签发岗同意
        """
        save_ty(params4.savety_45,self.test_Login_36())

    def test_saveupdata_45(self):
        """
            用例描述：业务科室签发岗保存表单
        """
        save_updata(params4.saveupdata_45,self.test_Login_36())

    def test_handleTask_46(self):
        """
            用例描述：业务科室签发岗推送各区税务局汇总岗
        """
        handleTask(params4.handleTask_46, self.test_Login_36())

    def test_save_47(self):
        """
            用例描述：各区汇总表单保存
        """
        save_ty(params4.saveupdate_47,self.test_Login_36())

    def test_savety_48(self):
        """
            用例描述：各区汇总同意
        """
        save_ty(params4.savety_48,self.test_Login_36())

    def test_handleTask_49(self):
        """
            用例描述：推送各区税务局汇总签发岗
        """
        handleTask(params4.handleTask_49, self.test_Login_36())




if __name__ == '__main__':
    s = Testgddj()
    # s.test_Login_00() #登录 13100570043
    s.test_createTask_01() #发起流程
    s.test_save_03()
    s.test_save_05() #保存表单
    s.test_handleTask_06() #推送市局个人
    s.test_Login_07() #娄军军登录
    s.test_save_08()  #市局接受岗保存意见
    s.test_saveupdata_08()#市局接收岗保存表单
    s.test_handleTask_09()#推送市局处理岗
    s.test_save_11()
    s.test_save_13() #保存表单
    s.test_handleTask_14() #推送市局签发岗
    s.test_Login_15()#13101050580
    s.test_save_16()
    s.test_saveupdata_16()#市局签收岗保存表单
    s.test_handleTask_17() #推送到校稿
    # s.test_save_19()#汇总校稿保存意见
    # s.test_save_21()#保存汇总校稿工单数据
    # s.test_handleTask_22()#推送到稽查局13100540666江帆
    # s.test_Login_23()#江帆登录 13100540666
    # s.test_savety_24()#稽查局不同意
    # s.test_saveupdata_24()
    # s.test_handleTask_25()#不同意回推汇总分发
    # s.test_handleTask_26()#再次转给稽查局
    # s.test_savety_27()#稽查局接收岗同意
    # s.test_saveupdata_27()
    # s.test_handleTask_28()#推送到稽查处理岗
    # s.test_savety_29()#稽查处理岗同意
    # s.test_saveupdata_29()#稽查处理岗保存表单
    # s.test_handleTask_30()#推送到稽查局签收岗
    # s.test_savety_31()#稽查局签发岗同意
    # s.test_saveupdata_31() #稽查签发岗保存表单
    # s.test_handleTask_32()#稽查局签发岗推送汇总校稿
    # s.test_savety_33()#转分局流程同意
    # s.test_save_34()#转分局流程保存表单
    # s.test_handleTask_35()#汇总分发继续转分局接收岗
    # s.test_savety_37()#分局接收岗保存
    # s.test_save_38()#分局接收岗保存表单
    # s.test_handleTask_39()#分局接收岗浦东转其他科室 13101159240
    # s.test_savety_40()#业务科室接收岗保存同意
    # s.test_saveupdata_40()#业务科室接收岗保存表单
    # s.test_handleTask_41()#业务科室接收岗推送处理岗
    # s.test_save_42()#业务处理岗保存表单
    # s.test_savety_43()#业务处理岗保存同意
    # s.test_handleTask_44()#业务科室处理岗推送签发岗
    # s.test_savety_45()#业务签发岗同意
    # s.test_saveupdata_45()#业务签发岗保存表单
    # s.test_handleTask_46()#业务科室签发岗推送各区税务局汇总岗
    # s.test_save_47()#各区汇总表单保存
    # s.test_savety_48()#各区汇总表单同意
    # s.test_handleTask_49()#推汇总签发