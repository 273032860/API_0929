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
    with shelve.open('t_s.txt') as f:
        taskId = f.get('taskId')
        processInsId = f.get('processInsId')
        login = f.get("login")
    params["taskId"] = taskId
    if "processInstanceId" in params.keys():
        params["processInstanceId"] = processInsId
    if "processInsId" in params.keys():
        params["processInsId"] = processInsId
    zhanghao = login #读取文件内账号
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    # print(response.json())
    if urls.split('/')[-1] == "handleTask":
        with shelve.open('t_s.txt') as f:
            f["taskId"] = response.json()["data"]["tasks"][0]['taskId']
            f["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
            f["login"] = params["nextParticipantMap"][list(params["nextParticipantMap"])[0]][0]["userId"]


def createTask(para,zhanghao):
    urls,params,headers = para
    test = Assert.Assertions()
    nowTime = datetime.datetime.now().strftime('%m/%d %H:%M:%S')
    params["preSetTaskName"] = "{0}自动化测试-自定义表单推税务人员".format(nowTime)
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers, cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert 'SUCCESS' in response.text
    with shelve.open('t_s.txt') as f:
        f["taskId"] = response.json()["data"]["tasks"][0]['taskId']
        f["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
        f["login"] = zhanghao
    assert test.assert_code(response.status_code, 200)

def daoru(zhanghao):
    test = Assert.Assertions()
    urls = "http://10.199.137.214:8080/workflow/web/workflow/form/rwzx/zdybd/excel/import/swry/djxh"
    headers = {}
    fl = open('C:/Users/Lenovo/Desktop/3DJXH.xls', 'rb')
    files = {'files': ('3DJXH.xls', fl, 'multipart/form-data', {'Expires': '0'})}
    params = {}
    with shelve.open('t_s.txt') as f:
        taskId = f.get('taskId')
        processInsId = f.get('processInsId')
        login = f.get("login")
    params["taskId"] = taskId
    params["processInsId"] = processInsId
    # print(params)
    zhanghao = login  # 读取文件内账号
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
    with shelve.open('t_s.txt') as f:
        taskId = f.get('taskId')
        processInsId = f.get('processInsId')
        login = f.get("login")
    with open('queryPushInfo.txt')as f:
        a = json.loads(f.read())
    params["formDataSplitDto"]=a
    params["taskId"] = taskId
    if "processInstanceId" in params.keys():
        params["processInstanceId"] = processInsId
    if "processInsId" in params.keys():
        params["processInsId"] = processInsId
    zhanghao = login #读取文件内账号
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    for inx,nextrw in enumerate(response.json()["data"]["tasks"]):
        with shelve.open('t_s.txt') as f:
            f["taskId{}".format(inx)] = nextrw["taskId"]
            f["processInsId{}".format(inx)] = nextrw['processInsId']
            f["login{}".format(inx)] = params["formDataSplitDto"]["formDataSplitRuleDtoList"][inx]["participantDTOList"][0]["userId"]

def cf_bl(para):
    #拆分后办理
    with shelve.open('t_s.txt')as f:
        cfsl = (len(f.items()) // 3 - 1)
    # 获取文件参数
    for swry in range(cfsl):
        with shelve.open('cft_s_l.txt') as f:
            taskId = f.get('taskId{}'.format(swry))
            processInsId = f.get('processInsId{}'.format(swry))
            login = f.get('login{}'.format(swry))
    urls, params, headers = para
    test = Assert.Assertions()
    params["taskId"] = taskId
    if "processInstanceId" in params.keys():
        params["processInstanceId"] = processInsId
    if "processInsId" in params.keys():
        params["processInsId"] = processInsId
    zhanghao = login  # 读取文件内账号
    # print(params)
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    if urls.split('/')[-1] == "handleTask":
        with shelve.open('t_s.txt') as f:
            f["taskId"] = response.json()["data"]["tasks"][0]['taskId']
            f["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
            f["login"] = params["nextParticipantMap"][list(params["nextParticipantMap"])[0]][0]["userId"]

def saveCjlxx(para):
    #接口容器
    urls,params,headers = para
    test = Assert.Assertions()
    #获取文件参数
    with open('zdybdid.txt')as f:
        a = json.loads(f.read())
    params = a
    with shelve.open('t_s.txt') as f:
        login = f.get("login")
    zhanghao = login  # 读取文件内账号
    print(params)
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")

def queryZdybdDate(para):
    #接口容器
    urls,params,headers = para
    test = Assert.Assertions()
    #获取文件参数
    with shelve.open('t_s.txt') as f:
        taskId = f.get('taskId')
        processInsId = f.get('processInsId')
        login = f.get("login")
    params["taskId"] = taskId
    if "processInstanceId" in params.keys():
        params["processInstanceId"] = processInsId
    if "processInsId" in params.keys():
        params["processInsId"] = processInsId
    zhanghao = login #读取文件内账号
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    with open('zdybdid.txt',"w")as f:
        f.write(json.dumps(response.json()["data"]))
    with open('zdybdid.txt')as f:
        a = json.loads(f.read())
        a["requestDTO"] = a.pop("data")
        del a['total']
        del a['pageSize']
        del a['pageIndex']
        print(a)
        with shelve.open('t_s.txt') as f:
            taskId = f.get('taskId')
            processInsId = f.get('processInsId')
            for n in a["requestDTO"]:
                n["taskId"] = taskId
                n["processInsId"] = processInsId
    with open('zdybdid.txt', "w")as f:
        f.write(json.dumps(a))

def queryPushInfo(para):
    # 接口容器
    urls, params, headers = para
    test = Assert.Assertions()
    # 获取文件参数
    with shelve.open('t_s.txt') as f:
        taskId = f.get('taskId')
        processInsId = f.get('processInsId')
        login = f.get("login")
    params["taskId"] = taskId
    if "processInstanceId" in params.keys():
        params["processInstanceId"] = processInsId
    if "processInsId" in params.keys():
        params["processInsId"] = processInsId
    zhanghao = login  # 读取文件内账号
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    with open('queryPushInfo.txt',"w")as f:
        f.write(json.dumps(response.json()["data"]))

def cfts(para,tpl):
    # 接口容器
    urls, params, headers = para
    test = Assert.Assertions()
    with shelve.open('t_s.txt') as f:
        taskId = f.get('taskId{}'.format(tpl))
        processInsId = f.get('processInsId{}'.format(tpl))
        login = f.get('login{}'.format(tpl))
    # 获取文件参数
    if urls.split('/')[-1] == "get":
        params["participant"]["groupId"]=get_groupid(tpl)
    if "taskId" in params.keys():
        params["taskId"] = taskId
    if "processInstanceId" in params.keys():
        params["processInstanceId"] = processInsId
    if "processInsId" in params.keys():
        params["processInsId"] = processInsId
    if para == "handleTask35":
        with shelve.open('t_s.txt') as f:
            taskId = f.get('taskId')
            processInsId = f.get('processInsId')
        params["participant"]["groupId"] = get_groupid(tpl)
        params["taskId"] = taskId
        params["processInstanceId"] = processInsId
    if urls.split('/')[-1] == "saveCjlxx":
        with open('queryZdybdDate.txt')as f:
            cjsj = json.loads(f.read())
        cjsj[0]["cjl1"] = "数据采集"
        cjsj[0]["taskId"] = taskId
        params = {"requestDTO":cjsj}
    zhanghao = login  # 读取文件内账号
    response = requests.request("POST", urls, data=json.dumps(params), headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    if para == "gwdm26":
        pass
    if para == "handleTask27":
        with shelve.open('t_s.txt',"w") as f:
            f["taskId"] = response.json()["data"]["tasks"][0]['taskId']
            f["processInsId"] = response.json()["data"]["tasks"][0]['processInsId']
            f["login"] = params["nextParticipantMap"][list(params["nextParticipantMap"])[0]][0]["userId"]
    if urls.split('/')[-1] == "queryZdybdDate":
        with open("queryZdybdDate.txt","w")as f:
            f.write(json.dumps(response.json()["data"]["data"]))

def get_groupid(tpl):
    import time
    test = Assert.Assertions()
    with shelve.open('t_s.txt') as f:
        taskId = f.get('taskId{}'.format(tpl))
        processInsId = f.get('processInsId{}'.format(tpl))
        login = f.get('login{}'.format(tpl))
    urls = "http://10.199.137.214:8080/workflow/web/workflow/engine/task/basic/info/query"
    params = {}
    headers = {"Content-Type":"application/json;charset=UTF-8"}
    params["taskId"] = taskId
    params["processInsId"] = processInsId
    params["timestamp"] = (int(round(time.time() * 1000)))
    zhanghao = login
    response = requests.request("GET", urls, params=params, headers=headers,
                                cookies=Login(zhanghao))
    assert test.assert_code(response.status_code, 200)
    assert test.assert_code(response.json()["code"], "SUCCESS")
    return response.json()["data"]["groupData"][-1]["id"]


class Test_zdybd:
    def test_createTask(self):
        createTask(params6.casedata("createTask1"),"13100250014")

    @pytest.mark.parametrize("casename1", params6.caselist()[1:4])
    def test_save(self,casename1):
        save(params6.casedata(casename1))

    def test_daoru(self):
        daoru("13100250014")

    @pytest.mark.parametrize("casename1", params6.caselist()[6:18])
    def test_sh(self,casename1):
        save(params6.casedata(casename1))

    def test_queryZdybdDate(self):
        queryZdybdDate(params6.casedata("queryZdybdDate13"))

    def test_sh1(self):
        save(params6.casedata("param14"))

    def test_saveCjlxx(self):
        saveCjlxx(params6.casedata("saveCjlxx15"))

    def test_queryPushInfo(self):
        queryPushInfo(params6.casedata("queryPushInfo18"))

    def test_handleTask_cf(self,casename1):
        handleTask_cf(params6.casedata(casename1))

    @pytest.mark.parametrize("casename1", params6.caselist()[20:22])
    def test_cfts(self,casename1):
        save(params6.casedata(casename1))

    def test_cfts(self,casename1,tp2):
        cfts(params6.casedata(casename1),tp2)

if __name__ == '__main__':
    s = Test_zdybd()
    s.test_createTask()
    for n in params6.caselist()[1:4]:
        s.test_save(n)
    s.test_daoru()
    for j in params6.caselist()[6:12]:
        s.test_sh(j)
    s.test_queryZdybdDate()
    s.test_sh1()
    s.test_saveCjlxx()
    for j in params6.caselist()[16:17]:
        s.test_sh(j)
        print(j,'通过')
    s.test_queryPushInfo()
    s.test_handleTask_cf("handleTask19")
    for p in range(9):
        for o in params6.caselist()[20:35]:
            s.test_cfts(o,p)
            print(o,p)