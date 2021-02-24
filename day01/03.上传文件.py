import requests
url = "http://www.httpbin.org/post"
#本地存在的文件
file = "d:/test.png"
with open (file ,mode='rb') as f:
    #{'name':file-tuple}
    #('filename',fileobj,'content_type')
    cs = {"filename":(file,f,"image/png")}
    r = requests.post(url,files=cs)
    print(r.text)
#租车系统上传图片
url = " http://127.0.0.1:8080/carRental/file/uploadFile.action "
file = "d:/beijing.png"
with open (file ,mode='rb') as f:
    cs = {"mf": (file, f, "image/png")}
    r = requests.post(url, files=cs)
    print(r.text)
    #获取图片路径
    uploadPath = r.json()['data']['src']

#添加车，使用刚上传的图片
url = " http://127.0.0.1:8080/carRental/car/addCar.action"
cs = {
    "carnumber": "京9999",
    "cartype": "大奔",
    "color": "黑色",
    "carimg": "正常",
    "description": "2021新车",
    "price": "200000",
    "rentprice": "1000",
    "deposit": "75",
    "isrenting": "359"
}
head = {"Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
r = requests.post(url,data=cs,headers=head)
print(r.text)



