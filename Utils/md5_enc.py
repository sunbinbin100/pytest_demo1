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


def get_md5(pw):
    return hashlib.md5(str(pw).encode("UTF-8")).hexdigest() if pw is not None else None


# if __name__ == '__main__':
#     print(get_md5(123456))







