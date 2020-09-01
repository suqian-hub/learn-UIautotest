import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import unittest

# Zentao-V12.0.1 64bit
#driver = 'C:\chromedriver_win32\chromedriver.exe'
#browser = webdriver.Chrome(executable_path = driver)

class Submit_Bug_TestCase(unittest.TestCase):

    def setUp(self):
        driver = 'C:\chromedriver_win32\chromedriver.exe'
        self.browser = webdriver.Chrome(executable_path = driver)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        pass
        #browser.quit() #退出浏览器

    def test_case1(self): #登陆页面
        
        self.browser.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        time.sleep(1)
        
        self.browser.find_element_by_xpath("//*[@id='account']").send_keys("admin")
        self.browser.find_element_by_xpath("//input[@name='password']").send_keys("Aa123456")
        self.browser.find_element_by_xpath('//*[@id="submit"]').click()
        
        self.browser.refresh()
        title = self.browser.title
        #print(title)
        self.assertEqual(title, "我的地盘 - 禅道")
        print("登陆成功")

        #进入bug提交页面
        
        self.browser.find_element_by_xpath("//nav[@id='navbar']//li[4]//a[1]").click()
        self.browser.find_element_by_xpath("//ul[@class='nav nav-default']//a[contains(text(),'Bug')]").click()
        self.browser.find_element_by_xpath("//a[@class='btn btn-primary']").click()
        time.sleep(1)
        self.browser.get_screenshot_as_file("./submit_bug.png")
        
        time.sleep(1)
        title = self.browser.title
        #print(title)
        self.assertEqual(title, "见山会诊-小程序-提Bug - 禅道")

        #填写内容
        
        self.browser.find_element_by_xpath("//div[@id='module_chosen']//a[@class='chosen-single']").click()
        ele1 = self.browser.find_element_by_xpath("//div[@class='chosen-drop chosen-auto-max-width chosen-no-wrap in']")
        ele2 = self.browser.find_element_by_xpath("//div[@id='moduleIdBox']//li[2]")
        
        ActionChains(self.browser).move_to_element(ele1).move_to_element(ele2).click(ele2).perform()
        




if __name__ == '__main__':
    unittest.main()
        

        
