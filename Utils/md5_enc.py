#!/usr/bin/python
# coding=utf-8

import hashlib

"""
密码md5加密，用于传参加密后的密码
"""


def calc_md5(pw):
    md = hashlib.md5()
    md.update(str(pw).encode('utf-8'))
    return md.hexdigest()                            # 返回16进制密文


# if __name__ == '__main__':
#     print(calc_md5(123456))






