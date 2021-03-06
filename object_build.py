import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import unittest

class Object_Build_TestCase(unittest.TestCase):

    def setUp(self):
        driver = 'C:\chromedriver_win32\chromedriver.exe'
        self.browser = webdriver.Chrome(executable_path = driver)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        pass
        #browser.quit() #退出浏览器

    def test_case1(self):
        self.browser.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        time.sleep(0.5)
        
        self.browser.find_element_by_xpath("//*[@id='account']").send_keys("chanpin")
        self.browser.find_element_by_xpath("//input[@name='password']").send_keys("Aa123456")
        self.browser.find_element_by_xpath('//*[@id="submit"]').click()
        
        time.sleep(0.5)
        title = self.browser.title
        #print(title)
        self.assertEqual(title, "我的地盘 - 禅道")
        print("登陆成功")
        
        #进入提交需求页面
