import random
bank_name='中国工商银行'
bank={}
welcome='''
------------------欢迎使用中国工商银行系统------------------

------------------------1.开户--------------------------
------------------------2.存款--------------------------
------------------------3.取款--------------------------
------------------------4.转账--------------------------
------------------------5.查询--------------------------
------------------------6.退出--------------------------
'''
def bank_add(username,password,country,provicen,street,door,money,account,bank_name):
    if len(bank)>=100:
        return 3
    if account in bank:
        return 2

    bank[account]={
    'username':username,
    'password':password,
    'country':country,
    'provicen':provicen,
    'street':street,
    'door':door,
    'money':money,
    'bank_name':bank_name
    }
    return 1





def user_add():
    username=input('请输入您的用户名：')
    password=input('请输入您的密码：')
    country=input('请输入您所在的国家：')
    provicen=input('请输入您所在的省份：')
    street=input('请输入您所在的街道：')
    door=input('请输入您的门牌号:')
    money=int(input('请输入您存入的金额￥：'))
    account=random.randint(10000000,100000000)
    status=bank_add(username,password,country,provicen,street,door,money,account,bank_name)
    if status==1:
        print('恭喜您开户成功！以下是您的账户信息！')
        info='''
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
        print(info%(username,account,password,country,provicen,street,door,money,bank_name))
    elif status==2:
        print('您的账户已创建，请勿重复创建！')
    elif status==3:
        print('当前账户数量已达上限，请去别的银行开户！')

def add_money():
    account=int(input('请输入要存款的账号：'))
    if account in bank:
        money = int(input('请输入存款金额：'))
        bank[account]['money'] += money
        info = '''
                用户名：%s
                账号:%s
                余额：%s
                '''
        print(info%(bank[account]['username'], account, bank[account]['money']))
    else:
        print('您输入的账号不存在')
        return 0

def take_money():
    account=int(input('请输入账号：'))
    if account in bank:
        password=input('请输入密码：')
        if password == bank[account]['password']:
            money=int(input('请输入取款金额￥'))
            if money <= bank[account]['money']:
                bank[account]['money'] -= money
                info='''
                用户名：%s
                账号：%s
                余额：%s
                '''
                print(info%(bank[account]['username'],account,bank[account]['money']))
            else:
                print('余额不足！')
                return 0
        else:
            print('密码错误！')
            return 0
    else:
        print('您输入的账号不存在！')
        return 0

def give_money():
    taccount=int(input('请输入转出账号：'))
    if taccount in bank:
        gaccount=int(input('请输入转入账号：'))
        if gaccount in bank:
            tpassword=input('请输入密码：')
            if tpassword == bank[taccount]['password']:
                tmoney=int(input('请输入转账金额￥：'))
                if tmoney <= bank[taccount]['money']:
                    bank[taccount]['money'] -= tmoney
                    bank[gaccount]['money'] += tmoney
                    info='''
                    用户名：%s
                    转出账号:%s
                    转入账号：%s
                    转出金额：%s
                    余额：%s
                    
                    '''
                    print(info%(bank[taccount]['username'],taccount,gaccount,tmoney,bank[taccount]['money']))
                else:
                    print('您的账户余额不足！')
                    return 0
            else:
                print('密码错误！')
                return 0
        else:
            print('您输入的账户不存在！')
            return 0
    else:
        print('您输入的账户不存在！')
        return 0

def query():
    account=int(input('请输入您的账户：'))
    if account in bank:
        password=input('请输入密码：')
        if password == bank[account]['password']:
            info='''
            --------------以下是您的个人信息---------------
            用户名：%s
            账号：%s
            密码：%s
            余额：%s
            地址：
                国家：%s
                省份：%s
                街道：%s
                门牌号：%s
            开户行：%s
            --------------------------------------------
            '''
            print(info%(bank[account]['username'],account,password,bank[account]['money'],
                        bank[account]['country'],bank[account]['provicen'],bank[account]['street']
                        ,bank[account]['door'],bank_name))
        else:
            print('密码错误！')
            return 0
    else:
        print('您输入的账号不存在！')
        return 0




while 1:
    print(welcome)
    i=input('请输入您要选择的业务:')
    if i=='1':
        user_add()
    elif i=='2':
        add_money()
    elif i=='3':
        take_money()
    elif i=='4':
        give_money()
    elif i=='5':
        query()
    elif i=='6':
        print('欢迎使用本系统！期待您下次光临！')
        break
    else:print('请输入正确的业务号！')