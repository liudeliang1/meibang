"""
=============================
Author:'Dayle'
Time:2021/4/26
E-mail:39072149@qq.com
=============================
"""
import time
import pytest

from lxml import etree
from data.scene_data import scene_success_data
from common.conifg import myconf
from common.mylogger import log
from common.text_replace import ConText, da_replace

"""
场景案例-主流程
--开单->排单->下单->消耗->结算->

"""


@pytest.mark.scene
class TestOrderTask:
    # 登录
    @pytest.mark.parametrize("test_info", scene_success_data)
    def test_login_task(self, test_info, init_http):
        """登录接口"""
        # 定义http_requests
        http = init_http
        url = myconf.get('url', 'url') + "/clients/login"
        # 接口请求
        log.info('正在请求地址{}'.format(url))
        response = http.request(method=test_info["method"], url=url, data=test_info["login_data"])
        print(response)
        try:
            tree = etree.HTML(response.text)
            sx = tree.xpath("//li[contains(@class,'active')]//a//span")
            sy = sx[0].text
            assert sy == "首页"
            print("登录成功！")
        except AssertionError as e:
            print("登录失败！")

    # 开单
    @pytest.mark.parametrize("test_info", scene_success_data)
    def test_add_task(self, test_info, init_http):
        """开单"""
        # 定义http_requests
        http = init_http
        url = myconf.get('url', 'url') + "/clients/bookingInfo/createNewBooking"
        # 接口请求
        log.info('正在请求地址{}'.format(url))
        add_data = test_info["add_data"]
        log.info('正在请求报文{}'.format(add_data))
        response = http.request(method=test_info["method"], url=url, json=add_data)
        res = response.json()
        print(res)
        code = res["stateCode"]
        try:
            # 【校验响应结果】
            assert str(code) == test_info["expected"]
        except AssertionError as e:
            # 用例执行未通过
            log.info('【{}】:用例执行未通过'.format(test_info["title"]))
            log.exception(e)
            raise e
        else:
            # 用例执行通过
            log.info('【{}】:用例执行通过'.format(test_info["title"]))
            # 保存订单
            res_data = res["data"]
            kd_id = res_data["id"]
            # 存储订单id
            setattr(ConText, "kd_id", kd_id)

    # 排单
    @pytest.mark.parametrize("test_info", scene_success_data)
    def test_assign_task(self, test_info, init_http):
        """排单"""
        # 定义http_requests
        http = init_http
        url = myconf.get('url', 'url') + "/clients/bookingInfo/createNewBookingArrange"
        data = str(test_info["pd_data"])
        # 替换上个接口的响应单号
        new_data = da_replace(data, ["kd_id", ])
        new_data = eval(new_data)
        # 接口请求
        log.info('正在请求地址{}'.format(url))
        log.info('正在请求报文{}'.format(new_data))
        response = http.request(method=test_info["method"], url=url, json=new_data)
        res = response.json()
        print(res)
        code = res["stateCode"]
        try:
            # 【校验响应结果】
            assert str(code) == test_info["expected"]
        except AssertionError as e:
            # 用例执行未通过
            log.info('【{}】:用例执行未通过'.format(test_info["title"]))
            log.exception(e)
            raise e
        else:
            # 用例执行通过
            log.info('【{}】:用例执行通过'.format(test_info["title"]))

    # 结算
    @pytest.mark.parametrize("test_info", scene_success_data)
    def test_close_task(self, test_info, init_http):
        """排单"""
        # 定义http_requests
        http = init_http
        url = myconf.get('url', 'url') + "/clients/treatSecond/saleAndConsume"
        data = str(test_info["js_data"])
        # 替换上个接口的响应单号
        new_data = da_replace(data, ["kd_id", ])
        new_data = eval(new_data)
        # 接口请求
        log.info('正在请求地址{}'.format(url))
        log.info('正在请求报文{}'.format(new_data))
        response = http.request(method=test_info["method"], url=url, json=new_data)
        res = response.json()
        print(res)
        code = res["stateCode"]
        try:
            # 【校验响应结果】
            assert str(code) == test_info["expected"]
        except AssertionError as e:
            # 用例执行未通过
            log.info('【{}】:用例执行未通过'.format(test_info["title"]))
            log.exception(e)
            raise e
        else:
            # 用例执行通过
            log.info('【{}】:用例执行通过'.format(test_info["title"]))


if __name__ == '__main__':
    pytest.main(['-m scene'])
