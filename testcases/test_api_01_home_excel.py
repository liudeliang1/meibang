"""
=============================
Author:'Dayle'
Time:2021/4/26
E-mail:39072149@qq.com
=============================
"""
import os
import time
import pytest
from common.conifg import myconf
from common.mylogger import log
from common.constant import DATA_DIR
from common.read_excel import ReadExcel

"""
相关用例

"""
# 读取用例数据
data_file_path = os.path.join(DATA_DIR, 'cases.xlsx')
excel = ReadExcel(data_file_path, 'home')
cases = excel.read_data()


@pytest.mark.smoke
class TestHomeTask:
    pytestmark = [pytest.mark.zhu, pytest.mark.smoke]  # 打标签

    @pytest.mark.parametrize("test_info", cases)
    def test_home_task(self, test_info, init_http):
        """主页用例"""
        # 定义http_requests
        http = init_http
        url = myconf.get('url', 'url') + test_info["url"]
        data = eval(test_info["data"])
        # 接口请求
        log.info('正在请求地址{}'.format(url))
        response = http.request(method=test_info["method"], url=url, data=data)

        print(response)
        if not test_info["title"] == "login":
            res = response.json()
            print(res)
            code = res["stateCode"]
            try:
                # 【校验响应结果】
                assert code == test_info["expected"]
            except AssertionError as e:
                # 用例执行未通过
                log.info('【{}】:用例执行未通过'.format(test_info["title"]))
                log.exception(e)
                raise e
            else:
                # 用例执行通过
                log.info('【{}】:用例执行通过'.format(test_info["title"]))


if __name__ == '__main__':
    pytest.main(['-m zhu'])
