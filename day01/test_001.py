'''
pytest命令约束
1.文件用test开头
2.类用Test开头
3.函数或方法用test_开头
'''
import requests
import pytest



@pytest.fixture(params=[{"username":"","pwd":""},{"username":"fasuhfuud","pwd":"123456"},{"username":"","pwd":"123456"},{"username":"12345678912","pwd":""},{"username":"17699947158","pwd":"123456"},{"username":"12345678913","pwd":"12345"},{"username":"12345678913","pwd":"1234567891011121314"}])
def login_data(request):#固定写法，request是pytest的关键字
    return request.param#固定写法


#使用7组数据分别执行这个用例，共执行7次
def test_login(login_data):
    print(login_data)
    #f   format格式化
    print(f"测试登录功能，使用用户名：{login_data['username']},密码：{login_data['pwd']}登录")


import pytest
import requests

# 练习：用fixture+requests，优化金融项目注册接口的脚本
cs = [
    # 密码长度为5
    {"data": {"mobilephone": 1801234567, "pwd": "12345"},
     "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
    # 密码长度超过18
    {"data": {"mobilephone": 1801234567, "pwd": "12345678901234567890"},
     "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
    # 密码为空
    {"data": {"mobilephone": 1801234567, "pwd": ""},
     "expect": {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},
    # 手机号码格式不正确
    {"data": {"mobilephone": 180123456, "pwd": "123456"},
     "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}}
     ]


@pytest.fixture(params=cs)
def register_data(request):  # 固定写法
    return request.param  # 固定写法


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r


# 数据驱动的测试模型，
# test_register 测试脚本/测试逻辑，测试数据与测试逻辑分离，相同逻辑的数据放到一起，实现一个脚本即可。
# 数据可以放到csv、xml、yaml……去维护
def test_register(register_data):
    print(f"测试数据：{register_data['data']}")
    print(f"预期结果：{register_data['expect']}")
    r = register(register_data['data'])
    print(f"实际结果：{r.text}")
    assert r.json()['status'] == register_data['expect']['status']
    assert r.json()['code'] == register_data['expect']['code']
    assert r.json()['msg'] == register_data['expect']['msg']






























#
# def test_register_001():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "",
#         "pwd": "",#手机号密码为空
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20103'
#     assert rjson["msg"] == "手机号不能为空"
#     print("注册失败")
#
# def test_register_002():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "fasuhfuud",#手机号为字母
#         "pwd": "123456",
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20109'
#     assert rjson["msg"] == "手机号码格式不正确"
#     print("注册失败")
#
#
# def test_register_003():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "",#手机号为空
#         "pwd": "123456",
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20103'
#     assert rjson["msg"] == "手机号不能为空"
#     print("注册失败")
#
# def test_register_004():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "12345678912",
#         "pwd": "",#密码为空
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20103'
#     assert rjson["msg"] == "密码不能为空"
#     print("注册失败")
#
# def test_register_005():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "17699947158",#旧会员手机号注册
#         "pwd": "123456",
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20110'
#     assert rjson["msg"] == "手机号码已被注册"
#     print("注册失败")
#
# def test_register_006():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "12345678913",
#         "pwd": "12345",#密码为5位
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20108'
#     assert rjson["msg"] == "密码长度必须为6~18"
#     print("注册失败")
#
# def test_register_007():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "12345678913",
#         "pwd": "1234567891011121314",#密码为19位
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20108'
#     assert rjson["msg"] == "密码长度必须为6~18"
#     print("注册失败")

# def test_register_008():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "18799964829",
#         "pwd": "        ",#密码为8位空格
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 0
#     assert rjson['code'] == '20103'
#     assert rjson["msg"] == "密码不能为空"
#     print("注册失败")
#
# def test_register_009():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "12345678945",
#         "pwd": "123456",#手机号密码正确
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 1
#     assert rjson['code'] == '10001'
#     assert rjson["msg"] == "成功"
#     print("注册成功")
#
# def test_register_0010():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "17699943782",
#         "pwd": "123456",#手机号密码正确
#         "regname" : ""#用户名为空
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 1
#     assert rjson['code'] == '10001'
#     assert rjson["msg"] == "注册成功"
#     print("注册成功")
#
# def test_register_0011():
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     cs = {
#         "mobilephone": "15958395832",
#         "pwd": "123456",#手机号密码正确
#         "regname" : "测试用户"#用户名写入正确
#     }
#     r = requests.get(url, params=cs)
#     print(r.text)
#     rjson = r.json()
#     assert rjson['status'] == 1
#     assert rjson['code'] == '10001'
#     assert rjson["msg"] == "注册成功"
#     print("注册成功")