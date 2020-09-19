import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

import unittest

class Test_Task_TestCase(unittest.TestCase):

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
        
        self.browser.find_element_by_xpath("//*[@id='account']").send_keys("admin")
        self.browser.find_element_by_xpath("//input[@name='password']").send_keys("Aa123456")
        self.browser.find_element_by_xpath('//*[@id="submit"]').click()

        time.sleep(0.2)
        #self.browser.refresh()
        title = self.browser.title
        #print(title)
        self.assertEqual(title, "我的地盘 - 禅道")
        print("登陆成功")
        
        #进入提交测试页面
        self.browser.find_element_by_xpath("//nav[@id='navbar']//li[4]//a[1]").click()
        self.browser.find_element_by_xpath("//div[@id='subHeader']//li[3]//a[1]").click()
        self.browser.find_element_by_xpath("//a[@class='btn btn-info']").click()

        time.sleep(0.5)
        self.browser.get_screenshot_as_file("./test_task.png")
        title = self.browser.title
        #print(title)
        self.assertEqual(title, "见山会诊-小程序-提交测试 - 禅道")

        #所属模块
        self.browser.find_element_by_xpath("//div[@id='project_chosen']//a[@class='chosen-single chosen-default']").click()
        ele1 = self.browser.find_element_by_xpath("//div[@id='project_chosen']//ul[@class='chosen-results']")  
        ActionChains(self.browser).move_to_element(ele1).click(ele1).perform()

        #负责人
        self.browser.find_element_by_xpath("//div[@id='owner_chosen']//a[@class='chosen-single chosen-default']").click()
        time.sleep(1)        
        #ele2 = self.browser.find_element_by_xpath("//div[@class='chosen-drop chosen-auto-max-width chosen-no-wrap in']//ul[@class='chosen-results']")  
        ele3 = self.browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]/div[1]/ul[1]/li[1]") 
        ActionChains(self.browser).move_to_element(ele3).click(ele3).perform()
       
        #开始日期
        self.browser.find_element_by_xpath("//input[@id='begin']").click()
        ele4 = self.browser.find_element_by_xpath("/html[1]/body[1]/div[2]/div[3]/table[1]/tfoot[1]/tr[1]/th[1]")
        ActionChains(self.browser).move_to_element(ele4).click(ele4).perform()        
        
        #名称
        self.browser.find_element_by_xpath("//input[@id='name']").send_keys('UI自动化测试提交测试单')

        #描述
        frameid = self.browser.find_element_by_xpath("//iframe[@class='ke-edit-iframe']")
        self.browser.switch_to.frame(frameid)
        self.browser.find_element_by_xpath('/html/body').clear()  #清空；对元素的操作
        self.browser.find_element_by_xpath('/html/body').send_keys("UI自动化测试提交测试单")
        self.browser.switch_to.default_content()

        #保存
        self.browser.find_element_by_xpath("//button[@id='submit']").click()


if __name__ == '__main__':
    unittest.main()


