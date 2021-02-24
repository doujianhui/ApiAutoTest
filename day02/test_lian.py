import mock

import pytest
import requests


cs = [
    #密码长度为5
    {"data":{"mobilephone":18012345674,"pwd":"12345"},
     "expect":{"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}},
    # 密码长度超过18
    {"data": {"mobilephone": 18012345621, "pwd": "12345678901234567890"},
     "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
    # 密码为空
    {"data": {"mobilephone": 18012345622, "pwd": ""},
     "expect": {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},
    # 手机号码格式不正确
    {"data": {"mobilephone": 1801234523, "pwd": "123456"},
     "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}}
]
#从cs中每次取一个param
@pytest.fixture(params=cs)
def register_data(request):

    return request.param

#用户注册
def register(data):
    url="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data)
    return r.json()


#用户登录
def login(data):
    r = requests.post("http://192.168.150.222:8081/futureloan/mvc/api/member/login", data)
    return r.json()


#用户充值
def recharge(data):
    r = requests.post("http://192.168.150.222:8081/futureloan/mvc/api/member/recharge", data)
    return r.json()


#用户取现
def withdraw(data):
    r = requests.post("http://192.168.150.222:8081/futureloan/mvc/api/member/withdraw", data)
    return r.json()



class TestClass:

    def setup_class(self):
        print("开始测试")
    def teardown_class(self):
        print("测试结束")

    def setup_method(self):
        print("开始测试本接口")

    def teardown_method(self):
        print("本接口测试完成")

    #注册用例测试
    def test_register(self,register_data):
        print(f"测试数据:{register_data['data']}")
        print(f"预期结果:{register_data['expect']}")
        r = register(register_data['data'])
        print("实际结果:{r.text}")

        #断言
        assert r['status'] == register_data['expect']['status']
        assert r['code'] == register_data['expect']['code']
        assert r['msg'] == register_data['expect']['msg']


    #登录用例测试
    def test_login(self):
        data = {"mobilephone":"15026582814","pwd":"123456","regname":"requests_test"}
        r = login(data)

        assert r['status'] == 1
        assert r['code'] == "10001"
        assert r['msg'] == "登录成功"



    #充值用例测试
    def test_recharge(self):
        data = {"mobilephone":"15026582814","pwd":"123456","regname":"requests_test","amount":"1000"}

        r = recharge(data)

        assert r['status'] == 1
        assert r['code'] == "10001"
        assert r['msg'] == "充值成功"


    #取现用例测试
    def test_withdraw(self):
        data = {"mobilephone":"15026582814","pwd":"123456","regname":"requests_test","amount":"1000"}

        withdraw = mock.Mock(return_value={"code": 10001, "msg": "取现成功"})
        r = withdraw(data)
        assert r['msg'] == "取现成功"









