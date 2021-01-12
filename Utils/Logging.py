#! /usr/bin/python
# coding:utf-8

import logging
import time
# from reload import reload

# reload(sys)
# sys.setdefaultencoding("utf-8")

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] 【%(levelname)s】 %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=r".\Log\Service" + time.strftime(r'%Y-%m-%d', time.localtime(time.time())) + ".log",
                    filemode='a')
console = logging.StreamHandler()
logging.getLogger('suds.client').addHandler(console)


def writeLog(methodname, result):
    """写日志"""
    content = methodname + "\n"
    for item in result:
        content = content + '\t|' + str(item)
    if not result.Success:
        logging.error(content)


def writeException(msg):
    """写日志"""
    logging.error("【Catch Exception】" + str(msg))


















