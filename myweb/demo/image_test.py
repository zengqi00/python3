# 1.导入相关的模块
import requests
# xpath语法用到了一个模块(pip install lxml)
# lxml 帮助我们解析 html xml
from lxml import html
etree = html.etree
# 2.发送网络请求获取数据
# 2.1确定爬取网站(url)
base_url = "https://www.mzitu.com/jiepai/"
# 2.2 防止反爬(构建请求头)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
# 2.3发送请求
# 响应体 (想要的数据,响应头)
response = requests.get(url=base_url, headers=headers)
# 拆分响应对象,拿到数据内容
# print(response.content.decode("utf-8"))
# 字符串类型
html = response.content.decode("utf-8")
# 3.分析网页架构(找到需要的数据)(解析数据)
# 解析数据: xpath 节点截取数据 bs4 (html) pyquery 正则表达式
# <html>
#     <div>
#       <div>
#         <a>
#         <img>http:"aaaaa"<img>
#         </a>
#       <div>
#     <div>
#       <div>
#     <div>
# </html>

# //*[@id="div-comment-10133"]/p/img
# url_list = https://www.mzitu.com/jiepai/comment-page-51/#comments
# 使用xpath进行解析数据(不可以解析字符串类型)
# 1.转换成可以解析的类型div-comment-10133
html = etree.HTML(response.content.decode("utf-8"))
url_list = html.xpath('//*[@id ="comments"]/ul/li')
# print(url_list)
# 需求获取li(p/img(src))
num = 0
for li in url_list:
    num += 1
    #     print(li)
    # 二次解析(获取真正我们需要的图片)
    img_url = li.xpath("./div/p/img/@data-original")[0]
    print(img_url)
    # 4.保存到本地
    # 发送请求下载图片
    img_response = requests.get(url=img_url, headers=headers)

    # 保存本地(给下载的图片起名字)
    with open("/Users/zengqi/Desktop/zengqi_study/python3/myweb/demo/imag/{}.jpg".format(num), "wb") as f:
        f.write(img_response.content)


