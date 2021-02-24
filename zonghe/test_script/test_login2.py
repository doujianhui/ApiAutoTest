import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp, Check


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login.yaml"))
def login_data(request):
    return request.param
def test_login(baserequest,url,db_info,login_data):
    MySqlOp.delete_user(db_info, login_data['regdata']['mobilephone'])
    #注册用户
    print("注册数据：",login_data['regdata'])
    r = Member.register(baserequest, url, login_data['regdata'])
    #登录
    print("登录数据：",login_data['logindata'])
    r = Member.login(baserequest, url, login_data['logindata'])

    #检查结果
    # assert r.json()['code'] == login_data['expect']['code']
    # assert r.json()['status'] == login_data['expect']['status']
    # assert r.json()['msg'] == login_data['expect']['msg']
    # 重复代码，出现次数多的代码，可以封装成方法，简化调用
    Check.equal(r.json(), login_data['expect'], 'code,status,msg')


    #删除注册用户
    MySqlOp.delete_user(db_info, login_data['regdata']['mobilephone'])