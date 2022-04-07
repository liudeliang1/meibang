"""
=============================
author:'liudl'
time:2019/8/31
E-mail:liudl7@lenovo.com
=============================
"""
import requests


class HttpRequest(object):
    """不需要记住cookie信息的请求类"""

    def request(self, method, url, json=None, data=None, headers=None, cookies=None):
        # None 默认值，可传可不传
        # 发送请求的方法
        # 转换为小写
        method = method.lower()
        # 判断发送请求的方法
        if method == 'post':
            return requests.post(url=url, data=data, json=json, headers=headers)
        elif method == 'get':
            return requests.get(url=url, params=data, headers=headers, cookies=cookies)


class HttpSession(object):
    """使用session对象发送请求，自动记录cookies信息"""

    def __init__(self):
        # 创建一个session对象
        self.session = requests.session()

    def request(self, method, url, data=None, json=None, headers=None):
        # 判断请求方法
        method = method.lower()
        if method == 'post':
            return self.session.post(url=url, data=data, json=json, headers=headers)
        elif method == 'get':
            return self.session.get(url=url, params=data, json=json, headers=headers)

    def close(self):
        # 记得关闭session对象
        self.session.close()


if __name__ == '__main__':
    http = HttpSession()
    # response1 = http.request(method='get', url='http://test.lemonban.com/futureloan/mvc/api/member/login',
    #                          data={"mobilephone": "18750261519", "pwd": "123qwe"})
    # re = http.request(method='get', url='http://test.lemonban.com/futureloan/mvc/api/loan/add',
    #                   data={"memberId": "132694", "title": "世界这么大，想去看一看", "amount": 20000, "loanRate": "12.0",
    #                         "loanTerm": 2, "loanDateType": 0, "repaymemtWay": 11, "biddingDays": 5})
    # response = http.request(method='post', url='http://test.lemonban.com/futureloan/mvc/api/member/withdraw',
    #                         data={"mobilephone": "18750261519", "amount": 10000})
    response = http.request(method='post', url='http://clients-test.meibangtech.com/clients/bookingInfo/createNewBookingArrange',
                            json={
    "jsonString": "{\"appid\":\"55224\",\"consumeData\":{\"remark\":\"\",\"platType\":12,\"appointmentId\":\"\",\"custID\":\"A001980993904\",\"orderDate\":\"2022-04-01 09:28:11\",\"treatmentList\":[],\"cardList\":[],\"YQCardList\":[],\"timeCardList\":[],\"mealCardList\":[],\"sendMessage\":false},\"saleData\":{\"customerId\":\"A001980993904\",\"custID\":\"A001980993904\",\"siteID\":\"A00101\",\"empID\":\"000000000\",\"spbill_create_ip\":\"\",\"openid\":\"\",\"list1\":[],\"list2\":[{\"pid\":\"XM021\",\"id\":\"XM021\",\"ProductID\":\"XM021\",\"couponData\":{},\"timeCard\":false,\"isYq\":\"0\",\"name\":\"手真甲护理(基础)\",\"number\":\"1\",\"price\":\"28\",\"discount\":\"100\",\"totalprice\":\"28\",\"arrears\":\"0\",\"largess\":false,\"total\":\"28\",\"minPrice\":\"21\",\"maxPrice\":null,\"ValidBalance\":null,\"AccountID\":\"\",\"usePrice\":null,\"packName\":null,\"product_id_card\":\"\",\"ProductIDCopy\":\"\",\"empFormList\":[{\"empID\":\"A06000678\",\"scale\":\"100\",\"saleHandlerType\":\"0\",\"empName\":\"程路通-1\",\"groupType\":\"1\"}],\"maxDiscountPrice\":\"28\",\"packDetails\":[],\"packArrears\":0}],\"list3\":[],\"list4\":[],\"list5\":[],\"salePayAccHistoryForm\":{\"list1\":[1,2,3],\"list2\":[\"账上余额\",\"会费\",\"储值卡\"],\"list3\":[],\"moneyPay\":\"0\",\"cardPay\":0,\"taxPay\":0},\"tbSalePayFormList\":[],\"actPay\":28,\"arrears\":\"0.00\",\"should\":28,\"newList\":[],\"orderDate\":\"2022-04-01 09:28:11\",\"remark\":\"\",\"platType\":\"12\",\"ydPay\":false,\"cardItemParams\":[],\"sendMessage\":false},\"orderAppointDate\":1648774800000}",
    "appointedDate": 1648774800000,
    "entityID": "A00101",
    "appid": "55224"
}, headers={'Cookie': 'JSESSIONID=B1CF7F38E1DD5EA23DEDCE33A735D7FC'})
    print(response)
    res = response.json()

    print(res)
