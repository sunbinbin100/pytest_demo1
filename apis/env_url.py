#!/usr/bin/python
# coding:utf-8

import os


class ProDeviceConfig:
    """
    线上环境kddurl
    """
    # url="http://test1-api-kdd.qttcs3.cn"
    pro_kdd_url = 'http://kanduoduo.redianduanzi.com'
    # url='127.0.0.1:2051/small_video'


class PreDeviceConfig:
    """
    预发布环境kddurl
    """
    pre_kdd_url = 'http://pre-kanduoduo.redianduanzi.com'


class ProPZHTConfig:
    """
    线上配置后台登录接口
    """
    pro_kdd_url = "http://kanduoduo.qutoutiao.net/admin/user/login"


class test_kdd:
    KDD_DB = "mysql://rddz:re.dz@2019@10.0.1.237/kanduoduo?charset=utf8"


class Djh_url_pro:
    login_url = 'https://www.dianjinghu.com/web.php?m=home&c=login&a=log'
    p_c_url = 'https://www.dianjinghu.com/web.php?m=home&c=memberNew&a=center'













