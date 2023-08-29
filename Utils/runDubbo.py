#!/usr/bin/python
# coding:utf-8

import socket
import json, re, ast
import telnetlib
from pithy import pretty_print, make_session
from prettyprinter import cpprint
# from pyhessian.client import HessianProxy   # from pyhessian import protocol
from Test_Config import get_nacos_info, GetNacosConfig                   # 顺序在apis包后
from Test_Config.db_uat.operate_pymysql import sql_execute_get_one, get_db_info


class RunDubbo(telnetlib.Telnet):
    prompt, coding = 'dubbo>', 'utf-8'

    def __init__(self, host=None, port=0, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.write(b'\n')                      # 模拟命令行输入telnet xx.xx.xxx.xxx xxxxx命令后，回车

    def command(self, flag, str_=""):          # 模拟命令行输入 具体的命令
        data = self.read_until(flag.encode())  # ☆☆☆读取上一次命令执行后返回的内容（内容包括：elapsed: 33 ms.\r\ndubbo>）
        self.write(str_.encode() + b"\n")      # 输入新的命令(str_的值)并回车执行。   若再次调用本方法，可读取本次调用的结果（本次连接未关闭的情况下）
        return data

    def invoke(self, service_name, method_name, arg1=''):      # 接口的入参 arg1 默认为空或dict
        # if isinstance(arg1, (dict,)):
        #     arg1 = json.dumps(arg1)                # Dubbo接口入参须为json格式
        command_str = "invoke {0}.{1}({2})".format(service_name, method_name, arg1)  # 服务名.方法名(入参)，服务名包括接口名interface
        self.command(self.prompt, command_str)       # 也可以写成：RunDubbo.prompt
        data = self.command(RunDubbo.prompt, "此句是本方法的最后1个命令语句，但是此句随便输入什么，不影响，因为下一行断开连接了，所以此句命令的运行结果不会被读取到")
        # 结果data，为bytes类型，且有\r光标起始换行和\n
        self.close()                  # Telnet自带的断开连接。也可以写为：self.write(b"exit\n")。所以每次调用本方法，都是1个新的连接（新的子进程）
        # ☆close方法不能放在两次调用command方法的代码中间，因为第二次调用command后，才获取到了第一次调用command后的数据（第一次调用command后，是没有结果的）
        data = data.decode(self.coding, errors='ignore').split('\n')[0].strip()     # 去除首尾空格（\r也算空格），也可.split('\r')[0]
        # data = re.findall(r'(.*)', data)[0]       # 取第一部分，末尾有\r
        return json.loads(data)                     # json格式(str，单引号里包的双引号格式的字典) 反序列化为 字典
        # 因为有 "success":true ，所以不能用eval()和ast.literal_eval()

    def do(self, arg2):
        """
        执行非invoke命令，如ls、ls 服务名、ls -l、ls -l 服务名等
        """
        command_str1 = arg2
        self.command(self.prompt, command_str1)
        data = self.command(self.prompt, "此句是本方法的最后1个命令语句，但是此句随便输入什么，不影响，因为下一行断开连接了，所以此句命令的运行结果不会被读取到")
        self.write(b"exit\n")         # or：self.close()。断开连接，所以每次调用本方法，也都是1个新的连接（新的子进程）
        data = data.decode(RunDubbo.coding, errors='ignore')  # data是运行了line44后获得的结果，而不是line45
        return data             # 如'ls'，结果为：'com.stjk.efficient.client.api.CallWorkOrderService\r\ndubbo>'


"""
https://cloud.tencent.com/developer/article/2071960、https://blog.csdn.net/software_test010/article/details/121215418、
https://article.itxueyuan.com/jlMvKA、https://www.136.la/jingpin/show-26913.html、
https://www.jianshu.com/p/d6b32fcb9b83、https://www.cnblogs.com/watery/p/13452914.html
工单创建、受理-接口文档：
https://thoughts.aliyun.com/workspaces/5fbb5e916b9dce0024029df0/docs/634cd429c2b4fd0001fb0aa7
"""
# https://www.jianshu.com/p/40968685dcd6、https://cloud.tencent.com/developer/article/1564629


if __name__ == '__main__':
    sql1 = "select * from efficient.qingniu_enterprise limit 1"
    nacos_info2 = get_nacos_info('../Test_Config/cfg_db.yaml', 'shantaijk_nacos')
    print(nacos_info2)

    # aa = '{"callId":"callId","errorMsg":"成功","result":153280,"success": True}'
    # print(ast.literal_eval(aa), type(ast.literal_eval(aa)))  # dict
    # print(json.dumps(ast.literal_eval(aa)), type(json.dumps(ast.literal_eval(aa))))  # str，json格式


