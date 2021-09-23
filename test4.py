# dict = {"k1":"v1","k2":"v2","k3":"v3"}
'''请循环遍历出所有的key'''
# # for i in dict:
# #     print(i,'value:',dict[i])
# #
# # '''请循环遍历出所有的value'''
# # for key,value in dict.items():
# #     print(key,'value:',value)
# '''请在字典中增加一个键值对,"k4":"v4"'''
# dict['k4']='v4'
# print(dict)

'''小明去超市购买水果，账单如下.请将上面的数据存储到字典里，
可以根据水果名称查询购买这个水果的费用
用水果名称做key，金额做value，创建一个字典
'''
# Friuts = {
# 	'苹果':12.3,  # 水果和单价
# 	'草莓':4.5,
#        '香蕉':6.3,
#        '葡萄':5.8,
#        '橘子':6.4,
#        '樱桃':15.8}


'''编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3} '''
# a=[21,56,21,10,21,56,56,56,56,10,56,56,10,56,56]
# # def tongji(a,b,c):
# c={}
# b=[]
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# for i in range(len(b)):
#     c[b[i]]=a.count(b[i])
# print(c)

'''有以下公司员工信息，将数据转换为字典方式（姓名作为键，
其他作为值,张三:{xxx:xxx,xx:xxx}）'''
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
]
a=[]
names_dict={}
for i in range(len(names)):
    a.append([])
print(a)
for i in range(len(names)):
    for j in range(1,len(names[i])):
        a[i].append(names[i][j])
print(a)
for i in range(len(names)):

    for j in range(1,len(names[i])):

        names_dict[names[i][0]]=a[i]
print(names_dict)