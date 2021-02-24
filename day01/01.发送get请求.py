'''
接口测试：
    使用request中的get、post方法调用接口，检查返回值是否正确
'''
import requests
#get请求，不带参数
#获取用户列表接口
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/list"
# url = "http://jy001:8081/futureloan/mvc/api/member/list"
#发送get请求
r = requests.get(url)
#打印响应
print(r.text)
#检查结果是否与预期相同
assert r.status_code == 200
assert r.reason == "OK"
rjson=r.json()
assert rjson['status']==1
assert rjson['code']=='10001'
assert rjson["msg"]=="获取用户列表成功"
#响应头
print(r.headers)
############get请求，带参数#################
#注册接口，参数拼接在url的后面，多个参数用&拼接
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/list"
#发送get请求
r = requests.get(url)
#打印响应，文本格式的
# print(r.text)
# rjson = r.json()
# assert  rjson['status']==0
# assert rjson['code']=='20108'
# assert rjson["msg"]=="密码长度必须为6-18"

#注册接口，使用param传参
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
cs = {
    "mobilephone":"17699947158",
    "pwd":"123456",
    "regname":"requests_test"
}
r = requests.get(url,params=cs)
print(r.text)
rjson = r.json()
assert rjson['status']==0
assert rjson['code']=='20110'
assert rjson["msg"]=="手机号码已被注册"

#查询手机号码归属地的接口，参数：tel
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=17699947158"
r=requests.get(url)
print(r.text)
assert '新疆联通' in r.text
