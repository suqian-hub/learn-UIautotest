from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

#from pywin32 import win32gui
#from pywin32 import win32con

driver = 'C:\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(executable_path = driver)
'''
Zentao-v12.0.1-64bit
'''
#打开网页
browser.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
time.sleep(2)
#用户名
browser.find_element_by_xpath("//*[@id='account']").send_keys("admin")
#密码
browser.find_element_by_xpath('//*[@id="loginPanel"]/div/div[2]/form/table/tbody/tr[2]/td/input').send_keys("Aa123456")

#登录
browser.find_element_by_xpath('//*[@id="submit"]').click()
#定位标题
browser.refresh()
tilte = browser.find_element_by_css_selector("body.m-my-index:nth-child(2) div:nth-child(1) div.container hgroup:nth-child(1) h1:nth-child(1) > a:nth-child(1)")
time.sleep(1)
# 断言
if "dotest" in tilte.text:
    print("登录成功")
else:
    print("登录失败")
time.sleep(1)

#测试模块
browser.find_element_by_xpath("//nav[@id='navbar']//li[4]//a[1]").click()
time.sleep(1)
#Bug
browser.find_element_by_xpath("//ul[@class='nav nav-default']//a[contains(text(),'Bug')]").click()
#点击提交bug
#browser.refresh()
browser.find_element_by_xpath("//a[@class='btn btn-primary']").click()
time.sleep(1)

'''
select标签定位(旧版禅道v9.4）
使用index
若是操作隐藏的元素的话：style="display: none;"；【若不是隐藏的的话不需要js】
js = 'document.querySelectorAll("select")[0].style.display="block";'
driver.execute_script(js)
------
document.querySelectorAll("select")  选择所有的select。
[0] 指定这一组标签里的第几个。
style.display="block";  修改样式的display="block" ,表示可见。
执行完这句js代码后，就可以正常操作下拉框了。

index定位;导入：from selenium.webdriver.support.select import Select

选择所属模块
js = 'document.querySelectorAll("select")[1].style.display="block";'#[1]:从零开始查第几个就写几
browser.execute_script(js)

module =browser.find_element_by_xpath("//*[@id='module']")
Select(module).select_by_index(1) #选择下拉字典项的操作
'''
#所属模块（新版使用li隐藏标签）
browser.find_element_by_xpath("//div[@id='module_chosen']//a[@class='chosen-single']").click()
time.sleep(1)
ele1 = browser.find_element_by_xpath("//div[@class='chosen-drop chosen-auto-max-width chosen-no-wrap in']")
#ActionChains(browser).move_to_element(ele1).perform()
ele2 = browser.find_element_by_xpath("//div[@id='moduleIdBox']//li[2]")
ActionChains(browser).move_to_element(ele1).move_to_element(ele2).perform()
ele2.click()

#所属项目
browser.find_element_by_xpath("//div[@id='project_chosen']").click()
time.sleep(1)
ele3 = browser.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/span[1]/div[1]/div[1]/ul[1]/li[1]") 
ActionChains(browser).move_to_element(ele3).perform()
ele3.click()

#影响版本
time.sleep(5)
js = 'document.querySelectorAll("select")[3].style.display="block";'
browser.execute_script(js)
#
project = browser.find_element_by_xpath("//*[@id='openedBuild']")

Select(project).select_by_index(1)

#当前指派
time.sleep(5)
js = 'document.querySelectorAll("select")[4].style.display="block";'
browser.execute_script(js)

project = browser.find_element_by_xpath("//*[@id='assignedTo']")
Select(project).select_by_index(1)


#Bug标题
time.sleep(5)
browser.find_element_by_id(id_="title").send_keys("安卓-首页：logo显示不正确")

#严重程度:1
time.sleep(5)
browser.find_element_by_xpath("//*[@id='dataform']/table/tbody/tr[5]/td/div/div[2]/div/div[1]/button").click()   #点击严重程度按钮

time.sleep(5)
browser.find_element_by_xpath("//*[@id='dataform']/table/tbody/tr[5]/td/div/div[2]/div/div[1]/ul/li[1]/a/span").click()  #选择级别

#优先级:2
time.sleep(5)
browser.find_element_by_xpath('//*[@id="dataform"]/table/tbody/tr[5]/td/div/div[2]/div/div[2]/button').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="dataform"]/table/tbody/tr[5]/td/div/div[2]/div/div[2]/ul/li[3]/a/span').click()

'''
重新步骤
因为标签含有iframe；所以需要用其他的方法进行

多层框架或窗口
frame标签：frame标签有frameset、frame、iframe三种；frame、iframe需要切换，否则无法定位到；
1.iFrame有ID 或者 name的情况
driver.switch_to.frame("id或者name")
2:没有id or name需要用xpath定位
3.跳出iFrame
//跳出frame,进入default content;
dr.switchTo().defaultContent();
'''
#重现步骤
time.sleep(5)
frameid = browser.find_element_by_xpath('//*[@id="dataform"]/table/tbody/tr[6]/td/div[2]/div[2]/iframe') #使用xpath定位到iframe标签
browser.switch_to.frame(frameid) #dr.switch_to.frame切换至iframe标签；如果有id或name的话直接：driver.switch_to.frame('id')
browser.find_element_by_xpath('/html/body').clear()  #清空；对元素的操作
browser.find_element_by_xpath('/html/body').send_keys("这是内容")
#跳出iframe标签
browser.switch_to.default_content()


'''
元素类型为：hidden
调用js实现浏览器上下滑动及左右滑动
driver.execute_script('window.scrollTo(0,2500);')
纵向滑动：0,2500；0：顶部；2500：底部（2500-3000）

driver.execute_script('window.scrollTo(2500,0);')
横向滑动：2500,0；0：左；2500：右（2500-3000）
'''
browser.execute_script('window.scrollTo(0,2500);')   #滑动到底部
time.sleep(5)


'''
#上传附件：input类型

需要安装：pip install pypiwin32 完成后重启pycharm
导入：
import win32gui
import win32con
'''
#driver.find_element_by_xpath('//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').click()    #定位到上传功能
# win32gui
#time.sleep(5)
#dialog = win32gui.FindWindow('#32770', u'打开')  # 打开对话框
#ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
#ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
#Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
#button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
#time.sleep(5)
#win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\1.png')  # 往输入框输入绝对地址
#time.sleep(5)
#win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
#time.sleep(5)

#点击保存功能;拉动滚动条
browser.find_element_by_xpath("//*[@id='submit']").click()   #在点击底部的功能

browser.quit() #退出浏览器
