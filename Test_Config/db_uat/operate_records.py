#!/usr/bin/python
# coding=utf-8
import records
from pithy import Config
from pithy import pretty_print
from pithy import DB             # pithy的sqlalchemy   pithy  __init__.py  from .db import DB


# 获取配置管理器
confi = Config(file_name='../cfg_db.yaml')     # 使用自定义的配置文件(默认为cfg.yaml)
rddz_db_values = confi['rddz_db']
pretty_print(rddz_db_values)
# host_values = rddz_db_values['host']         # 其他类似


# records实现数据库操作，生成数据库实例
mysqlurl = "mysql://rddz:re.dz@2019@10.0.1.237/kanduoduo?charset=utf8"
# records_db_object = records.Database(mysqlurl)
# print(records_db_object)


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





