import unittest
from selenium import webdriver
from ddt import ddt,data,file_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://localhost:8080/HKR')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id('loginname').send_keys('paomorufeng')
driver.find_element_by_id('password').send_keys('gyq147258')
driver.find_element_by_id('submit').click()
driver.find_element_by_id('img').click()
driver.find_element_by_id('file1').send_keys(r'D:\LenovoSoftstore\Install\Steam\steamapps\workshop\content\431960\838533010\1.jpg')
driver.find_element_by_id('pic_btn').click()
