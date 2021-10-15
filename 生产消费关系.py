from threading import Thread
import time
import timeit
basket = 0
count1 = 0
class cooker(Thread):
    def run(self) -> None:
        global basket
        global count1
        count_else = 0
        while 1 :
            if basket < 500:
                count_else = 0
                basket += 1
                count1 += 1
            else:
                count_else += 1
                time.sleep(0.1)
                if count_else > 100:
                    print('总共做了',count1,'个汉堡！')
                    break
class eater(Thread):
    username = ''
    def run(self) -> None:
        global basket
        money = 10000
        count = 0
        while 1 :
            if money > 0:
                if basket > 0:
                    money -= 5
                    count += 1
                    basket -= 1
                else:
                    time.sleep(0.01)
            else:
                print(self.username,'抢了',count,'个汉堡！')
                break
c1 = cooker()
c1.start()
c2 = cooker()
c2.start()
c3 = cooker()
c3.start()
e1 = eater()
e1.username = '张三'
e1.start()
e2 = eater()
e2.username = '李四'
e2.start()
e3 = eater()
e3.username = '王五'
e3.start()
e4 = eater()
e4.username = '赵六'
e4.start()
e5 = eater()
e5.username = '刘七'
e5.start()
e6 = eater()
e6.username = '周八'
e6.start()
