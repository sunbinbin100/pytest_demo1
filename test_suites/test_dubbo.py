#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import nacos
import yaml
from pithy import pretty_print
from prettyprinter import cpprint
from Test_Config import GetNacosConfig, get_nacos_info






def addWorkerOrder():  # 创建"电话问诊-视频转电话"工单
    args1 = {'title': 'sun-Dubbo问诊工单13', 'intro': 'i\'m工单描述', 'operator': 210000282100143, 'source': 'WENZHEN_SYSTEM',
             'priority': 'P1', 'category': 'DIANHUAWENZHEN', 'secondaryCategory': 'VIDEOTOTEL', 'currentAssignee': '210003954440127',
             'imageKey': 'habasm-8301c16e0b1843369e523d7d6abedeca.jpeg,habasm-265a029b571247d4b68060bcefe4b220.jpeg',
             'mobile': '15221466109', 'contactMobile': '15221466109', 'isReturnVisit': True, 'returnVisitTime': 1667198701000}
    result = conn.invoke('com.stjk.efficient.client.api.CallWorkOrderService', 'addWorkerOrder', json.dumps(args1))  # result=conn.do('ls')
    cpprint(result)
    conn.close()  # telnetlib自带的断开连接。也可以自定义一个方法：self.write(b"exit\n")


def acceptWorkerOrder(order_id):  # 受理工单
    args2 = {'id': order_id, 'operator': '210002043170144', 'status': 'SOLVE', 'currentAssignee': '210002043170144',
             'intro': 'I\'m受理说明', 'imageKey': '', 'contactMobile': '', 'isReturnVisit': False,
             'isAdmin': True}
    result = conn.invoke('com.stjk.efficient.client.api.CallWorkOrderService', 'accept', json.dumps(args2))
    cpprint(result)
    conn.close()


# addWorkerOrder()
# acceptWorkerOrder(153032)
# print(conn.do('ls -l'))












# def AddWorkerOrderReq(service, interface, method, req, retcode='000000'):
#     url = 'http://10.19.125.66:20880/' + service + '.' + interface
#     print('URL:\t%s' % url)
#     print('Method:\t%s' % method)
#     print('Req:\t%s' % req)
#     res = getattr(HessianProxy(url), method)(req)
#     print('Res:\t%s' % json.dumps(res, ensure_ascii=False))
#
#
# if __name__ == '__main__':
#     service = 'com.stjk.efficient.client.api'  # 服务名：providers:com.stjk.efficient.client.api.CallWorkOrderService
#     interface = 'CallWorkOrderService'  # 为service的一部分，接口：com.stjk.efficient.client.api.CallWorkOrderService
#     method = 'addWorkerOrder'
#     req = protocol.object_factory('com.stjk.efficient.client.req.addWorkerOrder', operator='210000282100143',
#                                   source='WENZHEN_SYSTEM', currentAssignee=210003954440127, isReturnVisit=False)
#     AddWorkerOrderReq(service, interface, method, req)
# # https://www.jianshu.com/p/40968685dcd6、https://cloud.tencent.com/developer/article/1564629





