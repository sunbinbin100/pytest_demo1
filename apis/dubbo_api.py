#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
# import nacos
# import yaml
# import requests
# from pithy.api import request
# from pithy import pretty_print
# from prettyprinter import cpprint
# from apis import TestPeafowlConfig
# from Test_Config import get_nacos_info, GetNacosConfig
# from Utils import RunDubbo


class WorkerOrderDubbo(object):

    def __init__(self):
        # self.url = TestPeafowlConfig.test_peafowl_url
        self.operator = 210000282100143   # staff, 15221466224

    def add_worker_order(self, title, returnVisitTime):
        """
        创建"电话问诊-视频转电话"工单
        """
        args = {'title': title, 'intro': 'i\'m工单描述', 'operator': self.operator, 'source': 'WENZHEN_SYSTEM',
                'priority': 'P1', 'category': 'DIANHUAWENZHEN', 'secondaryCategory': 'VIDEOTOTEL',
                'currentAssignee': '210003954440127', 'imageKey': 'habasm-8301c16e0b1843369e523d7d6abedeca.jpeg',
                'mobile': '15221466109', 'contactMobile': '15221466109',
                'isReturnVisit': True, 'returnVisitTime': returnVisitTime}
        return json.dumps(args)        # invoke入参要求为json格式

    def accept_worker_order(self, order_id):
        """
        受理工单
        """
        args = {'id': order_id, 'operator': self.operator, 'status': 'SOLVE', 'currentAssignee': '210002043170144',
                'intro': 'I\'m受理说明', 'imageKey': '', 'contactMobile': '', 'isReturnVisit': False, 'isAdmin': True}
        return json.dumps(args)










