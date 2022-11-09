#!/usr/bin/python
# coding=utf-8

import os

import records
import mysql.connector  # import MySQLdb
import yaml
from pithy import get_config
from pithy import pretty_print
from apis.env_url import Stjk_db

# 获取配置管理器，使用自定义的配置文件(默认为cfg.yaml)
conf = get_config(file_name='../cfg_db.yaml')     # 拼接'../'表示当前文件所在目录的父目录，即db_uat的父目录：Test_Config
stjk_db_values = conf['shantaijk_db']
pretty_print(stjk_db_values)      # dict。取值，例：host_values = stjk_db_values['host']

print(os.path.exists('../cfg_db.yaml'))        # 自定义路径，使得目录存在。不走pithy的Config类中 当前目录或根目录下是否有该文件的拼接、判断了
yaml2 = yaml.load(open('../cfg_db.yaml'), Loader=yaml.FullLoader)  # pithy里cfg.py line41 后续能以相对路径打开
pretty_print(yaml2)


# records实现数据库操作，生成数据库实例
# mysqlurl1 = Stjk_db.stjk_db_url
# records_db_object = records.Database(mysqlurl1)
# print(records_db_object)                          # ModuleNotFoundError: No module named 'MySQLdb'


# 定义一些数据库查询(示例：)
# def get_user_id(username):
#     """
#     根据用户名获取用户ID
#     """
#     rows = records_db_object.query("select * from user where username=:username", username=username)
#     print(rows)                                # 默认返回封装的RecordCollection对象
#     print(rows.first(as_dict=True))            # 以字典的形式获取第一条数据
#     print(rows.all(as_ordereddict=True))       # 以排序字典的形式获取全部数据
#     return rows[0].id


# if __name__ == '__main__':
#     print(get_user_id('pithy'))







