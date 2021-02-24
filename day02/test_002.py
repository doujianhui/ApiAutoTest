'''
测试前置和后置
    类和方法级别的
'''
class TestClass:
    def setup_class(self):
        print("类里所有用例前执行一次")

    def teardown_class(self):
        print("类里所有用例后执行一次")

    def setup_method(self):
        print("每个方法前执行")

    def teardown_method(self):
        print("每个方法后执行")

    def test_001(self):
        print("用例1")

    def test_002(self):
        print("用例2")

    def test_003(self):
        print("用例3")