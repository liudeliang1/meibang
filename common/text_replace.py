"""
=============================
author:'Dayle'
time:2019/9/9
E-mail:liudl7@lenovo.com
=============================
"""
import re

from common.conifg import myconf

"""
实现思路：
1、获取用例数据
2、判断该条用例数据是否有需要替换的数据
3、对数据进行替换
"""


# 通过search方法进行匹配
# 判断是否有匹配到数据

class ConText:
    """用来（临时）保存接口之间以来参数的类"""
    pass


def data_replace(data):
    """替换动态参数"""
    while re.search(r"#(.+?)#", data):
        res = re.search(r"#(.+?)#", data)
        # 提取要替换的内容
        r_data = res.group()
        # 获取要替换的字段
        key = res.group(1)
        # 去配置文件中读取字段对应的数据
        try:
            value = myconf.get('data', key)
        except:
            value = getattr(ConText, key)
        # 进行替换
        data = re.sub(r_data, str(value), data)

    return data


def da_replace(data, li):
    """替换动态参数"""
    for key in li:
        res = re.search(r"#(.+?)#", data)
        # 提取要替换的内容
        r_data = res.group()
        # 获取要替换的字段
        value = getattr(ConText, key)
        # 进行替换
        data = re.sub(r_data, str(value), data)

    return data


# if __name__ == '__main__':
#     # 给对象设置一个属性：对象（类），属性名    属性值
#     # setattr(ConText, "memberid", 1999)
#     # # print(ConText.memberid)
#     # # 获取对象的属性：对象 属性名
#     # id = getattr(ConText, 'memberid')
#     # print(id)

# if __name__ == '__main__':
#     s = '{"mobilephone": "#ph_one#","pwd":"#pwd#","mobilephone2": "#phone#"}'
#     setattr(ConText, "ph_one", 1999)
#     setattr(ConText, "pwd", 111)
#     s2 = da_replace(s, ["phone", "pwd"])
#     print(s2)


if __name__ == '__main__':
    s = """{
                "jsonString": "{\"appid\":\"#kd_id#\",\"consumeData\":{\"remark\":\"\",\"platType\":12,\"appointmentId\":\"\",\"custID\":\"A001980993904\",\"orderDate\":\"2022-04-01 09:28:11\",\"treatmentList\":[],\"cardList\":[],\"YQCardList\":[],\"timeCardList\":[],\"mealCardList\":[],\"sendMessage\":false},\"saleData\":{\"customerId\":\"A001980993904\",\"custID\":\"A001980993904\",\"siteID\":\"A00101\",\"empID\":\"000000000\",\"spbill_create_ip\":\"\",\"openid\":\"\",\"list1\":[],\"list2\":[{\"pid\":\"XM021\",\"id\":\"XM021\",\"ProductID\":\"XM021\",\"couponData\":{},\"timeCard\":false,\"isYq\":\"0\",\"name\":\"手真甲护理(基础)\",\"number\":\"1\",\"price\":\"28\",\"discount\":\"100\",\"totalprice\":\"28\",\"arrears\":\"0\",\"largess\":false,\"total\":\"28\",\"minPrice\":\"21\",\"maxPrice\":null,\"ValidBalance\":null,\"AccountID\":\"\",\"usePrice\":null,\"packName\":null,\"product_id_card\":\"\",\"ProductIDCopy\":\"\",\"empFormList\":[{\"empID\":\"A06000678\",\"scale\":\"100\",\"saleHandlerType\":\"0\",\"empName\":\"程路通-1\",\"groupType\":\"1\"}],\"maxDiscountPrice\":\"28\",\"packDetails\":[],\"packArrears\":0}],\"list3\":[],\"list4\":[],\"list5\":[],\"salePayAccHistoryForm\":{\"list1\":[1,2,3],\"list2\":[\"账上余额\",\"会费\",\"储值卡\"],\"list3\":[],\"moneyPay\":\"0\",\"cardPay\":0,\"taxPay\":0},\"tbSalePayFormList\":[],\"actPay\":28,\"arrears\":\"0.00\",\"should\":28,\"newList\":[],\"orderDate\":\"2022-04-01 09:28:11\",\"remark\":\"\",\"platType\":\"12\",\"ydPay\":false,\"cardItemParams\":[],\"sendMessage\":false},\"orderAppointDate\":1648774800000}",
                "appointedDate": 1648774800000,
                "entityID": "A00101",
                "appid": "#kd_id#"
            }
     },"""
    setattr(ConText, "kd_id", 1999)
    # setattr(ConText, "pwd", 111)
    s2 = da_replace(s, ["kd_id", ])
    print(s2)
