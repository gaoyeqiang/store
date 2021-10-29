import unittest
from selenium import webdriver
from ddt import ddt,data,file_data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from threading import Thread
import time

@ddt
class test_login(unittest.TestCase):
    def setUp(self) :
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/HKR')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def tearDown(self) :
        self.driver.quit()
    def do_input(self,username = None,password = None):
        if username:
            self.driver.find_element_by_id('loginname').send_keys(username)
        if password:
            self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('submit').click()
    def get_success_result(self):
        return self.driver.title
    def get_bad_resule(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                expected_conditions.presence_of_element_located((By.ID,'msg_uname'))
            )#等待最长10秒直到id为msg_uname的元素出现
            return element.text
        except Exception:
            pass
    def get_none_pwd(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                expected_conditions.presence_of_element_located((By.ID,'msg_pwd'))
            )
            return element.text
        except Exception:
            pass
    # @unittest.skip
    @file_data('bad.yaml')
    def test_bad(self,**userdata):
        username = userdata['username']
        password = userdata['password']
        excepted = userdata['except']
        self.do_input(username,password)
        self.assertEqual(self.get_bad_resule(),excepted)

    # @unittest.skip
    @file_data('normal.yaml')
    # @unittest.skip
    def test_success(self,**userdata):
        username = userdata['username']
        password = userdata['password']
        excepted = userdata['except']
        self.do_input(username,password)
        self.assertEqual(self.get_success_result(),excepted)
    @file_data('none.yaml')
    def test_none(self,**userdata):
        username = userdata['username']
        password = userdata['password']
        excepted = userdata['except']
        self.do_input(username,password)
        self.assertEqual(self.get_none_pwd(),excepted)
# class testboy(Thread,test_login):
#     @file_data('normal.yaml')
#     def run(self) -> None:
#         super(test_login.test_success())
if __name__ == '__main__':
    unittest.main()
# testboy().start()