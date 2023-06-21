#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import nacos
import yaml, ast
from pithy import pretty_print
from prettyprinter import cpprint
from apis import WorkerOrderDubbo
from Test_Config.db_uat import get_db_info, sql_execute_get_one
from Test_Config import get_nacos_info, GetNacosConfig
from Utils import RunDubbo

stNacInfo = get_nacos_info('../Test_Config/cfg_db.yaml', 'shantaijk_nacos')  # 在本文件中，查找cfg_db.yaml的相对路径
stServerAddr, stNamespaceId = stNacInfo['server_addresses'], stNacInfo['namespaceId']
stNacUsername, stNacPassword = stNacInfo['username'], stNacInfo['password']
STJKNacosConfig = GetNacosConfig(stServerAddr, stNamespaceId, stNacUsername, stNacPassword)  # 类对象


class TestWorkerOrderDubbo(object):

    def setup(self):
        """
        初始化接口
        """
        self.WorkerOrderDubbo = WorkerOrderDubbo()       # 1次初始化为类对象，供各用例重复使用，避免各用例重复调用WorkerOrderDubbo()类
        # self.RunDubbo = RunDubbo                       # 1次初始化为类变量（RunDubbo类需要有2个参数），供重复使用
        ip_and_port = STJKNacosConfig.get_service_ip_and_port("providers:com.stjk.efficient.client.api.CallWorkOrderService")
        self.conn = RunDubbo(ip_and_port[0], ip_and_port[1])  # 类对象
        self.title = "\"sun-Dubbo问诊工单20\""  # 或"'xxx'"。sql语句中，查询条件的内容两边需要加单引号或双引号。第一个用例中引用时，须去除两边的引号(使操作的是同一数据)

    def test_add_worker_order(self):
        """
        创建"电话问诊-视频转电话"工单
        """
        json_args = self.WorkerOrderDubbo.add_worker_order(ast.literal_eval(self.title), 1687246187000)  # 2023-06-20 15:29:47
        resp = self.conn.invoke('com.stjk.efficient.client.api.CallWorkOrderService', 'addWorkerOrder', json_args)
        cpprint(resp)
        assert resp['errorCode'] == '0'
        assert resp['errorMsg'] == '成功'
        assert resp['success'] is True

    def test_accept_worker_order(self):      # 受理上一个用例运行成功后，新建的工单
        """
        受理工单（为'已解决'）
        """
        sql_string = 'select * from efficient.kefu_worker_order where title=%s order by update_at desc' % self.title
        # where title={} order by update_at desc'.format('\'sun-Dubbo问诊工单18\'')
        st_db_info = get_db_info('../Test_Config/cfg_db.yaml', 'shantaijk_db')  # 相对路径
        order_id = sql_execute_get_one(sql_string, **st_db_info)['id']      # int。mode仅为'select'时，可以不需要limit 1
        json_args = self.WorkerOrderDubbo.accept_worker_order(order_id)
        resp = self.conn.invoke('com.stjk.efficient.client.api.CallWorkOrderService', 'accept', json_args)
        cpprint(resp)
        assert resp['errorCode'] == '0'
        assert resp['errorMsg'] == '成功'
        assert resp['result'] and resp['success'] is True













