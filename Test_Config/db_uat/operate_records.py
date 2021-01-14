#!/usr/bin/python
# coding=utf-8
import records
from pithy import Config
from pithy import pretty_print
from apis.env_url import Kdd_db
from pithy import DB             # pithy的sqlalchemy   pithy  __init__.py  from .db import DB


# 获取配置管理器，使用自定义的配置文件(默认为cfg.yaml)
confi = Config(file_name='../cfg_db.yaml')     # 拼接'../'表示当前文件所在目录的父目录，即db_uat的父目录-Test_Config
rddz_db_values = confi['rddz_db']
pretty_print(rddz_db_values)
# host_values = rddz_db_values['host']         # 其他类似

# print(os.path.exists('../cfg_db.yaml'))            # 直接使得目录存在，不走当前目录或根目录下是否有该文件的拼接、判断了
# yl = yaml.load(open('../cfg_db.yaml'), Loader=yaml.FullLoader)  # pithy里cfg.py line40 后续能以相对路径打开
# print(yl)


# records实现数据库操作，生成数据库实例
mysqlurl1 = Kdd_db.kdd_db_url
mysqlurl = "mysql://rddz:re.dz@2019@10.0.1.237/kanduoduo?charset=utf8"
print(bool(mysqlurl1 == mysqlurl))
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







