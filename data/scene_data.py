"""
=============================
Author:'Dayle'
Time:2021/4/26
E-mail:39072149@qq.com
=============================
"""
from common.create_time import now_time
now_time = now_time()

# 主页
scene_success_data = [
    {"case_id": '1', "title": "scene", "method": 'post', "url": "/clients/login", "expected": '100',
     # 登录数据
     "login_data": {"username": "000000000", "password": "123456", "remember-me": "on"},
     "test_data": {"time": now_time, "password": "123456", "remember-me": "on"},
     # 开单数据
     "add_data": {
         "status": "4",
         "saleType": "3",
         "source": 4,
         "appDate": 1648774800000,
         "custID": "A001980993904",
         "remark": "",
         "techIdArr": [
             "A06000678"
         ],
         "appTechIdArr": [
             ""
         ],
         "durnTime": "",
         "roomId": "",
         "appDeviceIdArr": [
             ""
         ],
         "isNeedTea": "0",
         "isNeedHair": "0",
         "isNeedPark": "0",
         "isLineUp": "2",
         "appointSourceCode": ""
     },
     # 排单数据
     "pd_data": {
         "jsonString": "{\"appid\":\"#kd_id#\",\"consumeData\":{\"remark\":\"\",\"platType\":12,\"appointmentId\":\"\",\"custID\":\"A001980993904\",\"orderDate\":\"2022-04-01 09:28:11\",\"treatmentList\":[],\"cardList\":[],\"YQCardList\":[],\"timeCardList\":[],\"mealCardList\":[],\"sendMessage\":false},\"saleData\":{\"customerId\":\"A001980993904\",\"custID\":\"A001980993904\",\"siteID\":\"A00101\",\"empID\":\"000000000\",\"spbill_create_ip\":\"\",\"openid\":\"\",\"list1\":[],\"list2\":[{\"pid\":\"XM021\",\"id\":\"XM021\",\"ProductID\":\"XM021\",\"couponData\":{},\"timeCard\":false,\"isYq\":\"0\",\"name\":\"手真甲护理(基础)\",\"number\":\"1\",\"price\":\"28\",\"discount\":\"100\",\"totalprice\":\"28\",\"arrears\":\"0\",\"largess\":false,\"total\":\"28\",\"minPrice\":\"21\",\"maxPrice\":null,\"ValidBalance\":null,\"AccountID\":\"\",\"usePrice\":null,\"packName\":null,\"product_id_card\":\"\",\"ProductIDCopy\":\"\",\"empFormList\":[{\"empID\":\"A06000678\",\"scale\":\"100\",\"saleHandlerType\":\"0\",\"empName\":\"程路通-1\",\"groupType\":\"1\"}],\"maxDiscountPrice\":\"28\",\"packDetails\":[],\"packArrears\":0}],\"list3\":[],\"list4\":[],\"list5\":[],\"salePayAccHistoryForm\":{\"list1\":[1,2,3],\"list2\":[\"账上余额\",\"会费\",\"储值卡\"],\"list3\":[],\"moneyPay\":\"0\",\"cardPay\":0,\"taxPay\":0},\"tbSalePayFormList\":[],\"actPay\":28,\"arrears\":\"0.00\",\"should\":28,\"newList\":[],\"orderDate\":\"2022-04-01 09:28:11\",\"remark\":\"\",\"platType\":\"12\",\"ydPay\":false,\"cardItemParams\":[],\"sendMessage\":false},\"orderAppointDate\":1648774800000}",
         "appointedDate": 1648774800000,
         "entityID": "A00101",
         "appid": "#kd_id#"
     },
     # 结算数据
     "js_data": {
         "appid": "#kd_id#",
         "consumeData": {
             "remark": "",
             "platType": 12,
             "appointmentId": "",
             "custID": "A001980993904",
             "orderDate": "2022-04-01 09:28:11",
             "treatmentList": [
                 {
                     "productID": "XM021",
                     "accountID": "",
                     "pckId": "",
                     "amount": "1",
                     "price": "28",
                     "Largess": "false",
                     "cardCash": "28.00",
                     "ValidCount": "1",
                     "handlers": [
                         {
                             "empID": "A00101763",
                             "scale": 1,
                             "isBeautician": "1",
                             "empName": "袁丽梅",
                             "groupType": "2"
                         }
                     ],
                     "deviceArr": [],
                     "id": "XM021",
                     "pckNum": "",
                     "packNum": "",
                     "Name": "手真甲护理(基础)",
                     "rate": 1,
                     "roomId": "16",
                     "roomIdName": "",
                     "startServiceTime": 1648774800000,
                     "usedTime": "",
                     "pId": "XM021",
                     "packName": "",
                     "roomName": "翠1",
                     "product_id_card": "null"
                 }
             ],
             "cardList": [],
             "YQCardList": [],
             "timeCardList": [],
             "mealCardList": [],
             "sendMessage": "true"
         },
         "saleData": {
             "customerId": "A001980993904",
             "custID": "A001980993904",
             "siteID": "A00102",
             "empID": "000000000",
             "spbill_create_ip": "",
             "openid": "",
             "list1": [],
             "list2": [
                 {
                     "pid": "XM021",
                     "id": "XM021",
                     "ProductID": "XM021",
                     "couponData": {},
                     "timeCard": "false",
                     "isYq": "0",
                     "name": "手真甲护理(基础)",
                     "number": "1",
                     "price": "28",
                     "discount": "100",
                     "totalprice": "28",
                     "arrears": "0",
                     "largess": "false",
                     "total": "28",
                     "minPrice": "21",
                     "maxPrice": "null",
                     "ValidBalance": "null",
                     "AccountID": "",
                     "usePrice": "null",
                     "packName": "null",
                     "product_id_card": "",
                     "ProductIDCopy": "",
                     "empFormList": [
                         {
                             "empID": "A06000678",
                             "scale": "100",
                             "saleHandlerType": "0",
                             "empName": "程路通-1",
                             "groupType": "1"
                         }
                     ],
                     "maxDiscountPrice": "28",
                     "packDetails": [],
                     "packArrears": 0
                 }
             ],
             "list3": [],
             "list4": [],
             "list5": [],
             "salePayAccHistoryForm": {
                 "list1": [
                     1,
                     2,
                     3
                 ],
                 "list2": [
                     "账上余额",
                     "会费",
                     "储值卡"
                 ],
                 "list3": [],
                 "moneyPay": "0",
                 "cardPay": 0,
                 "taxPay": 0
             },
             "tbSalePayFormList": [
                 {
                     "amount": 28,
                     "payMethod": "WX",
                     "payMethodName": "微信"
                 }
             ],
             "actPay": 28,
             "arrears": "0.00",
             "should": 28,
             "newList": [],
             "orderDate": "2022-04-01 09:28:11",
             "remark": "",
             "platType": "12",
             "ydPay": "false",
             "cardItemParams": [],
             "sendMessage": "true"
         },
         "cardDataForm": {
             "appid": "#kd_id#",
             "consumeData": {
                 "remark": "",
                 "platType": 12,
                 "appointmentId": "",
                 "custID": "A001980993904",
                 "orderDate": "2022-04-01 09:28:11",
                 "treatmentList": [],
                 "cardList": [],
                 "YQCardList": [],
                 "timeCardList": [],
                 "mealCardList": [],
                 "sendMessage": "true"
             },
             "saleData": {
                 "customerId": "A001980993904",
                 "custID": "A001980993904",
                 "siteID": "A00102",
                 "empID": "000000000",
                 "spbill_create_ip": "",
                 "openid": "",
                 "list1": [],
                 "list2": [],
                 "list3": [],
                 "list4": [],
                 "list5": [],
                 "salePayAccHistoryForm": {
                     "list1": [
                         1,
                         2,
                         3
                     ],
                     "list2": [
                         "账上余额",
                         "会费",
                         "储值卡"
                     ],
                     "list3": [],
                     "moneyPay": "0",
                     "cardPay": "0.00",
                     "taxPay": 0
                 },
                 "tbSalePayFormList": [
                     {
                         "amount": 28,
                         "payMethod": "WX",
                         "payMethodName": "微信"
                     }
                 ],
                 "actPay": "0.00",
                 "arrears": "0.00",
                 "should": "0.00",
                 "newList": [],
                 "orderDate": "2022-04-01 09:28:11",
                 "remark": "",
                 "platType": "12",
                 "ydPay": "false",
                 "cardItemParams": [],
                 "sendMessage": "true"
             }
         }
     },
     },
]

dic = scene_success_data[0]
print(dic["test_data"])
