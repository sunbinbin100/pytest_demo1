#!/usr/bin/python
# coding:utf-8

import os


class TestPeafowlConfig:
    """
    医美测试环境path
    """
    test_peafowl_url = 'https://api.test.shantaijk.cn/api/peafowl'
    test_angelica_url = 'https://api.test.shantaijk.cn/api/angelica'


class PrePeafowlConfig:
    """
    医美预发环境xx地址
    """
    pre_peafowl_url = 'https://api.pre.shantaijk.cn/'


class ProPeafowlConfig:
    """
    医美线上环境xx地址
    """
    pro_peafowl_url = 'https://api.shantaijk.cn/'


class Stjk_db:
    """
    杉泰测试环境数据库链接
    """
    stjk_db_url = "mysql://test_group:Shantai@test@mysql-test-in.shantaijk.cn?charset=utf8"
    kdd_db_url = "mysql://rddz:re.dz@2019@10.0.1.237/kanduoduo?charset=utf8"


# class ProPZHTConfig:
#     """
#     线上配置后台登录接口
#     """
#     pro_kdd_url = "http://kanduoduo.qutoutiao.net/admin/user/login"


class Djh_url_pro:
    login_url = 'https://www.dianjinghu.com/web.php?m=home&c=login&a=log'
    p_c_url = 'https://www.dianjinghu.com/web.php'













