import xlrd

'''衣服种类'''
def clothes():
    wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx')
    a = []
    for i in range(12):
        wb_view = wb.sheet_by_index(i)
        rows = wb_view.nrows
        for j in range(1,rows):
            if wb_view.cell_value(j,1) not in a :
                a.append(wb_view.cell_value(j,1))
    return a
'''全年销售量'''
def total():
    sum = 0
    wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx')
    for  i in range(12):
        wb_view = wb.sheet_by_index(i)
        rows = wb_view.nrows
        for j in range(1,rows):
            sum += wb_view.cell_value(j,4)
    return sum

'''全年的销售总额'''

def Total_sales():
    wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx')
    sum = 0
    for i in range(12):
        wb_view = wb.sheet_by_index(i)
        rows = wb_view.nrows
        for j in range(1,rows):
            sum += wb_view.cell_value(j,2) * wb_view.cell_value(j,4)
    print('2020年销售总额是：￥',sum)

'''每件衣服的销售（件数）占比'''
def compare():
    wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx')
    for k in range(len(clothes())):
        total = 0
        test_object = 0
        for i in range(12):
            wb_view = wb.sheet_by_index(i)
            rows = wb_view.nrows
            for j in range(1,rows):
                total = total + wb_view.cell_value(j,4)
                if clothes()[k] == wb_view.cell_value(j,1):
                    test_object = test_object + wb_view.cell_value(j,4)
        print(clothes()[k],'的全年销售占比为','{:.2%}'.format(test_object/total))

'''每件衣服的月销售占比'''
def month_compare():
    wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx')
    for k in range(len(clothes())):
        for i in range(12):
            wb_view = wb.sheet_by_index(i)
            month_total = 0
            test_object = 0
            rows = wb_view.nrows
            for j in range(1,rows):
                month_total += wb_view.cell_value(j,4)
                if clothes()[k] == wb_view.cell_value(j,1):
                    test_object += wb_view.cell_value(j,4)
            print(clothes()[k],'的',i+1,'月销售占比为','{:.2%}'.format(test_object/month_total))

'''每件衣服的销售额占比'''
def sales_volume():
    wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx')
    for k in range(len(clothes())):
        total1 = 0
        test_object = 0
        for i in range(12):
            wb_view = wb.sheet_by_index(i)
            rows = wb_view.nrows
            for j in range(1,rows):
                total1 = total1 + wb_view.cell_value(j,4) * wb_view.cell_value(j,2)
                if clothes()[k] == wb_view.cell_value(j,1):
                    test_object = test_object + wb_view.cell_value(j,4) * wb_view.cell_value(j,2)
        print(clothes()[k],'的全年销售额占比为','{:.2%}'.format(test_object/total1))


'''最畅销的衣服是那种'''
def Best_seller():
    wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx')
    target = ''
    temporary = 0
    for k in range(len(clothes())):
        test_object = 0
        for i in range(12):
            wb_view = wb.sheet_by_index(i)
            rows = wb_view.nrows
            for j in range(1, rows):
                if clothes()[k] == wb_view.cell_value(j,1):
                    test_object += wb_view.cell_value(j,4)
        if test_object / total() > temporary:
            temporary = test_object / total()
            target = clothes()[k]
    print('最畅销的衣服是',target)


'''每个季度最畅销的衣服'''
def season():
    wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx')
    target_chun = ''
    target_xia = ''
    target_qiu = ''
    target_dong = ''
    temporary_chun = 0
    temporary_xia = 0
    temporary_qiu = 0
    temporary_dong = 0
    for k in range(len(clothes())):
        total = 0
        test_object = 0
        for i in range(12):
            wb_view = wb.sheet_by_index(i)
            rows = wb_view.nrows
            if 3<=i <=5:
                for j in range(1,rows):
                    total = total + wb_view.cell_value(j, 4)
                    if clothes()[k] == wb_view.cell_value(j, 1):
                        test_object += wb_view.cell_value(j, 4)
                if test_object / total > temporary_chun:
                    temporary_chun = test_object / total
                    target_chun = clothes()[k]
            if 6<=i<=8:
                for j in range(1, rows):
                    total = total + wb_view.cell_value(j, 4)
                    if clothes()[k] == wb_view.cell_value(j, 1):
                        test_object += wb_view.cell_value(j, 4)
                if test_object / total > temporary_xia:
                    temporary_xia = test_object / total
                    target_xia = clothes()[k]
            if 9<=i<=11:
                for j in range(1, rows):
                    total = total + wb_view.cell_value(j, 4)
                    if clothes()[k] == wb_view.cell_value(j, 1):
                        test_object += wb_view.cell_value(j, 4)
                if test_object / total > temporary_qiu:
                    temporary_qiu = test_object / total
                    target_qiu = clothes()[k]
            if 1<=i<=2  or i ==12 :
                for j in range(1, rows):
                    total = total + wb_view.cell_value(j, 4)
                    if clothes()[k] == wb_view.cell_value(j, 1):
                        test_object += wb_view.cell_value(j, 4)
                if test_object / total > temporary_dong:
                    temporary_dong = test_object / total
                    target_dong = clothes()[k]
    print('春季最畅销的衣服是：',target_chun,'春季销售数量占比为：','{:.2%}'.format(temporary_chun))
    print('夏季最畅销的衣服是：', target_xia, '夏季销售数量占比为：', '{:.2%}'.format(temporary_xia))
    print('秋季最畅销的衣服是：', target_qiu, '秋季销售数量占比为：', '{:.2%}'.format(temporary_qiu))
    print('冬季最畅销的衣服是：', target_dong, '冬季销售数量占比为：', '{:.2%}'.format(temporary_dong))

'''全年销量最低的衣服'''
def min_seller():
    wb = xlrd.open_workbook('2020年每个月的销售情况.xlsx')
    target = ''
    temporary = []
    for k in range(len(clothes())):
         test_object = 0
         for i in range(12):
             wb_view = wb.sheet_by_index(i)
             rows = wb_view.nrows
             for j in range(1,rows):
                 if clothes()[k] == wb_view.cell_value(j, 1):
                     test_object += wb_view.cell_value(j, 4)
         temporary.append(test_object / total())

    a = temporary.index(min(temporary))
    print('全年销量最低的衣服是：',clothes()[a])








