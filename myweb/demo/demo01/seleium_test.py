import random
from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome('/Users/zengqi/.virtualenvs/py3.7/lib/python3.7/site-packages/chromedriver')
# for i in range(8):
#     email = "".join(random.sample("1234567890asdfrewq",8))+"@163.com"
#     print(email)
driver.get("https://www.baidu.com/")
#保存网站图片
driver.save_screenshot("/Users/zengqi/Desktop/seleium_study/imooc.png")
#找到图片的定位
code_element = driver.find_element_by_xpath('//*[@id="qrcode"]/div/div[1]')
left = code_element.location["x"]
top = code_element.location["y"]
right = code_element.size["width"]+left
height = code_element.size["height"]+top

im = Image.open("/Users/zengqi/Desktop/seleium_study/imooc.png")
img = im.crop((left,top,right,height))
img.save("/Users/zengqi/Desktop/seleium_study/imooc1.png")
driver.close()
