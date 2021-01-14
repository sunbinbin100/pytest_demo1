#!/usr/bin/python
# coding=utf-8

import os
import sys
import yaml
import pymysql
from pithy import get_config
# import mysql.connector
from pithy import pretty_print
from apis.env_url import Kdd_db

print(Kdd_db.kdd_db_url)

# 获取配置管理器，使用自定义的配置文件(默认为cfg.yaml)
confi = get_config(file_name='../cfg_db.yaml')     # 拼接'../'表示当前文件所在目录的父目录，即db_uat的父目录-Test_Config
rddz_db_values = confi['rddz_db']
pretty_print(rddz_db_values)
# host_values = rddz_db_values['host']             # 其他类似

# print(os.path.exists('../cfg_db.yaml'))            # 直接使得目录存在，不走当前目录或根目录下是否有该文件的拼接、判断了
# yl = yaml.load(open('../cfg_db.yaml'), Loader=yaml.FullLoader)  # pithy里cfg.py line40 后续能以相对路径打开
# print(yl)


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
# print(sql_execute_get_one(sql1, **rddz_db_values))


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










