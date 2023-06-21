#!/usr/bin/python
# coding:utf-8
# author:sun

import json
import requests
from pithy import make_session
# from pithy import thrift_client
# from requests import Session
from pithy.api import request
from apis import TestPeafowlConfig
from Utils import cookies1            # 顺序在apis包后


class Peafowl(object):
    # url1 = 'https://'  # 装饰器可引用

    def __init__(self):
        # self.session = make_session()         # pithy中返回的 python-requests库 中的 Session()，使用 requests库 中的 Session()也是一样的
        # self.url = TestPeafowlConfig().test_peafowl_url
        pass

    @request(url=TestPeafowlConfig.test_peafowl_url + "/merchant/queryMerchantList", method='post', cookies=cookies1, verify=False)
    def query_merchant_list0(self, areaCode, latitude, longitude):
        """
        查询医美首页的推荐机构列表(post，上海)
        """
        requests.packages.urllib3.disable_warnings()   # Python requests 设置verify=False移除SSL认证时，解决InsecureRequestWarning
        payload = {"pageSize": 20, "supportType": 1, "areaCode": areaCode,
                   "latitude": latitude, "longitude": longitude, "pageNo": 1}
        return dict(json=payload)  # 看情况使用 json、data or params，与requests.post()用法中的(json=payload)类似，转为仅1个key:'json'的字典

    @request(url=TestPeafowlConfig.test_peafowl_url + '/goodsPackage/getAllGoodsPackage', method='post', cookies=cookies1, verify=False)
    def get_all_goods_package(self, provCode, cityCode):
        """
        查询医美首页的热门套餐(post)
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"pageSize": 10, "supportType": 1, "pageNo": 1, "provCode": provCode, "cityCode": cityCode}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/merchant/queryMerchant', method='post', cookies=cookies1, verify=False)
    def query_merchant(self, merchantCode):
        """
        查询机构详情(post)
        """
        requests.packages.urllib3.disable_warnings()
        payload = {	"merchantCode": merchantCode}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/merchant/queryMerchantGoodsPackage', method='post', cookies=cookies1, verify=False)
    def query_merchant_goods_package(self, merchantCode):
        """
        查询机构详情页的套餐--机构支持的套餐(商品)(post)
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"merchantCode": merchantCode, "supportType": 1}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/area/getAreaInfo', method='post', cookies=cookies1, verify=False)
    def get_area_info(self, provinceCode):
        """
        查询当前城市定位
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"provinceCode": provinceCode}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_angelica_url + '/interests/getOrderList', method='post', cookies=cookies1, verify=False)
    def get_order_list0(self, consumerType, status):
        """
        查询医美'预约列表'-'全部'tab中，多选一权益的数据(15221466071用户的列表)
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"consumerType": consumerType, "status": status}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/reservation/getOrderList', method='post', cookies=cookies1, verify=False)
    def get_order_list1(self, pageNo, pageSize, orderStatusList):
        """
        查询医美'预约列表'-'全部'tab中，第一页所有的普通权益的数据(15221466071用户的列表)
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"pageNo": pageNo, "pageSize": pageSize, "orderStatusList": orderStatusList}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/appointmentManage/addAppointmentUser', method='post', cookies=cookies1, verify=False)
    def add_appointment_user(self, name, sex, mobileNo, dateBirth, relaType):
        """
        添加(15221466071账号的)预约人（为防止数据越来越多，每次新增后会清理）
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"name": name, "sex": sex, "mobileNo": mobileNo, "dateBirth": dateBirth, "relaType": relaType}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/appointmentManage/getAppointmentUser', method='post', cookies=cookies1, verify=False)
    def get_appointment_user(self):
        """
        查询(15221466071账号的)预约人列表 数据
        """
        requests.packages.urllib3.disable_warnings()
        payload = {}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/appointmentManage/updateAppointmentUser', method='post', cookies=cookies1, verify=False)
    def update_appointment_user(self, name, sex, mobileNo, dateBirth, patientId):
        """
        编辑(15221466071账号的)预约人：零七一自动化测试预约人（前端限制，只能更改手机号）
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"name": name, "sex": sex, "mobileNo": mobileNo, "dateBirth": dateBirth, "patientId": patientId}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/merchant/queryMerchantList', method='post', cookies=cookies1, verify=False)
    def query_merchant_list1(self, areaCode, interestsCode, latitude, longitude):
        """
        查询'嗨体功能水光'权益 在'上海市市辖区'支持使用的医美机构
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"pageSize": 50, "supportType": 1, "areaCode": areaCode, "interestsCode": interestsCode,
                   "latitude": latitude, "longitude": longitude, "pageNo": 1}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/mechanism/reservationDate', method='post', cookies=cookies1, verify=False)
    def get_reservation_date(self, merchantCode):
        """
        查询'外滩医美机构1外滩xxxx'机构的 可预约日期
        """
        requests.packages.urllib3.disable_warnings()
        payload = {'merchantCode': merchantCode}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/mechanism/reservationTime', method='post', cookies=cookies1, verify=False)
    def get_reservation_time(self, merchantCode, appDate):
        """
        查询'外滩医美机构1外滩xxxx'机构 某一天的预约时间
        """
        requests.packages.urllib3.disable_warnings()
        payload = {'merchantCode': merchantCode, 'appDate': appDate}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/reservation/create', method='post', cookies=cookies1, verify=False)
    def create_reservation_order(self, merchantCode, appDate, appPeriod, patientId, detailList):
        """
        创建'预约列表'-'待预约'tab中第一个权益的预约单（下下一个用例会调用'取消预约'接口，初始化该权益（取消后，新生成的该权益数据的id会变））
        """
        requests.packages.urllib3.disable_warnings()
        payload = {'merchantCode': merchantCode, 'appDate': appDate, 'appPeriod': appPeriod, 'patientId': patientId,
                   'detailList': detailList}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/reservation/getDetail', method='post', cookies=cookies1, verify=False)
    def get_detail(self, interests_id):
        """
        查询'预约列表'-'预约中'tab中 第一个权益的预约详情
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"id": interests_id}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/reservation/getPatientInfo', method='post', cookies=cookies1, verify=False)
    def get_patient_info(self, interests_id):
        """
        点击查询 '预约中'tab中 第一个权益的预约详情的 '预约人'信息
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"id": interests_id}
        return dict(json=payload)

    @request(url=TestPeafowlConfig.test_peafowl_url + '/reservation/cancel', method='post', cookies=cookies1, verify=False)
    def cancel_reservation_order(self, interests_id, merchantCode):
        """
        取消预约 '预约中'tab中的第一个权益（有多个'待确认'状态的权益时，预约时间近的 排序更靠前）
        """
        requests.packages.urllib3.disable_warnings()
        payload = {"id": interests_id, "merchantCode": merchantCode}
        return dict(json=payload)








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


