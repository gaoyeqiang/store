from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.jd.com')
driver.find_element_by_xpath('//*[@id ="key"] ').send_keys('刻晴键盘')
driver.find_element_by_xpath('//*[@clstag = "h|keycount|head|search_a" and @class = "button"]').click()

time.sleep(3)
current_win = driver.current_window_handle#同页跳转
driver.find_element_by_css_selector('#J_goodsList > ul > li:nth-child(2) > div').click()
handls = driver.window_handles
print(handls)
driver.switch_to.window(handls[1])#不同页跳转
driver.find_element_by_id('InitCartUrl').click()
time.sleep(3)
current_windows = driver.current_window_handle
time.sleep(3)
driver.find_element_by_css_selector('#content > div.login-wrap > div.w > div > div.login-tab.login-tab-r').click()
driver.find_element_by_id('loginname').send_keys('15057035189')
driver.find_element_by_id('nloginpwd').send_keys('gyq147258')
driver.find_element_by_id('loginsubmit').click()
