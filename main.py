import unittest
from HTMLTestRunner import HTMLTestRunner
from threading import Thread
class main(Thread):
    pattern = ''
    def run(self) -> None:
        tests = unittest.defaultTestLoader.discover('./',self.pattern)
        runner = HTMLTestRunner.HTMLTestRunner(
            title='login登录测试',
            description='登录测试',
            verbosity= 1 ,
            stream=open('登陆测试.html','w+',encoding='utf-8')
        )
        runner.run(tests)
a = main()
a.pattern = 'testlogin.py'
a.start()


