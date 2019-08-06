from selenium import webdriver
import time

def login():
    driver = webdriver.Chrome('/Users/zengqi/.virtualenvs/env1/lib/python3.7/site-packages/chromedriver')
    driver.maximize_window()
    time.sleep(1)
    #进入网站
    driver.get("http://jfjx.jtyjy.com:1035")
    #name定位并输入账号
    username = driver.find_element_by_name('username').send_keys('18372')
    pwd = [123456, 111111]
    for i in range(1):
        #name定位并输入密码
        driver.find_element_by_name('password').send_keys(pwd[i])
        #点击登陆按钮
        driver.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
        time.sleep(5)
login()


