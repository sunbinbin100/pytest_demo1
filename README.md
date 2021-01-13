    ├─pytest_demo1
    ├── apis
    ├── rpt
    │   ├── html111
    │   └── xml111
    ├── Test_Config
    │   ├── __init__.py
    │   ├── cfg_db.yaml
    │   └── db_uat
    │       ├── __init__.py
    │       ├── operate_pymysql.py
    │       ├── operate_records.py
    │       └── redis_client.py
    ├── test_suites
    ├── Utils
    │   ├── __init__.py
    │   ├── Logging.py
    │   ├── getCookies.py
    │   └── md5_enc.py
    ├── env.cfg
    ├── README.MD
    └── requirements.txt


* pithy调用requests更加简洁，在调用时还能够打印出输入和输出的参数，方便调试
* 参考链接：[基于 python 的接口自动化测试](https://mp.weixin.qq.com/s?__biz=MzIwNjEwNTQ4Mw%3D%3D&mid=2651577106&idx=1&sn=4c3e7f3a3090fea19ef48d24cdb5211f)<br>
        [pithy-test的github](https://github.com/yuyu1987/pithy-test)<br>
        [pithy-test用户手册](https://pithy-test.readthedocs.io/en/latest/index.html)
* thriftpy文件有缺失，需要用的话需要去找一下


* cfg.yaml —— appid的配置信息
* cfg_db.yaml —— 数据库连接信息
* env_url —— 接口url信息
* env.cfg —— 环境配置，用于切换环境
* config.py —— 配置驱动脚本（暂未添加）





