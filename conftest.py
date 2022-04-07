"""
=============================
Author:'Dayle'
Time:2021/4/26
E-mail:39072149@qq.com
=============================
"""
import pytest
from common.http_requests import HttpSession


@pytest.fixture(scope='class')
def init_http():
    """接口测试前置条件"""
    http = HttpSession()
    yield http  # 返回
    # 后置条件
    http.close()
