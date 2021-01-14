#!/usr/bin/python
# coding:utf-8

import json
from pithy import request
from pithy import make_session
# from pithy import thrift_client


class DeviceInfoChange(object):

    def __init__(self):
        self.session = make_session()
        self.tk = "ACEgCobn-bhOr3o0YjunutQIVwOZtF8V95lrZGQ"

    @request(url="http://hadmin.redianduanzi.com/admin/user/login", method='post')
    def get_pro_token(self, account, password):
        """
        获取线上配置后台登录时的token
        """
        payload = {"account": account, "password": password}
        return dict(data=payload)

    @request(url="http://kanduoduo.redianduanzi.com/admin/device/clear", method='get')
    def device_info_clear(self, token):
        """
        线上清除、刷新设备信息
        """
        params = {"token": token, "tk": self.tk}
        return dict(params=params)

    @request(url="http://kanduoduo.redianduanzi.com/admin/device/get", method='get')
    def device_info_get(self, token):
        """
        线上清除设备信息后，查看设备信息
        """
        params = {"token": token, "tk": self.tk}
        return dict(params=params)

    # 调用soa接口示例

    # @request(url="http://xxxx:9140/rpc", interface_type="SOA", method="POST")
    # def get_shipping_order(tracking_id, contents, app_id):
    #     """
    #     Restful接口调用方式
    #     :param tracking_id:
    #     :param contents:
    #     :param app_id:
    #     :return:
    #     """
    #     iface = 'me.ele.socquery.api.ShippingOrderQueryService'
    #     method = 'getShippingOrder'
    #     args = dict(
    #         trackingId=tracking_id,
    #         contents=contents if contents else [],
    #         appId=app_id
    #     )

# 调用thrift接口示例（在thrift方法中传参，可以在方法体中传，也可以在参数列表中定义）

# @thrift_client
# class GaiaService(object):
#     """
#     Thrift调用方式
#     """
#
#     def __init__(self):
#         self.thrift_file = "ThriftFile/gaia.thrift"
#         self.port = 18200
#         self.host = "xxxxx.vm.elenet.me"









