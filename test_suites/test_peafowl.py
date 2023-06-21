#!/usr/bin/python
# coding:utf-8
# author:sun

import os
import sys
import pytest
import requests
from pithy import Config
from pithy import pretty_print
from apis.env_url import TestPeafowlConfig  # 绝对路径导入
from apis import Peafowl
from Test_Config.db_uat import get_db_info, sql_execute_get_one


class TestPeafowl(object):
    """医美接口服务"""

    def setup(self):
        """
        初始化接口
        """
        self.Peafowl = Peafowl()               # 1次初始化为类对象，供各用例重复使用，避免各用例重复调用Peafowl()类
        # self.base_url = TestPeafowlConfig.test_peafowl_url

    # @pytest.mark.run              # .run(order=1)  需安装pytest-ordering插件
    @pytest.mark.timeout(10)  # 限定10s超时
    def test_query_merchant_list0(self, areaCode1="310100", latitude1="31.160076",
                                  longitude1="121.433532"):  # 或用 @pytest.mark.parametrize("xxx", [1, 2, 3]) 参数化方法
        """
        查询医美首页的推荐机构列表（上海）
        """
        resp = self.Peafowl.query_merchant_list0(areaCode1, latitude1, longitude1).to_json()
        assert resp.success is True
        assert resp['errorMsg'] == '成功'  # assert resp.result.total == 4
        # assert isinstance(resp['result']['list'][0], dict)
        assert resp.result.list[0].merchantName == '医美大美丽实体机构1'
        assert resp.result.list[2].merchantName == '外滩医美机构1外滩医美机构1外滩医美机构1外滩医美机构1外滩医美机构1外滩医美机构1外滩医美机构1外'

    @pytest.mark.flaky(reruns=2, reruns_delay=1)  # 失败则延迟1s后重跑，一共跑2次
    def test_get_all_goods_package(self):
        """
        查询医美首页的热门套餐（上海）
        """
        resp = self.Peafowl.get_all_goods_package('310000', '310100').json
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert resp.result.list[0].skuName == '嗨体功能水光+去颈纹css2'
        assert resp.result.total == 7

    @pytest.mark.run
    def test_query_merchant(self, merchantCode0='a89794a8-0691-4c24-ad91-41a737df3795'):
        """
        查询机构详情
        """
        resp = self.Peafowl.query_merchant(merchantCode0).to_json()
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert resp.result.merchantName == '外滩医美机构1外滩医美机构1外滩医美机构1外滩医美机构1外滩医美机构1外滩医美机构1外滩医美机构1外'
        assert resp.result.merchantAddress == '上海市黄浦区中山东一路'

    @pytest.mark.run
    def test_query_merchant_goods_package(self, merchantCode1='a89794a8-0691-4c24-ad91-41a737df3795'):
        """
        查询机构详情页的套餐--机构支持的套餐(商品)
        """
        resp = self.Peafowl.query_merchant_goods_package(merchantCode1).json
        assert resp.success is True
        assert resp['errorMsg'] == '成功'  # assert len(resp.result) == 7
        assert resp.result[0].skuName == '嗨体功能水光+去颈纹css2'
        assert resp.result[1].skuName == 'AOPT超光子嫩肤全模式-1次'

    @pytest.mark.run
    def test_get_area_info(self, provinceCode1='310000'):
        """
        查询当前城市定位
        """
        resp = self.Peafowl.get_area_info(provinceCode1).to_json()
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert resp.result[0].areaCode == '310100'
        assert resp.result[0].areaName == '上海市市辖区'

    @pytest.mark.run
    def test_get_order_list0(self):
        """
        查询医美'预约列表'-'全部'tab中，多选一权益的数据(15221466071用户的列表，数据2025-09-30过期)
        """
        resp = self.Peafowl.get_order_list0('peafowl', '1,2,14').json
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert resp.result[0]['interestsId'] == '2022093014574400001030000318681'
        assert resp.result[0].interestsNameShow == 'sun测试用医美主权益-1😄'
        assert resp.result[0].interestsCode == 'Z00140'
        assert resp.result[0].valid is False

    @pytest.mark.run
    def test_get_order_list1(self):
        """
        查询医美'预约列表'-'全部'tab中，第一页所有的普通权益的数据（未购买新权益时，数据都是2024-06-06过期）
        # 查看其他各tab的权益数据的接口不一一写了，因为只是[]中的入参不同而已，且后续用例会覆盖到
        """
        resp = self.Peafowl.get_order_list1(1, 10, []).to_json()
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert resp.result.list[0].interestsName == '嗨体功能水光'
        assert resp.result.list[7].interestsName == '嗨体功能水光'
        assert resp['result']['total'] == 8  # 测试账号15221466071未购买新权益的情况下，普通权益总数是8个

    @pytest.mark.run
    def test_add_appointment_user(self):
        """
        添加(15221466071账号的)预约人（为防止数据越来越多，每次新增后会清理）
        """
        resp = self.Peafowl.add_appointment_user('零七一自动化测试预约人六', 'FEMALE', '15221466071', '1995-10-10', 'RELA_WIFE').json
        assert resp.success is True
        assert resp.errorCode == '0'
        assert resp['errorMsg'] == '成功'
        sql_string1 = "update cif_patient_product.t_info_sufferer_base_info set usable_flag=%s where " \
                      "operator_id = '210003955790137' order by updated_at desc limit 1" % "'UN_USABLE'"  # 或"\"UN_USABLE\""
        # 或 "set usable_flag={} where xxx".format('\'UN_USABLE\'')      sql语句中，查询条件的内容两边需要加单引号或双引号
        st_db_info1 = get_db_info('../Test_Config/cfg_db.yaml', 'shantaijk_db1')  # 相对路径
        sql_execute_get_one(sql_string1, mode="update", **st_db_info1)  # mode仅为'select'时，可以不需要limit 1

    @pytest.mark.run
    def test_get_appointment_user(self):
        """
        查询(15221466071账号的)预约人列表 数据
        """
        resp = self.Peafowl.get_appointment_user().to_json()
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert resp.result[-1].name == 'sun自动化测试姓名'
        assert resp['result'][-1]['mobileNo'] == '15221466071'
        assert resp.result[-1].patientId == '260005036960010'

    @pytest.mark.run
    def test_update_appointment_user(self):
        """
        编辑(15221466071账号的)预约人：零七一自动化测试预约人（前端限制，只能更改手机号）
        """
        resp = self.Peafowl.update_appointment_user('零七一自动化测试预约人', 'FEMALE', '15221466072', '1995-09-09', '260005130310043').json
        assert resp.success is True
        assert resp['result'] is True
        assert resp.errorCode == '0'
        assert resp['errorMsg'] == '成功'

    @pytest.mark.run
    def test_query_merchant_list1(self):
        """
        查询'嗨体功能水光'权益 在'上海市市辖区'支持使用的医美机构
        """
        resp = self.Peafowl.query_merchant_list1("310100", "B01006", "31.159962", "121.433494").json
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert resp.result.total == 4
        assert resp.result.list[0].merchantName == '医美大美丽实体机构1'
        assert resp.result.list[3].merchantName == '金涛测试医美机构'

    @pytest.mark.run
    def test_get_reservation_date(self):
        """
        查询'外滩医美机构1外滩xxxx'机构的 可预约日期
        """
        resp = self.Peafowl.get_reservation_date('a89794a8-0691-4c24-ad91-41a737df3795').to_json()
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert len(resp['result']['appDateList']) is not 0
        assert isinstance(resp.result.appDateList, list)

    @pytest.mark.run
    def test_get_reservation_time(self):
        """
        查询'外滩医美机构1外滩xxxx'机构 2023-04-30的预约时间
        """
        resp = self.Peafowl.get_reservation_time('a89794a8-0691-4c24-ad91-41a737df3795', '2023-04-30').json
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert len(resp['result']['appointmentTimeList']) != 0
        assert isinstance(resp.result.appointmentTimeList, list)

    @pytest.mark.run
    def test_create_reservation_order(self):
        """
        创建'预约列表'-'待预约'tab中第一个权益的预约单（下下下个用例会调用'取消预约'接口，初始化该权益（取消后，新生成的该权益数据的id会变））
        peafowl.reservation_order_detail表
        """
        resp = self.Peafowl.get_order_list1(1, 10, ["init", "fail", "cancel"]).to_json()  # 与下下下个用例对比，此处不是直接引用其他用例，所以没问题
        interests_id0 = resp.result.list[0].id    # '待预约'tab中 第一个权益的id
        resp = self.Peafowl.create_reservation_order('a89794a8-0691-4c24-ad91-41a737df3795', '2023-07-31',
                                                     '09:00-10:00', '260005036960010', [{"id": interests_id0}]).json
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert resp.result[0].id == interests_id0
        assert resp.result[0].orderStatus == 'submitted'

    @pytest.mark.run
    def test_get_detail(self):
        """
        查询'预约列表'-'预约中'tab中 第一个权益的预约详情
        """
        resp = self.Peafowl.get_order_list1(1, 10, ["submitted", "confirm", "achieve"]).json  # or Peafowl()
        interests_id1 = resp.result.list[0].id    # '预约中'tab中 第一个权益的id
        resp = self.Peafowl.get_detail(interests_id1).to_json()  # or Peafowl()。下下个用例第一行用TestPeafowl()时，上上一行和此处若用self.Peafowl，下下个用例会报错，
        assert resp.success is True                            # 因为本用例作为方法被引用时，新类对象内部 引用不了自己的类(中的类对象、变量或方法)，会造成循环引用导致报错(
        assert resp['errorMsg'] == '成功'                       # self.Peafowl中的Peafowl会被当成方法去查找，会找不到这个方法)
        assert resp.result.orderStatus == 'submitted'
        assert resp.result.id == interests_id1
        return resp.result.id, resp['result']['merchantCode']

    @pytest.mark.run
    def test_get_patient_info(self):
        """
        点击查询 '预约中'tab中 第一个权益的预约详情的 '预约人'信息
        """
        interests_id2 = self.test_get_detail()[0]  # 把上一个用例当作方法使用，获得所需入参（前端也是这个原理）(or TestPeafowl().xxx)
        resp = self.Peafowl.get_patient_info(interests_id2).json
        assert resp.success is True
        assert resp['errorMsg'] == '成功'
        assert resp.result['appName'] == 'sun自动化测试姓名'
        assert resp.result.appTel == '15221466071'

    @pytest.mark.run
    def test_cancel_reservation_order(self):
        """
        取消预约 '预约中'tab中的第一个权益（有多个'待确认'状态的权益时，预约时间近的 排序更靠前）
        """
        result1 = self.test_get_detail()  # 用self时，上上个用例的第1、3行 中的self和此处的self都代表 本类对象，所以找 .peafowl属性 不会有问题
        interests_id3, merchantCode2 = result1[0], result1[1]
        resp = self.Peafowl.cancel_reservation_order(interests_id3, merchantCode2).to_json()
        assert resp.success is True
        assert resp.errorMsg == '成功'
        assert resp['result'] is not None
        print('取消后，新生成的该权益数据的id为：', resp.result)






