"""
=============================
Author:'Dayle'
Time:2021/4/26
E-mail:39072149@qq.com
=============================
"""
# 主页
comment_success_data = [
    {"case_id": '1', "title": "login", "method": 'post', "url": "/clients/login",
     "data": {"username": "000000000", "password": "123456", "remember-me": "on"}, "expected": 'pass'},
    {"case_id": '2', "title": "正案例-正常请求", "method": 'get', "url": "/lianli-beauty-customer-api/treat-comment/list",
     "data": {"starQuantity": "1"}, "expected": '100'},
    {"case_id": '3', "title": "反案例-中文字符", "method": 'get', "url": "/lianli-beauty-customer-api/treat-comment/list",
     "data": {"starQuantity": "大大大"}, "expected": '100'},
]


