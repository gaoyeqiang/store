import xlrd
import pymysql
def update(sql,parame):
    con = pymysql.connect(host='localhost', user='root', password='1234', database='excel_to_db')
    couser = con.cursor()
    couser.execute(sql,parame)
    con.commit()
    couser.close()
    con.close()
def create_table(bookname,page):
    wb = xlrd.open_workbook(bookname)
    for i in range(page):
        wb_view = wb.sheet_by_index(i)
        cols = wb_view.ncols
        print(i+1,'月',cols)
        update('create table %s月的销售情况 (`%s` varchar (20))',(i+1,wb_view.cell_value(0,0)))
        for j in range(1,cols):
            print('shangmian',j)
            update('alter table %s月的销售情况 add `%s`varchar (20)',(i+1,wb_view.cell_value(0,j)))
            print('xiamian',j)

create_table('2020年每个月的销售情况.xlsx',12)
def excel_to_db(bookname,page):
    wb = xlrd.open_workbook(bookname)
    for i in range(page):
        wb_view = wb.sheet_by_index(i)
        rows = wb_view.nrows
        cols = wb_view.ncols
        for j in range(1,rows):
            prame = [i + 1]
            for k in range(cols):
                prame.append(wb_view.cell_value(j,k))
                print(prame)
            update('insert into %s月的销售情况 values (%s,%s,%s,%s,%s)',prame)
excel_to_db('2020年每个月的销售情况.xlsx',12)