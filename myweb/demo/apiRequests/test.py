import requests

base_url = "https://www.yeechoo.com//"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

session = requests.session()

res = session.get(url=base_url,headers=headers)
print(res.text)