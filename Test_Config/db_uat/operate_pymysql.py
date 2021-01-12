#!/usr/bin/python
# coding=utf-8
import os
import sys

import pymysql
from pithy import get_config
# import mysql.connector
from pithy import pretty_print

# from cfg import test_kdd

# 获取配置管理器
confi = get_config(file_name='../cfg_db.yaml')     # 使用自定义的配置文件(默认为cfg.yaml)
rddz_db_values = confi['rddz_db']
pretty_print(rddz_db_values)
# host_values = rddz_db_values['host']         # 其他类似

# print(os.path.exists('../cfg_db.yaml'))            # 直接使得目录存在，不走当前目录或根目录下是否有该文件的拼接、判断了
# print(os.path.join(sys.path[0], 'cfg_db.yaml'))
# print(os.path.join(sys.path[1], 'cfg_db.yaml'))


def sql_execute_get_one(sql, mode="select", **db):
    conn = pymysql.connect(cursorclass=pymysql.cursors.DictCursor, **db)
    cursor = conn.cursor()
    try:
        if mode == "select":
            cursor.execute(sql)
            result = cursor.fetchone()            # 只取一条，fetchall时返回list
            return result if result else None
        else:
            cursor.execute(sql)
            conn.commit()
    finally:
        cursor.close()
        conn.close()


# sql1 = "select * from album limit 3"
# print(sql_execute_get_one(sql1, **rddz_db))


def sql_execute_get_all(sql, mode="select", **db):
    conn = pymysql.connect(cursorclass=pymysql.cursors.DictCursor, **db)
    cursor = conn.cursor()
    try:
        if mode == "select":
            cursor.execute(sql)
            result = cursor.fetchall()
            return result if result else None
        else:
            cursor.execute(sql)
            conn.commit()
    finally:
        cursor.close()
        conn.close()







