'''
requests.session 来保持状态。自动管理过程中产生的cookie，
下次请求时自动带着上次的cookie
'''
import requests
#requests.get()
s = requests.session()
print(s.cookies)
#通过dic_from_cookiejar将cookie转成字典
print("登录前的cookies：",requests.utils.dict_from_cookiejar(s.cookies))
#登陆接口
url = "https://www.bagevent.com/user/login"
cs = {
    "access_type":"1",
    "loginType":"1",
    "emailLoginWay":"0",
    "account": "2780487875@qq.com",
    "password":"qq2780487875",
    "remindmeBox":"on",
    "remindme":"1"
}
r = s.post(url,data=cs)
print(r.text)
#dashboard接口
r = s.get("https://www.bagevent.com/acount/dashboard")
print(r.text)
assert "<title>百格活动 - 账户总览</title>" in r.text

#退出登录的接口
url = "https://www.bagevent.com/cn/ "
print("退出登录后的cookies：",requests.utils.dict_from_cookiejar(s.cookies))