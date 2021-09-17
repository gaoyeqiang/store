import random
k=0
shop = [

    ["机械革命"   ,   15000],
    ["HUAWEI watch", 1200],
    ["MAC PC",       13000],
    ["Iphone 54 plus",45000],
    ["辣条"           ,2.5],
    ["老干妈"          ,13]
]
mycart = []
money=input('请充值金额￥:')
if money.isdigit():
    money = int(money)
    free = random.randint(0, 3)
    if free < 1:
        k = 0
        j = 1
        print('恭喜您抽到3折辣条优惠券')
    else:
        print('恭喜您抽到9折机械革命优惠券')
        k = 1
        h = 1
    while 1:

        for i,j in enumerate(shop):
            print(i,j)
        chose=input('请输入想要的商品编号：')
        if chose.isdigit():
            chose=int(chose)
            if chose<len(shop)-1:
                if money>=shop[chose][1]:
                    mycart.append(shop[chose])
                    if k==0 and shop[chose][0]== "辣条" and j<=10:
                        money-=shop[chose][1]*0.3
                        j+=1
                    elif k==1 and shop[chose][0]=="机械革命" and h<=20:
                        money-=shop[chose][1]*0.9
                        h+=1
                    else:money-=shop[chose][1]
                else:print('您的余额不足')
            else:print('您输入的商品不存在！')
        elif chose == 'q' or chose == 'Q':
            break
        else:print('输入非法！')
else:print('请输入正确的数值！')

count = []

for key,value  in enumerate(mycart):

    if value in mycart[:key]:
        continue
    count.append(mycart.count(mycart[key]))


mycart = list(set([tuple(t) for t in mycart]))

for k in mycart:
    mycart[mycart.index(k)] = list(k)
print(count)
print("以下是您的购物小条，请拿好！")
print("---------------------------------------")
for key,value  in enumerate(mycart):
    print(key,"------",value[0],"  价格：￥",value[1],"  数量:",count[key])
print("---------------------------------------")
print("您的余额还剩：￥",money)