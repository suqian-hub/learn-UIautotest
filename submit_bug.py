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
        
        time.sleep(0.5)
        title = self.browser.title
        #print(title)
        self.assertEqual(title, "我的地盘 - 禅道")
        print("登陆成功")

        #进入bug提交页面
        self.browser.find_element_by_xpath("//nav[@id='navbar']//li[4]//a[1]").click()
        self.browser.find_element_by_xpath("//ul[@class='nav nav-default']//a[contains(text(),'Bug')]").click()
        self.browser.find_element_by_xpath("//a[@class='btn btn-primary']").click()
        
        time.sleep(0.5)
        self.browser.get_screenshot_as_file("./submit_bug.png")
        title = self.browser.title
        #print(title)
        self.assertEqual(title, "见山会诊-小程序-提Bug - 禅道")

        #填写内容 1、模块
        self.browser.find_element_by_xpath("//div[@id='module_chosen']//a[@class='chosen-single']").click()
        ele1 = self.browser.find_element_by_xpath("//div[@class='chosen-drop chosen-auto-max-width chosen-no-wrap in']")
        ele2 = self.browser.find_element_by_xpath("//div[@id='moduleIdBox']//li[2]")
        
        ActionChains(self.browser).move_to_element(ele1).move_to_element(ele2).click(ele2).perform()

        #填写内容 2、项目
        self.browser.find_element_by_xpath("//div[@id='project_chosen']").click()
        ele3 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/span[1]/div[1]/div[1]/ul[1]/li[1]")
        ActionChains(self.browser).move_to_element(ele3).click(ele3).perform()

        #填写内容 3、版本
        time.sleep(0.2)
        self.browser.find_element_by_xpath("//div[@id='openedBuild_chosen']").click()
        ele4 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]")
        ele5 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/ul[1]/li[3]")
        ActionChains(self.browser).move_to_element(ele4).move_to_element(ele5).click(ele5).perform()

        #填写内容 4、指派
        self.browser.find_element_by_xpath("//div[@id='assignedTo_chosen']").click()
        ele6 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]/div[1]/ul[1]")
        ele7 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]/div[1]/ul[1]/li[3]")
        ActionChains(self.browser).move_to_element(ele6).move_to_element(ele7).click(ele7).perform()

        #填写内容 5、bug标题
        self.browser.find_element_by_xpath("//div[@class='input-control has-icon-right required']//input[@id='title']").send_keys("UI自动化测试，提交bug！")

        # 6、严重程度 ：1
        self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[2]/button[1]").click()
        ele8 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[2]/div[1]/div[1]")
        ele9 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
        ActionChains(self.browser).move_to_element(ele8).move_to_element(ele9).click(ele9).perform()

        # 7、优先级 ：1
        self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[3]/button[1]").click()
        ele10 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[3]/div[1]/div[1]")
        ele11 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[3]/div[1]/div[1]/span[1]")
        ActionChains(self.browser).move_to_element(ele10).move_to_element(ele11).click(ele11).perform()

        #8、重现步骤
        frameid = self.browser.find_element_by_xpath("//iframe[@class='ke-edit-iframe']")
        self.browser.switch_to.frame(frameid)
        self.browser.find_element_by_xpath('/html/body').clear()  #清空；对元素的操作
        self.browser.find_element_by_xpath('/html/body').send_keys("登录禅道测试账号，提交bug。")
        self.browser.switch_to.default_content()

        #9、保存
        self.browser.find_element_by_xpath("//button[@id='submit']").click()



if __name__ == '__main__':
    unittest.main()
