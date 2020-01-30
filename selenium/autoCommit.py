#-*- coding:utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

'''
V1.0实现自动化点击工时确认
1、添加chrome_driver驱动路径
'''
chrome_driver=r"D:\Program Files\Python3.8\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"#后面要修改为相对路径
driver=webdriver.Chrome(executable_path=chrome_driver)

driver.get("http://172.29.10.30/xmgl/index.jsp")

#登录模块
driver.find_element_by_id('opcode').clear()
driver.find_element_by_id('opcode').send_keys('Y01923')
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys('xueshan007')
driver.find_element_by_id('b-submit').click()
time.sleep(3)#此处睡三秒，有同事没有修改密码，此处让其有时间手动点击
#点击左侧：工时管理--工时确认
driver.find_element_by_id('menu-tree_4_switch').click()
time.sleep(1)
print("sleep1秒后，点击工时确认按钮")
driver.find_element_by_id('menu-tree_10_a').click()

#对右侧的工时确认列表进行循环点击确认
time.sleep(1)
driver.switch_to.frame("main-frame")
print("执行到main-frame这一步了")

while driver.find_element_by_tag_name('a') != '':
    #点击每一行需要确认工时的日期
    time.sleep(1)
    driver.find_element_by_tag_name('a').click()
    #点击所有工时复选框，点击工时确认按钮
    time.sleep(1)
    driver.find_element_by_id('checkall').click()
    driver.find_element_by_id('b_commit').click()
    #处理alter
    # 获得警告框
    alert = driver.switch_to.alert#返回一个对象,里面有accept()和dismiss()
    print(alert.text)
    alert.accept()
    #第二个警告窗，确认按钮
    alert = driver.switch_to.alert#返回一个对象,里面有accept()和dismiss()
    alert.accept()
    #返回到工时确认首页
    time.sleep(1)
'''
#定义获取表格列表的数据
def get_dept_list(self):
    row = self.driver.find_elements_by_tag_name('tr')
    list=[]
    for i in row:
        j=i.find_elements_by_tag_name('td')
        for item in j:
            text=item.text
            list.append(text)
    return list
#可会获取到行的数据了
row = driver.find_elements_by_tag_name('tr')
list1=[]
for i in row:
    j=i.find_elements_by_tag_name('td')
    for item in j:
        text=item.text
        list1.append(text)
print(list1)

#可以获取到日历中
js_value = 'document.getElementById("workdate1").value="2020-01-23";'
driver.execute_script(js_value)
js_value = 'document.getElementById("workdate2").value="2020-01-23";'
driver.execute_script(js_value)
driver.find_element_by_id('b_query').click()
'''




