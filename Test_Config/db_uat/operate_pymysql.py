#!/usr/bin/python
# coding=utf-8

import os
import sys
import yaml
import pymysql      # import mysql.connector
from pithy import get_config
from pithy import pretty_print
from prettyprinter import cpprint
from apis.env_url import Stjk_db

print(Stjk_db.stjk_db_url)


def get_db_info():
    """使用配置管理器，获取自定义的配置文件(默认为cfg.yaml)中，连接数据库所需的数据"""
    confi = get_config(file_name='../cfg_db.yaml')     # 拼接'../'表示当前文件所在目录的父目录，即db_uat的父目录：Test_Config
    db_info = confi['shantaijk_db']
    return db_info                     # dict。取值，例：host_values = db_info['host']


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
        cursor.close()           # 需关闭操作数据库的游标
        conn.close()             # 最后关闭链接


def sql_execute_get_all(sql, mode="select", **db):
    conn = pymysql.connect(cursorclass=pymysql.cursors.DictCursor, **db)
    cursor = conn.cursor()
    try:
        if mode == "select":
            cursor.execute(sql)
            result = cursor.fetchall()            # 返回一个list
            return result if result else None
        else:
            cursor.execute(sql)
            conn.commit()
    finally:
        cursor.close()
        conn.close()


print(os.path.exists('../cfg_db.yaml'))        # 自定义路径，使得目录存在。不走pithy的Config类中 当前目录或根目录下是否有该文件的拼接、判断了
yaml1 = yaml.load(open('../cfg_db.yaml'), Loader=yaml.FullLoader)  # pithy里cfg.py line41 后续能以相对路径打开
pretty_print(yaml1)


# if __name__ == '__main__':
#     sql1 = "select * from efficient.qingniu_enterprise limit 3"
#     cpprint(sql_execute_get_all(sql1, **get_db_info()))







