#!/usr/bin/python
# coding=utf-8


import requests
from Utils import calc_md5


def get_djh_cookies(mobile, password, remember_login=1, type=1):
    """
    获取电竞虎登录接口cookie
    """
    url1 = 'https://www.dianjinghu.com/web.php?m=home&c=login&a=log'
    md5_pw = calc_md5(password)              # 传入明文密码，进行MD5加密
    payload1 = {"mobile": mobile, "password": md5_pw, 'remember_login': remember_login, 'type': type}
    resp = requests.post(url=url1, data=payload1, verify=False)
    return resp.cookies


# 获取用户15221466224的cookies
def cks1():
    cks = get_djh_cookies(15221466224, 123456)
    return cks


if __name__ == '__main__':
    print(cks1())







