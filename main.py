import unittest
from HTMLTestRunner import HTMLTestRunner
from threading import Thread
from testlogin import test_login

case_list = unittest.TestLoader().getTestCaseNames(test_login)
class main_test(Thread):
    title = ''
    description = ''
    classname = None
    casename = ''
    filename = ''
    def run(self) -> None:
        suite = unittest.TestSuite()#suite必须在run下面，否则会重复加载
        for i in case_list:
            if i.startswith(self.casename):
                suite.addTest(self.classname(i))
        runner = HTMLTestRunner.HTMLTestRunner(  title = self.title,
                    description = self.description,
                    verbosity= 1 ,
                    stream=open(self.filename,'w+',encoding='utf-8'))
        runner.run(suite)

test1 = main_test()
test1.title = '登陆失败的测试！'
test1.casename ='test_bad'
test1.classname = test_login
test1.description = '账号或密码错误！'
test1.filename = '测试报告1.html'
test1.start()

test2 = main_test()
test2.title = '正常登录的测试！'
test2.casename = 'test_success'
test2.classname = test_login
test2.description = '登录成功'
test2.filename = '测试报告2.html'
test2.start()

test3 = main_test()
test3.title = '密码为空的测试！'
test3.casename = 'test_none'
test3.classname = test_login
test3.description = '登录失败'
test3.filename = '测试报告3.html'
test3.start()
