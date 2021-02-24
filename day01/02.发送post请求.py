import requests

#表单格式的数据：content-type：www-x-form-urlencodeed,使用data传参
#登录接口
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
cs = {
    "mobilephone":"17699947158",
    "pwd":"123456"
}
r = requests.post(url,data=cs)
#打印响应
print(r.text)
rjson = r.json()
assert rjson['status']==1
assert rjson['code']=='10001'
assert rjson["msg"]=="登录成功"

#json格式的数据：content-type:application/json,使用json传参
#具体使用data还是json传参，要看接口是怎么定义的
#httpbin.org是一个测试网站，不管发送什么类型的数据，
#这个接口将发送的请求，封装成json格式的返回
url = "http://www.httpbin.org/post"
cs = {
    "mobilephone":"17699947158",
    "pwd":"123456"
}
r = requests.post(url,data=cs)
#打印响应
print("data传参===",r.text)

r = requests.post(url,json=cs)
print("json传参===",r.text)
print("=====================================================")
#租车系统，添加车辆
url = "http://127.0.0.1:8080/carRental/car/addCar.action "
cs = {
    "carnumber":"京8999",
    "cartype":"大奔",
    "color":"黑色",
    "carimg":"正常",
    "description":"2021新车",
    "price":"200000",
    "rentprice":"1000",
    "deposit":"75",
    "isrenting":"359"
}
#使用接口添加的车辆，中文字符乱码，但是用界面添加的车辆，不会有乱码
#分别抓脚本的包与界面的包，对比差异。界面设置了charset=UTF-8，但是脚本未设置导致
head = {
    "Content-Type":"application/x-www-form-urlencodeed;charset=UTF-8"
}
r = requests.post(url,data=cs,headers=head)
print(r.text)


