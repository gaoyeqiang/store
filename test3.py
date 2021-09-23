# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"],
#     ['刘备', '45', '男', '220', 'alibaba', 500, '30']
# ]


'''统计每个人的平均薪资'''
# avg=0
# sum=0
# for i in range(len(names)):
#     for j in range(len(names[0])):
#        if j==5:
#             sum+=names[i][j]
# avg=sum/len(names)
# print(avg)

'''统计每个人的平均年龄'''
# avg=0
# sum=0
# for i in range(len(names)):
#     for j in range(len(names[0])):
#        if j==1:
#             sum+=int(names[i][j])
# avg=sum/len(names)
# print(avg)

'''公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中'''
# a=[['刘备','45','男','220','alibaba',500,'30']]
# names.extend(a)
# print(names)

'''统计公司男女人数'''
# mans=0
# wumen=0
# for i in range(len(names)):
#     for j in range(len(names[0])):
#        if names[i][j]=='男':
#             mans+=1
#        elif names[i][j]=='女':
#            wumen+=1
# info='''
# 男性：%s人
# 女性：%s人
# '''
# print(info%(mans,wumen))

'''每个部门的人数'''

# while 1:
#     sum = 0
#     p = input('请输入要统计的部门编号：')
#     for i in range(len(names)):
#         for j in range(len(names[0])):
#             if names[i][j]==p:
#                sum+=1
#     print(sum)

'''现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业
的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必
须上交，所以大家上交作业的次数并不一致。'''
# a=[ ['罗恩', 23 ,35 ,44],
#     ['哈利' ,60, 77 ,68 ,88, 90],
#     ['赫敏', 97 ,99 ,89 ,91, 95, 90],
#     ['马尔福' ,100, 85 ,90] ]
# while 1:
#     name=input('请输入要统计的名字：')
#     score=0
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             if a[i][0]==name:
#                 if type(a[i][j])==int:
#                     score+=a[i][j]
#     print(score)

'''对购物车系统进行改造：
（1）	添加登陆功能，登陆后才能进行购物操作。
（2）	添加结算积分添加功能。
（3）	登陆成功后系统随机分发一张优惠券（免单券6张，免半券3张，满600减100券50张，
        满10000减1000券10张，无券）前提是优惠券存在列表中。
'''
# import random
# k=0
# shop = [
#
#     ["机械革命"   ,   15000],
#     ["HUAWEI watch", 1200],
#     ["MAC PC",       13000],
#     ["Iphone 54 plus",45000],
#     ["辣条"           ,2.5],
#     ["老干妈"          ,13]
# ]
# mycart = []
# money=input('请充值金额￥:')
# if money.isdigit():
#     money = int(money)
#     free = random.randint(0, 3)
#     if free < 1:
#         k = 0
#         j = 1
#         print('恭喜您抽到3折辣条优惠券')
#     else:
#         print('恭喜您抽到9折机械革命优惠券')
#         k = 1
#         h = 1
#     while 1:
#
#         for i,j in enumerate(shop):
#             print(i,j)
#         chose=input('请输入想要的商品编号：')
#         if chose.isdigit():
#             chose=int(chose)
#             if chose<len(shop)-1:
#                 if money>=shop[chose][1]:
#                     mycart.append(shop[chose])
#                     if k==0 and shop[chose][0]== "辣条" and j<=10:
#                         money-=shop[chose][1]*0.3
#                         j+=1
#                     elif k==1 and shop[chose][0]=="机械革命" and h<=20:
#                         money-=shop[chose][1]*0.9
#                         h+=1
#                     else:money-=shop[chose][1]
#                 else:print('您的余额不足')
#             else:print('您输入的商品不存在！')
#         elif chose == 'q' or chose == 'Q':
#             break
#         else:print('输入非法！')
# else:print('请输入正确的数值！')
#
# count = []
#
# for key,value  in enumerate(mycart):
#
#     if value in mycart[:key]:
#         continue
#     count.append(mycart.count(mycart[key]))
#
#
# mycart = list(set([tuple(t) for t in mycart]))
#
# for k in mycart:
#     mycart[mycart.index(k)] = list(k)
# print(count)
# print("以下是您的购物小条，请拿好！")
# print("---------------------------------------")
# for key,value  in enumerate(mycart):
#     print(key,"------",value[0],"  价格：￥",value[1],"  数量:",count[key])
# print("---------------------------------------")
# print("您的余额还剩：￥",money)

'''程序执行结果'''
'''
1
2
3
4
5
'''
# num=int(input())
# while num !=0:
#     print(num % 10)
#     num = num // 10

'''请对下列列表进行冒泡排序'''
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
# for i in range(len(a)-1):#0~12
#     for j in range(len(a)-i-1):#range:12~0
#         if a[j]<a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)
