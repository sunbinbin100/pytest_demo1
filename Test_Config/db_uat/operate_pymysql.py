#!/usr/bin/python
# coding=utf-8

import os
import sys
import yaml
import pymysql      # import mysql.connector
from pithy import get_config
from pithy import pretty_print
from prettyprinter import cpprint
# from apis.env_url import Stjk_db        # 不注释，runDubbo运行会报错


def get_db_info(caller_file_path, database):
    """
    使用配置管理器，获取自定义的配置文件(默认为cfg.yaml)中，连接数据库所需的数据
    """
    try:
        confi = get_config(file_name=caller_file_path)  # '../'表示当前文件所在目录的父目录，即db_uat的父目录：Test_Config
        # print(os.path.exists('../Test_Config/cfg_db.yaml'))          # 为True时，不走pithy-cfg-Config类的路径2
        # 其他目录下的文件调用本方法时，找cfg_db.yaml位置的file_name路径值 是相对于 调用文件所在地 而言的
        # 此处为相对路径，故对于调用文件来说也可能不对（如：处于2个嵌套包内的operate_records文件）
        db_info = confi[database]     # ../cfg_db.yaml、../Test_Config/cfg_db.yaml
        return db_info                # dict。取值 例：host_values = db_info['host']
    except BaseException as e:
        raise e


def sql_execute_get_one(sql, mode="select", **db):
    """
    执行sql。非'select'时，须传参"mode"
    """
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
    """
    执行sql。非'select'时，须传参"mode"
    """
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

# print(Stjk_db.stjk_db_url)
# print(os.path.exists('../cfg_db.yaml'))        # 自定义路径，使得目录存在。不走pithy的Config类中 当前目录或根目录下是否有该文件的拼接、判断了
# cfg_db_yaml1 = open('../cfg_db.yaml')
# yaml1 = yaml.load(cfg_db_yaml1.read(), Loader=yaml.FullLoader)  # pithy里cfg.py line41 后续能以相对路径打开
# cfg_db_yaml1.close()
# pretty_print(yaml1)


if __name__ == '__main__':
    sql1 = "select * from efficient.qingniu_enterprise limit 2"
    db_info1 = get_db_info('../cfg_db.yaml', 'shantaijk_db')
    cpprint(sql_execute_get_all(sql1, **db_info1))



