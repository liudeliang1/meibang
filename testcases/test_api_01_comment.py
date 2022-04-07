"""
=============================
Author:'Dayle'
Time:2021/4/26
E-mail:39072149@qq.com
=============================
"""
import time
import pytest
from data.comment_data import comment_success_data
from common.conifg import myconf
from common.mylogger import log

"""
相关用例

"""


class TestHomeTask:
    pytestmark = [pytest.mark.comment, pytest.mark.smoke]  # 打标签

    @pytest.mark.parametrize("test_info", comment_success_data)
    def test_comment_task(self, test_info, init_http):
        """评价管理"""
        # 定义http_requests
        http = init_http
        url = myconf.get('url', 'a_url') + test_info["url"]
        # 接口请求
        log.info('正在请求地址{}'.format(url))
        response = http.request(method=test_info["method"], url=url, data=test_info["data"])

        print(response)
        if test_info["title"] != "login":
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
    pytest.main(['-m home'])
