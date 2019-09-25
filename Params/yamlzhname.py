# -*- coding: utf-8 -*-
"""
读取yaml测试数据

"""
import yaml
import os
import os.path

def parse(yname):
    #读取所有yml数据并用字典形式保存
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params/自定义表单/创建任务-拆分前'
    # print(path_ya)
    pages = []
    for root, dirs, files in os.walk(path_ya):
        #os.walk获取路径、[]、文件名
        for name in files:
            #只获取文件
            watch_file_path = os.path.join(root, name)
            #将root路径+files文件名做拼接C:/Users/Lenovo/Desktop/接口文档/har2case/工单对接\login.yaml
            with open(watch_file_path, 'r', encoding='UTF-8') as f:
                page = yaml.safe_load(f)
                for n in range(1,len(page)):
                    # print(len(page))
                    list1= (page[n]["test"]["name"].split('/')[-1]+"{0}".format(n))
                    page[n][list1] = page[n].pop("test")
                    pages.append(page)
    # print(page)
    pages[0][0]["config"] = yname
    with open(path_ya+"/xiugai/{}.yaml".format(yname),"w")as yaml_file:
        yaml.dump(pages[0], yaml_file)
    # print()


if __name__ == '__main__':
    parse("zdy_cjrw")
