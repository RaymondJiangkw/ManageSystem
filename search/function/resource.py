# Get the relevent web pages
import requests
from lxml import html
Request_Headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Cookie":"UM_distinctid=16dcfb868cf64e-0c3fc636fbf067-b781636-15f900-16dcfb868d02ef; csrftoken=paHOMJRDzHYjPaO5B32TIDZO1hLf7zGrQHFXk6ivv1s0B9KMTgo1xhAGQgMTMxY6",
    "Host":"mis.bjtu.edu.cn",
    "Referer":"https://mis.bjtu.edu.cn/profile/",
    "Sec-Fetch-Mode":"navigate",
    "Sec-Fetch-Site":"none",
    "Sec-Fetch-User":"?1",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
}
payload = {
    'loginname':"19211423",
    "password":"jkw6766034",
    'csrfmiddlewaretoken':"",
    'next':"/o/authorize/?response_type=code&client_id=aGex8GLTLueDZ0nW2tD3DwXnSA3F9xeFimirvhfo&state=1578839321&redirect_uri=https://mis.bjtu.edu.cn/auth/callback/?redirect_to=/home/",
}
# Login Part get support from https://blog.csdn.net/iodjSVf8U1J7KYc/article/details/78940671
session_requests_login = requests.session()
session_requests_login.headers = Request_Headers
login_url = "https://cas.bjtu.edu.cn/auth/login/"
# print("Preparations Done. Try to open the session.")
login_result = session_requests_login.get(login_url)
# print("Session opens successfully.")
tree = html.fromstring(login_result.text)
authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
payload['csrfmiddlewaretoken'] = authenticity_token
# print("Data Prepares Well")
# print(payload)
# print("Try to Login")
session_requests_login.headers['Host'] = "cas.bjtu.edu.cn"
session_requests_login.headers['Origin'] = "https://cas.bjtu.edu.cn"
session_requests_login.headers['Referer'] = "https://cas.bjtu.edu.cn/auth/login/?next=/o/authorize/%3Fresponse_type%3Dcode%26client_id%3DaGex8GLTLueDZ0nW2tD3DwXnSA3F9xeFimirvhfo%26state%3D1578839321%26redirect_uri%3Dhttps%3A//mis.bjtu.edu.cn/auth/callback/%3Fredirect_to%3D/home/"
session_requests_login.headers['Content-Length'] = "342"
session_requests_login.headers['Content-Type'] = "application/x-www-form-urlencoded"
login_result = session_requests_login.post(
    login_url,
    data = payload,
    params = {"next":"/o/authorize/%3Fresponse_type%3Dcode%26client_id%3DaGex8GLTLueDZ0nW2tD3DwXnSA3F9xeFimirvhfo%26state%3D1578839321%26redirect_uri%3Dhttps%3A//mis.bjtu.edu.cn/auth/callback/%3Fredirect_to%3D/home/"}
)
# print("Login Successfully")
base_url = "https://mis.bjtu.edu.cn/home/"
