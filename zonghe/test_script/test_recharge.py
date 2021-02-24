'''
测试充值的脚本
'''
import pytest

from zonghe.baw import Member
from zonghe.caw import Check, DataRead, MySqlOp


#前置条件，注册的数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_setup.yaml"))
def setup_data(request):
    return request.param


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login.yaml"))
def recharge_data(request):
    return request.param

def test_recharge(register,baserequest,url):
    '''
    充值成功的脚本
    :param register:
    :param baserequest:
    :param url:
    :return:
    '''
    print()
    #下发登录请求
    r = Member.login(baserequest, url, )

    #检查结果
    Check.equal(r.json(), login_data['expect'], 'code,status,msg')