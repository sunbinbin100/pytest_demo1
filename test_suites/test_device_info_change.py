#!/usr/bin/python
# coding:utf-8

import pytest
from pithy import Config
from apis import DeviceInfoChange  # from apis.device_info_change_api import DeviceInfoChange    # 使用绝对路径导入
from pithy import pretty_print


class TestDeviceInfoChange(object):
    """
    device接口服务
    """
    def setup(self):
        """
        初始化接口
        """
        self.DeviceInfoChange = DeviceInfoChange()
        self.base_url = Config()['rddz_db']

    @pytest.mark.run                  # pytest-ordering插件
    def test_get_pro_token(self):
        """
        获取线上配置后台登录时的token
        """
        resp = self.DeviceInfoChange.get_pro_token("sunbinbin", "b191415770").to_json()
        pro_token = resp['data']['token']
        assert isinstance(pro_token, str)
        assert pro_token
        # pretty_print(self.base_url)
        return pro_token  # unicode

    @pytest.mark.run
    def test_device_info_clear(self):
        """
        线上清除、刷新设备信息
        """
        token = self.test_get_pro_token()  # unicode，若token为json对象需处理为python对象后再作为参数，否则会变为""xxx""
        resp = self.DeviceInfoChange.device_info_clear(token).to_json()
        assert resp.message == u'成功'

    @pytest.mark.run
    def test_device_info_get(self):
        """
        线上清除设备信息后，查看设备信息
        """
        token = self.test_get_pro_token()
        resp = self.DeviceInfoChange.device_info_get(token).to_json()
        assert resp['message'] == u'成功'
