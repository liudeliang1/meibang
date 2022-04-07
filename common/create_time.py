"""
=============================
Author:'Dayle'
Time:2021/6/22
E-mail:39072149@qq.com
=============================
"""
import time
import datetime


# 时间日期操作


def now_time():
    """生成当前月"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def last_month():
    """生成上一个月"""
    today = datetime.date.today()
    first = today.replace(day=1)
    l_month = first - datetime.timedelta(days=1)
    return l_month.strftime("%Y-%m")


def add_date_sub(n=0):
    try:
        n = int(n)
        last = time.localtime(time.time() + n * 86400)
        return time.strftime("%Y-%m-%d %H:%M:%S", last)
    except Exception as e:
        print('请输入数值', e)


def add_date(in_data, num):
    """
    日期的加减
    :param in_data: 初始日期
    :param num: 需要加减的天数
    :return: 运算后的日期
    """
    dt = datetime.datetime.strptime(in_data, "%Y-%m-%d")
    out_date = (dt + datetime.timedelta(days=num)).strftime("%Y-%m-%d")
    return out_date


if __name__ == '__main__':
    a = now_time()
    print(a)
