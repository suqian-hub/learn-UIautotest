from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

# chrome V84.0.4147.135 64bit
driver = 'C:\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(executable_path = driver)
'''
Zentao-v12.0.1-64bit
'''
#打开网页
browser.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
time.sleep(1)
#用户名
browser.find_element_by_xpath("//*[@id='account']").send_keys("admin")
#密码
browser.find_element_by_xpath('//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys("Aa123456")

#登录
browser.find_element_by_xpath('//*[@id="submit"]').click()
#定位标题
browser.refresh()
tilte = browser.find_element_by_css_selector("body.m-my-index:nth-child(2) div:nth-child(1) div.container hgroup:nth-child(1) h1:nth-child(1) > a:nth-child(1)")
time.sleep(0.5)
# 断言
if "dotest" in tilte.text:
    print("登录成功")
else:
    print("登录失败")

#测试模块
browser.find_element_by_xpath("//nav[@id='navbar']//li[4]//a[1]").click()
time.sleep(0.5)
#Bug
browser.find_element_by_xpath("//ul[@class='nav nav-default']//a[contains(text(),'Bug')]").click()
#点击提交bug
#browser.refresh()
browser.find_element_by_xpath("//a[@class='btn btn-primary']").click()
time.sleep(0.5)


#所属模块（新版使用li隐藏标签）
browser.find_element_by_xpath("//div[@id='module_chosen']//a[@class='chosen-single']").click()
time.sleep(0.5)
ele1 = browser.find_element_by_xpath("//div[@class='chosen-drop chosen-auto-max-width chosen-no-wrap in']")
#ActionChains(browser).move_to_element(ele1).perform()
ele2 = browser.find_element_by_xpath("//div[@id='moduleIdBox']//li[2]")
ActionChains(browser).move_to_element(ele1).move_to_element(ele2).perform()
ele2.click()

#所属项目
browser.find_element_by_xpath("//div[@id='project_chosen']").click()
time.sleep(0.5)
ele3 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/span[1]/div[1]/div[1]/ul[1]/li[1]") 
ActionChains(browser).move_to_element(ele3).perform()
ele3.click()

#影响版本
browser.find_element_by_xpath("//div[@id='openedBuild_chosen']").click()
time.sleep(0.5)
ele4 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]")
ele5 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[1]/div[1]/ul[1]/li[3]")
ActionChains(browser).move_to_element(ele4).move_to_element(ele5).perform()
ele5.click()
time.sleep(0.5)

#当前指派
browser.find_element_by_xpath("//div[@id='assignedTo_chosen']").click()
time.sleep(0.5)
ele6 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]/div[1]/ul[1]")
ele7 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]/div[1]/ul[1]/li[3]")
ActionChains(browser).move_to_element(ele6).move_to_element(ele7).perform()
ele7.click()
time.sleep(0.5)

#Bug标题
browser.find_element_by_xpath("//div[@class='input-control has-icon-right required']//input[@id='title']").send_keys("UI自动化测试，提交bug！")

#严重程度:1
browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[2]/button[1]").click()
time.sleep(0.5)
ele8 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[2]/div[1]/div[1]")
ele9 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[2]/div[1]/div[1]/span[1]")
ActionChains(browser).move_to_element(ele8).move_to_element(ele9).perform()
ele9.click()
time.sleep(0.5)

#优先级:1
browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[3]/button[1]").click()
time.sleep(0.5)
ele10 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[3]/div[1]/div[1]")
ele11 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[3]/div[1]/div[1]/span[1]")
ActionChains(browser).move_to_element(ele10).move_to_element(ele11).perform()
ele11.click()
time.sleep(0.5)


#重现步骤
frameid = browser.find_element_by_xpath("//iframe[@class='ke-edit-iframe']")
browser.switch_to.frame(frameid)
browser.find_element_by_xpath('/html/body').clear()  #清空；对元素的操作
browser.find_element_by_xpath('/html/body').send_keys("登录禅道测试账号，提交bug。")
browser.switch_to.default_content()
time.sleep(0.5)

#点击保存功能
browser.find_element_by_xpath("//button[@id='submit']").click()  

#退出浏览器
browser.quit() 

