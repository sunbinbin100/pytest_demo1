#!/usr/bin/python
# coding:utf-8

import socket
import json, re
import telnetlib
from Test_Config import GetNacosConfig, get_nacos_info
from pithy import pretty_print, make_session
from prettyprinter import cpprint
# from pyhessian.client import HessianProxy
# from pyhessian import protocol


class RunDubbo(telnetlib.Telnet):
    prompt, coding = 'dubbo>', 'utf-8'

    def __init__(self, host=None, port=0, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.timeout = timeout
        self.write(b'\n')

    def command(self, flag, str_=""):          # 命令行输入
        data = self.read_until(flag.encode())  # 读取上一次命令执行后返回的内容（内容包括自己本身）
        self.write(str_.encode() + b"\n")      # 输入新的命令str_并回车执行，下次执行本方法后 可读取本次执行的结果
        return data

    def invoke(self, service_name, method_name, arg1=''):      # 接口的入参 arg1 默认为空或dict
        # if isinstance(arg1, (dict,)):
        #     arg1 = json.dumps(arg1)                # Dubbo接口入参须为json格式
        command_str = "invoke {0}.{1}({2})".format(service_name, method_name, arg1)  # 服务名.方法名(入参)，服务名包括接口名
        self.command(self.prompt, command_str)       # 也可以写成：RunDubbo.prompt
        data = self.command(RunDubbo.prompt, "")     # 结果为bytes类型，且有\r光标起始换行和\n
        data = data.decode(self.coding, errors='ignore').split('\n')[0].strip()  # 去除首尾空格（\r也算空格），也可.split('\r')[0]
        return json.loads(data)                      # 反序列化为python对象
        # data = re.findall(r'(.*)', data)[0]       # 取第一部分，末尾有\r  # return json.loads(data.strip())  # 去除\r，再转为python对象

    def do(self, arg2):
        """
        执行非invoke命令，如ls、ls 服务名、ls -l、ls -l 服务名等
        """
        command_str1 = arg2
        self.command(self.prompt, command_str1)
        data = self.command(self.prompt, "随便什么内容，作为下一个命令--但每次运行都是新的，所以不影响")
        data = data.decode(RunDubbo.coding, errors='ignore')
        return data


"""
https://article.itxueyuan.com/jlMvKA、https://www.136.la/jingpin/show-26913.html、https://cloud.tencent.com/developer/article/2071960
https://www.jianshu.com/p/d6b32fcb9b83、https://blog.csdn.net/software_test010/article/details/121215418
工单创建、受理-接口文档：
https://thoughts.aliyun.com/workspaces/5fbb5e916b9dce0024029df0/docs/634cd429c2b4fd0001fb0aa7
"""

