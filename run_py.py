"""
=============================
Author:'Dayle'
Time:2021/4/26
E-mail:39072149@qq.com
=============================
"""

import time
import pytest

filetime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
filename = '{}_api_report_smoke_success.html'.format(filetime)

# # 只运行成功用例
# pytest.main(['-m success', '--resultlog=report/demo',
#              '--junitxml=report/demo.xml',
#              f'--html=report/{filename}'])
# 运行smoke用例
pytest.main(['-m comment',
             # '--resultlog=report/demo',
             '--junitxml=report/demo.xml',
             f'--html=report/{filename}',
             # r'--alluredir=allure_report/'
             ])












