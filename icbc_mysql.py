import pymysql
import random
con = pymysql.connect(host='localhost',user='root',password='1234',database='bank')
cousor = con.cursor()
welcome = '''
-------------------以下是本银行的业务选项-------------------
------------------------1：开户--------------------------
------------------------2：存款--------------------------
------------------------3：取款--------------------------
------------------------4：转账--------------------------
------------------------5：查询--------------------------
------------------------6：退出--------------------------
'''
def update(sql,param):
    con = pymysql.connect(host='localhost', user='root', password='1234', database='bank')
    cousor = con.cursor()
    cousor.execute(sql,param)
    con.commit()
    cousor.close()
    con.close()

def select(sql,param,mode='all',size=1):
    con = pymysql.connect(host='localhost', user='root', password='1234', database='bank')
    cousor = con.cursor()
    cousor.execute(sql,param)
    if mode == 'all':
       return cousor.fetchall()
    elif mode == 'one' or 1:
        return cousor.fetchone()
    elif mode == 'many':
        return cousor.fetchmany()
    con.commit()
    cousor.close()
    con.close()
def bank_add(account,username,password,country,province,street,gate,bankname,money):

    q=select('select count(*) from icbc',())
    q=q[0][0]
    print(q)
    if q >=100:
        return 0

    if select('select * from icbc where account=%s',(account)) == 1:
        return 1

    update ('insert into icbc values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(account,username,password,country,province,street,gate,bankname,money))

    return 2
def addmoney():
    account=input('请输入存款账户：')
    if account.isdigit():
        account=int(account)
        if select ('select count(*) from icbc where account=%s',(account))[0][0] == 1:
            money=input('请输入存款金额：')
            if money.isdigit():
                money = int(money)
                update('update icbc set money = money + %s where account = %s',(money,account))

                yue=select('select money from icbc where account=%s',(account),mode='one')[0]

                username=select('select username from icbc where account = %s',(account),mode='one')
                username = username[0]

                info = '''
                账号：%s
                用户名：%s
                余额：%s
                '''
                print(info%(account,username,yue))

            else:print('输入非法！')
        else:print('您输入的账号不存在！')
    else:print('输入非法！')

def takemoney():
    account=input('请输入账户：')
    if account.isdigit():
        account=int(account)
        if select('select count(*) from icbc where account=%s',(account)) == 1:
            password = input('请输入密码：')
            password1=select('select password from icbc where account = %s',(account),mode='one')
            password1 = password[0]
            if password == password1:
                money = input('请输入取款金额：')
                if money.isdigit():
                    money = int(money)
                    money1= cousor.execute('select money from icbc where account = %s',(account))
                    money1 = cousor.fetchone()[0]
                    if money <= money1:
                        cousor.execute('update icbc set money = money - %s where account = %s',(money,account))
                        con.commit()
                        yue = cousor.execute('select money from icbc where account = %s',(account))
                        yue = cousor.fetchone()[0]
                        username = cousor.execute('select username from icbc where account = %s', (account))
                        username = cousor.fetchone()[0]
                        print(yue)
                        info = '''
                        账号：%s
                        用户名：%s
                        余额：%s
                        '''
                        print(info % (account, username, yue))
                    else:print('余额不足！')
                else:print('输入非法！')
            else:print('密码错误！')
        else:print('您输入的账号不存在！')
    else:print('输入非法！')

def givemoney():
    gaccount=input('请输入转出账户：')
    if gaccount.isdigit():
        gaccount = int(gaccount)
        if cousor.execute('select * from icbc where account = %s' ,(gaccount)) == 1 :
            gpassword = input('请输入密码：')
            gpassword1 = cousor.execute('select password from icbc where account = %s',(gaccount))
            gpassword1 = cousor.fetchone()[0]
            if gpassword1 == gpassword:
                raccount = input('请输入收款账户：')
                if raccount.isdigit():
                    raccount = int(raccount)
                    if cousor.execute('select account from icbc where account = %s',(raccount)) == 1:
                        money = input('请输入转账金额：')
                        if money.isdigit():
                            money = int(money)
                            money1 = cousor.execute('select money from icbc where account = %s', (gaccount))
                            money1 = cousor.fetchone()[0]
                            if money <= money1:
                                cousor.execute('update icbc set money = money + %s where account = %s',(money,raccount))
                                cousor.execute('update icbc set money = money - %s where account = %s',(money,gaccount))
                                con.commit()
                                yue = cousor.execute('select money from icbc where account = %s', (gaccount))
                                yue = cousor.fetchone()[0]
                                username = cousor.execute('select username from icbc where account = %s', (gaccount))
                                username = cousor.fetchone()[0]
                                print(yue)
                                info = '''
                                账号：%s
                                用户名：%s
                                余额：%s
                                转出金额：%s
                                '''
                                print(info % (gaccount, username, yue,money))
                            else:print('余额不足！')
                        else:print('输入非法！')
                    else:print('您输入的收款账户不存在！')
                else:print('输入非法！')
            else:print('密码错误！')
        else:print('您输入的账户不存在！')
    else:print('输入非法！')

def look():
    account = input('请输入账户：')
    if account.isdigit():
        account = int(account)
        if cousor.execute('select * from icbc where account = %s ',(account)) == 1:
            password = input('请输入密码：')
            password1 = cousor.execute('select password from icbc where account = %s', (account))
            password1 = cousor.fetchone()[0]
            if password1 == password:
                mation = cousor.execute('select * from icbc where account = %s', (account))
                mation = cousor.fetchall()
                info = '''
                账号：%s
                用户名：%s
                密码：%s
                余额：%s
                开户行：%s
                地址：
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                '''
                account = mation[0][0]
                username = mation[0][1]
                password = mation[0][2]
                country = mation[0][3]
                province = mation[0][4]
                street = mation[0][5]
                gate = mation[0][6]
                bankname = mation[0][7]
                yue = mation[0][8]
                print(info%(account,username,password,country,province,street,gate,bankname,yue))
            else:print('密码错误！')
        else:print('您输入的账号不存在！')
    else:print('输入非法！')




def adduser():
    account = random.randint(10000000,100000000)
    username = input('请输入用户名：')
    password = input('请创建密码：')
    country = input('请输入国家：')
    province = input('请输入省份：')
    street = input('请输入街道：')
    gate = input('请输入门牌号：')
    bankname = '中国工商银行昌平回龙观支行'
    money = int(input('请输入初始余额：'))
    status = bank_add(account,username,password,country,province,street,gate,bankname,money)
    if status == 0:
        print('库已满')
    elif status == 1:
        print('已创建')
    else:
        print('开户成功')
        info = '''
          ----------------个人信息----------------
          用户名：%s
          账户：%s
          密码：%s
          国家：%s
          省份：%s
          街道：%s
          门牌号：%s
          余额：%s
          开户行名称：%s
          '''
        print(info % (username, account, password, country, province, street, gate, money, bankname))


while 1 :
    print(welcome)
    i = input('请输入您的业务号：')
    if i == '1':
        adduser()
    elif i == '2':
        addmoney()
    elif i == '3':
        takemoney()
    elif i == '4':
        givemoney()
    elif i == '5':
        look()
    elif i == '6':
        print('期待您的下次光临！')
        cousor.close()
        con.close()
        break
    else:
        print('您输入的业务号码有错，请重新输入！')

