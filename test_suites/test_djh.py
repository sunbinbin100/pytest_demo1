#!/usr/bin/python
# coding=utf-8

import os
import pytest
import allure
from pithy import Config
from apis import DJHLogin     # from apis.djh_login_api import DJHLogin  # 使用绝对路径导入
from Utils import calc_md5
from pithy import pretty_print


class TestDJHLogin(object):
    user_info = [(15221466224, 123456)]

    def setup(self):
        """
        初始化接口
        """
        self.DJHLogin = DJHLogin()

    # @Title('电竞虎登录接口')                             # Allure功能，报告的case显示标题
    # @pytest.mark.parametrize("x", [1, 2, 3])           # 参数组合
    @pytest.mark.parametrize("userinfo", user_info)      # 参数化
    @pytest.mark.run
    def test_djh_login(self, userinfo):
        """
        测试电竞虎登录接口(post)
        """
        resp = self.DJHLogin.djh_login(userinfo[0], userinfo[1]).to_json()  # .to_json()==.json
        assert resp.notice == '登陆成功'
        assert resp['status'] == 200                        # 通过字典形式取值
        assert resp.info.nickname == '帆布'                  # 通过点号取值
        assert resp('$.info.username') == '15221466224'     # 通过object path取值
        # allure测试报告相关
        allure.attach('<body>allure.attach测试文本text111111</body>', name='html测试块，名称可省略', attachment_type=allure.attachment_type.HTML)
        allure.attach.file('/Users/sunbinbin/Desktop/测试用文件/日结.png', name='日结图片', attachment_type=allure.attachment_type.JPG)           # .file

    @pytest.mark.run
    @pytest.mark.timeout(60)                             # 限定60s超时
    def test_djh_personal_center(self):
        """
        测试电竞虎个人中心接口(get)
        """
        resp = self.DJHLogin.djh_personal_center('home', 'memberNew', 'center').json
        assert resp['notice'] == '获取成功'
        assert resp.status == 200
        assert resp('$.info.user_info.email') == '1***@qq.com'
        assert resp.info.user_info.username == '152****6224'
        allure.attach('allure.attach测试文本text222222', name='text文本', attachment_type=allure.attachment_type.TEXT)


# if __name__ == '__main__':
#     pytest.main(['test_djh.py', '-v', '--alluredir', 'rpt1/xml', '--clean-alluredir'])
#     # allure generate rpt1/xml -o rpt1/html --clean
#     pytest.main('allure open -h 127.0.0.1 -p 8883 rpt1/html')





# git reset HEAD <file>（git add . 了）
# git reset --hard commit_id（git commit -m 'xxx' 了）

