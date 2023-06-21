#!/usr/bin/python
# coding=utf-8

import os
import records
import mysql.connector  # import MySQLdb
import yaml
from pithy import get_config
from pithy import pretty_print
from prettyprinter import cpprint
# from apis.env_url import Stjk_db


def get_db_info1(caller_file_path, database):
    """
    使用配置管理器，获取自定义的配置文件(默认为cfg.yaml)中，连接数据库所需的数据
    """
    try:
        confi = get_config(file_name=caller_file_path)  # '../'表示当前文件所在目录的父目录，即db_uat的父目录：Test_Config
        # print(os.path.exists('../Test_Config/cfg_db.yaml'))          # 为True时，不走pithy-cfg-Config类的路径2
        # 其他目录下的文件调用本方法时，找cfg_db.yaml位置的file_name路径值 是相对于 调用文件所在地 而言的
        # 此处为相对路径，故对于调用文件来说也可能不对（如：处于2个嵌套包内的operate_records文件）
        db_info = confi[database]     # ../cfg_db.yaml、../Test_Config/cfg_db.yaml
        return db_info                # dict。取值，例：host_values = db_info['host']
    except BaseException as e:
        raise e


# # records实现数据库操作，生成数据库实例
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


if __name__ == '__main__':
    print(get_db_info1('../cfg_db.yaml', 'shantaijk_db'))
    # print(get_user_id('pithy'))










