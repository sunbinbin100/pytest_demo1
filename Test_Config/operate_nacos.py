#!/usr/bin/python
# coding=utf-8

import os, sys
import yaml, json, ast
import nacos
from pithy import Config
from prettyprinter import cpprint  # import mysql.connector
from pithy import pretty_print


def get_nacos_info(caller_file_path, database):
    """
    获取配置文件cfg_db.yaml中，连接Nacos所需的数据ßgit
    """
    if not isinstance(caller_file_path and database, str):
        return '------2个入参必须都为string------'
    else:
        conf = Config(file_name=caller_file_path)  # 获取配置管理器，使用自定义的配置文件(默认为cfg.yaml)
        # print(os.path.exists('../Test_Config/cfg_db.yaml'))       # 为True时，不走pithy-cfg-Config类的路径2
        # 其他目录下的文件调用本方法时，找cfg_db.yaml位置的file_name路径值 是相对于 调用文件所在地 而言的
        # 此处为相对路径，故对于调用文件来说也可能不对（如处于2个嵌套包内的operate_records文件）
        nacos_info = conf[database]
        return nacos_info  # dict类型。取值，例：host_values = db_info['host']


class GetNacosConfig(object):
    """
    连接Nacos，1、查询对应dubbo接口所属服务的IP和端口 2、查询配置文件内容
    """
    def __init__(self, serv_addr, ns, un, pw):
        self.client = nacos.NacosClient(server_addresses=serv_addr, namespace=ns, username=un, password=pw)  # 连接nacos

    def get_service_ip_and_port(self, service_name, clusters='DEFAULT', group='DEFAULT_GROUP', healthy_only=False):
        service_info = self.client.list_naming_instance(service_name, clusters=clusters, group_name=group,
                                                        healthy_only=healthy_only)      # 不只返回健康实例，都返回
        # 返回实例信息列表（各参数含义 见函数入参说明，后4个入参都可不写---namespace_id可不写是因为__init__里获取过了)
        service_ip = service_info['hosts'][0]['ip']   # service_info['hosts'][0]['instanceId']：实例ID，包含ip、port、集群、分组名、服务名
        service_port = service_info['hosts'][0]['port']
        return service_ip, service_port               # 列表，第一个是str，第二个是int

    def get_yaml_config(self, data_id, group='DEFAULT_GROUP'):
        conf = self.client.get_config(data_id, group=group)              # 获取dataId（某yaml配置文件的全名）的内容，结果为str
        dict_conf = yaml.load(conf, Loader=yaml.FullLoader)              # str转为dict（json.dumps(conf)，可转为json对象）
        return dict_conf                                                 # 返回结果类型为dict


"""
https://www.cnpython.com/pypi/nacos-sdk-python、https://blog.csdn.net/m0_53011633/article/details/125181628、https://www.cnblogs.com/wlj-axia/p/15639106.html
"""

# git reset HEAD <file>（git add . 了）
# git reset --hard commit_id（git commit -m 'xxx' 了）


if __name__ == '__main__':
    # print('有from apis.env_url import Stjk_db时，会运行2次')
    print(os.path.exists('./cfg_db.yaml'))  # 自定义路径，使得目录存在。不走pithy的Config类中 当前目录或根目录下是否有该文件的拼接、判断了
    # cfg_db_yaml = open('./cfg_db.yaml')
    # yaml1 = yaml.load(cfg_db_yaml.read(), Loader=yaml.FullLoader)  # pithy里cfg.py line41 后续能以相对路径打开
    # cfg_db_yaml.close()
    # cpprint(yaml1)

    nacos_info1 = get_nacos_info('cfg_db.yaml', 'shantaijk_nacos')  # 优先读取当前目录下。当前目录下存在cfg_db.yaml
    cpprint(nacos_info1)   # 某些数据类型用pretty_print会报错，故用cpprint更好




