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
