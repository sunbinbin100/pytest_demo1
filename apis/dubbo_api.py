#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import nacos
import yaml
import requests
from pithy.api import request
from pithy import pretty_print
from prettyprinter import cpprint
from Test_Config import GetNacosConfig, get_nacos_info


class WorkerOrderDubbo(object):

    def __init__(self):
        # self.url = TestPeafowlConfig().test_peafowl_url
        pass

    def addWorkerOrder(self):
        """
        创建"电话问诊-视频转电话"工单
        """
        args1 = {'title': 'sun-Dubbo问诊工单13', 'intro': 'i\'m工单描述', 'operator': 210000282100143,
                 'source': 'WENZHEN_SYSTEM',
                 'priority': 'P1', 'category': 'DIANHUAWENZHEN', 'secondaryCategory': 'VIDEOTOTEL',
                 'currentAssignee': '210003954440127',
                 'imageKey': 'habasm-8301c16e0b1843369e523d7d6abedeca.jpeg,habasm-265a029b571247d4b68060bcefe4b220.jpeg',
                 'mobile': '15221466109', 'contactMobile': '15221466109', 'isReturnVisit': True,
                 'returnVisitTime': 1667198701000}


        result = conn.invoke('com.stjk.efficient.client.api.CallWorkOrderService', 'addWorkerOrder',
                             json.dumps(args1))  # result=conn.do('ls')
        cpprint(result)
        conn.close()  # telnetlib自带的断开连接。也可以自定义一个方法：self.write(b"exit\n")







stNacInfo = get_nacos_info()

stServerAddr = stNacInfo['server_addresses']
stNamespaceId = stNacInfo['namespaceId']
stNacUsername, stNacPassword = stNacInfo['username'], stNacInfo['password']
serviceName, dataId = "providers:com.stjk.efficient.client.api.CallWorkOrderService", "elsa.yaml"  # 服务名和配置文件名

STJKNacosConfig = GetNacosConfig(stServerAddr, stNamespaceId, stNacUsername, stNacPassword)  # 类变量
cpprint(STJKNacosConfig.get_yaml_config(dataId))
# ip_and_port = STJKNacosConfig.get_service_ip_and_port(serviceName)
# print(ip_and_port)
# conne = RunDubbo(ip_and_port[0], ip_and_port[1])  # Nacos查询efficient:服务管理-服务列表，'服务名称'处搜索 effi，可找到IP和端口
# print(conne)





