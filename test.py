from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.jd.com')
driver.find_element_by_xpath('//*[@id ="key"] ').send_keys('刻晴键盘')
driver.find_element_by_xpath('//*[@clstag = "h|keycount|head|search_a" and @class = "button"]').click()
# driver.find_element_by_xpath('//*[@class = "link-login"]').click()
time.sleep(3)
search_window = driver.current_window_handle

driver.find_element_by_xpath('//*[@data-sku = "10037361068277"]').click()
handles = driver.window_handles
for i in handles:
    if search_window == i:
        continue
    else:
        #将driver与新的页面绑定起来
        driver = driver.switch_to_window(i)
time.sleep(3)
driver.find_element_by_id('InitCartUrl').click()
# driver.find_element_by_id('loginname').send_keys('15057035189')
# driver.find_element_by_id('nloginpwd').send_keys('gyq147258')
# driver.find_element_by_id('loginsubmit').click()
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('file:///F:/Python%E8%87%AA%E5%8A%A8%E5%8C%96/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%9518/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6%E5%92%8C%E4%B8%8B%E6%8B%89%E5%88%97%E8%A1%A8/autotest.html')
# driver.find_element_by_id('accountID').send_keys('gyq')
# driver.find_element_by_id('passwordID').send_keys('123456')
# driver.find_element_by_id('areaID').send_keys('北京市')
# driver.find_element_by_id('sexID2').click()
# driver.find_element_by_xpath('//*[@value = "spring"]').click()
# driver.find_element_by_xpath('//*[@value = "winter"]').click()
# driver.find_element_by_xpath('//*[@name = "file"  and @type = "file"]').send_keys(r"F:\chrome\picture.jpg")
# driver.find_element_by_id('buttonID').click()
# time.sleep(3)
# driver.switch_to.alert.accept()

# driver.get(r'file:///F:/Python%E8%87%AA%E5%8A%A8%E5%8C%96/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%9518/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E5%BC%B9%E6%A1%86%E7%9A%84%E9%AA%8C%E8%AF%81/dialogs.html')
# driver.find_element_by_id('alert').click()
# time.sleep(3)
# driver.switch_to.alert.accept()
# time.sleep(2)
# driver.find_element_by_id('confirm').click()
# time.sleep(2)
# driver.switch_to.alert.accept()
# time.sleep(2)
# driver.find_element_by_id('confirm').click()
# time.sleep(2)
# driver.switch_to.alert.dismiss()
# driver.quit()
# driver.get('file:///F:/Python%E8%87%AA%E5%8A%A8%E5%8C%96/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%9518/%E7%BB%83%E4%B9%A0%E7%9A%84html/%E8%B7%B3%E8%BD%AC%E9%A1%B5%E9%9D%A2/pop.html')
# driver.find_element_by_id('goo').click()