#!/usr/bin/python
# coding=utf-8

import os
import requests
from pithy import pretty_print
# from prettyprinter import cpprint


class BaseApi:
    def req_helper(self, req):
        # 使用python关键字传参，将请求结构体传给requests.request()方法
        # def request(method, url, **kwargs)   (requests.request()所需参数)
        resp = requests.request(**req)
        return resp


# 示例：
class Djh_sign_in(BaseApi):
    pass


payload1 = {
    'method': 'post',
    'url': 'https://www.dianjinghu.com/web.php?m=home&c=login&a=log',
    'data': {"mobile": 15221466224, "password": 'e10adc3949ba59abbe56e057f20f883e', 'remember_login': 1, 'type': 1},
    'verify': False
}
pretty_print(Djh_sign_in().req_helper(payload1).json())




















