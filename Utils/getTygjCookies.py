#!/usr/bin/python
# coding=utf-8

import json
import requests
# from apis.env_url import TestPeafowlConfig
# from prettyprinter import cpprint


def get_tygj_cookies(mobile, verificationCode):
    """
    获取 使用验证码登录太医管家App后的Cookie
    """
    sms_login_url = 'https://api.test.shantaijk.cn/api/cif-login/cif/loginService/smsLogin'
    payload1 = {
        "clientType": "00", "appType": "IOS",
        "systemLanguage": "zh-Hans-CN", "deviceId": "FB307235-1C18-4B85-8479-38C74AC39227",
        "verificationSeqNo": "SMS_A00001", "deviceDesc": "iPhone8P", "deviceName": "iPhone",
        "verificationCode": verificationCode,
        "appVersion": "11500", "version": "11500", "protocolVersion": "2.0",
        "mobileNo": mobile, "roleType": "USER",
        "wifiName": "", "networkType": "WiFi", "traceLogId": "1661829400",
        "appId": "2", "isRooted": False, "wifiDetail": ",",
        "carrier": "中国移动", "systemVersion": "14.4",
        "IDFV": "8823C96C-559C-45FB-BBAF-6233D04E3BAB",
        "protocolCode": "A0001", "userId": ""
    }
    requests.packages.urllib3.disable_warnings()  # requests设置verify=False移除SSL认证时，解决InsecureRequestWarning警告
    resp = requests.post(url=sms_login_url, json=payload1, verify=False)
    return resp.cookies  # 或 '_tk=' + resp.json()['result']['sessionKey']、


# 获取账号 15221466071 登录后的Cookie（全局变量，重复利用）
cookies1 = get_tygj_cookies(15221466071, 111111)


# if __name__ == '__main__':
#     print(cookies1)











