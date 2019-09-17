import requests
import json
from Params.params1 import Login

def get_session():
    """
    获取session
    :param env: 获取cookie
    :return:
    """
    data = Login()
    urls = data.url
    params = data.data
    headers = data.header
    session = requests.session()
    response = session.post(urls, params, headers=headers)
    cookie = requests.utils.dict_from_cookiejar(response.cookies)
    return cookie
    # return response.json()["data"]["SWMHPortalToken"]

    # return response.cookies.get_dict()
    # print(response.cookies.get_dict())
#将cookies转换成字典形式，zhihu_cookie为保存的cookie文件，跟程序处在同一路径


if __name__ == '__main__':
    get_session()