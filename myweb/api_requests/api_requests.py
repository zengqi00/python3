import requests

data = {
'username':'432432',
'passwd':'432432'
}
res = requests.post(url='http://127.0.0.1:8000/login_in',data=data)
print (res.json())

def send_get(url,data):
    res = requests.get(url=url,data=data).json()
    return res

