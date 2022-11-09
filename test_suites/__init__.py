#!/usr/bin/python
# coding=utf-8


"""----------pithy使用说明（部分）---------"""

# 解析json字符,输出为字典    response = post('test').to_json()
# 解析json字符,输出为字典    response = post('test').json
# 输出为字符串              response = post('test').to_content()
# 输出为字符串              response = post('test').content
# 输出cookie对象            response = post('test').get_cookie()(或已废弃)
# 输出cookie对象            response = post('test').cookies       （结果为RequestsCookieJar，取值方法和dict一样）

# 结果取值, 假设response = {'a': 1, 'b': { 'c': [1, 2, 3, 4]}}
# print(response['b']['c'])          # 和字典一样取值
# print(response.b.c)                # 通过点号取值，结果为[1, 2, 3, 4]
# print(response('$.a'))             # 通过object path取值，结果为1
# for i in response('$..c[@>3]'):    # 通过object path取值，结果为选中 以c为key的字典 里大于3的所有元素


"""
# pithy调用requests更加简洁，在调用时还能够打印出输入和输出的参数，方便调试
# 参考链接：https://mp.weixin.qq.com/s?__biz=MzIwNjEwNTQ4Mw%3D%3D&mid=2651577106&idx=1&sn=4c3e7f3a3090fea19ef48d24cdb5211f
# thriftpy文件有缺失，需要用的话需要去找一下

# cfg.yaml     ---  appid的配置信息
# cfg_db.yaml  ---  数据库链接 和 Nacos链接相关信息
# env_url      ---  各环境接口url信息
# env.cfg      ---  环境配置，用于切换环境
# config.py    ---  配置驱动脚本（暂未添加）

# run4jenkins.py —— 供Jenkins执行时调用，能够并发执行测试用例，并且有失败重试机制
"""
















