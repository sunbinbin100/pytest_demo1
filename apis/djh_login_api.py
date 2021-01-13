#!/usr/bin/python
# coding=utf-8

import json
import requests
from pithy.api import request
from pithy import make_session
from Utils import cks1, calc_md5
from apis.env_url import Djh_url_pro  # 使用绝对路径导入
# from requests import Session


class DJHLogin(object):
    # url1 = '111'  # 装饰器可引用

    def __init__(self):
        self.session = make_session()            # pithy中返回的 requests库中的 Session()，使用  requests中的 Session()也是一样的
        # self.url2 = ''  # 装饰器不可引用

    @request(url=Djh_url_pro.login_url, method='post', verify=False)  # 忽略对 SSL 证书的验证
    def djh_login(self, mobile, password, remember_login=1, type=1):
        """
        电竞虎登录接口(post)
        """
        md5_pw = calc_md5(password)
        payload = {"mobile": mobile, "password": md5_pw, 'remember_login': remember_login, 'type': type}
        return dict(data=payload)

    @request(url=Djh_url_pro.p_c_url, method='get', cookies=cks1(), verify=False)  # 装饰器里可引用全局变量 或 类的局部变量，不能引用 self.url='xx' 这种的类变量
    def djh_personal_center(self, mm, cc, aa):
        """
        电竞虎个人中心接口(get)
        """
        params = {'m': mm, 'c': cc, 'a': aa}
        return dict(params=params)


# demo
def laotie_oauth(msg, version=None, rule=None):
    """
    OAuth2协议
    (老铁)热点段子加密encrypt
    """
    '''
    新版客户端加密密钥:ZmsU4tREJ9P/NbGQIN2OzUmOkAwaJE3Yycom1GhYZUI=
    新版客户端加密版本: 6
    '''
    auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.\
    eyJ1aWQiOjk2LCJuYW0iOiJsaXdlbndlbiIsImlhdCI6MTU2ODYwMDQ5NCwiZXhwIjoxNTY4NjAyMjk0LCJyb3MiOjQsInBkcyI6WyJrZGQiXX0.\
    SVicbpkkcuMnhEFQ4e2RVT7RHmA2yxZ1bD_XQQFwXhk"
    headers = {'Authorization': 'Bearer ' + auth_token}
    paload = {"encode": "1",
              "direction": "ctos",
              "version": "6",
              "platform": "android",
              "key": "ZmsU4tREJ9P/NbGQIN2OzUmOkAwaJE3Yycom1GhYZUI=",
              "params": "cf262ba1-4e26-4f87-9579-244517a4c5bb",
              "plain": json.dumps(msg)}
    url = "https://p1.innotechx.com/v1/tool/encrypt_test"
    res = requests.post(url, json=paload, headers=headers).json()
    return {'qdata': res['data']['cipher']}


# if __name__ == '__main__':
#     print(laotie_oauth(1))




