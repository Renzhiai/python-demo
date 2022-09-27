import xlrd
import xlwt
import xlsxwriter

#文件路径
file_path='C:/Users/zhiai.ren/Desktop/a.xlsx'
#打开Excel文件读取数据
data=xlrd.open_workbook(file_path)
#获取一个工作表
#table=data.sheets()[0]  #通过索引顺序获取
table=data.sheet_by_name('abc')    #通过名字获取
#获取整行和整列的值，返回list
row=table.row_values(1)
print(row)
column=table.col_values(0)
print(column)
#获取行数和列数
nrow=table.nrows
print(nrow)
ncolumn=table.ncols
print(ncolumn)
#循环获取列表数据
for i in range(nrow):
    print(table.row_values(i))
#获取某个单元格的值
cell_1A=table.cell(0,0).value
cell_4B=table.cell(3,1).value
print(cell_1A,cell_4B)
#获取索引
cell_1A=table.row(0)[0].value
print(cell_1A)
cell_1A=table.row_values(0)[0]
print(cell_1A)

'''
#写入
row=1
column=2
ctype=1
value='nihao'
xf=1
table.put_cell(row,column,ctype,value,xf)
'''
'''
#新建一个xls文件
xls=xlwt.Workbook()
#新建一个sheet
table=xls.add_sheet('Sheet1')
#写入数据
table.write(0,0,'哈哈')
#保存
xls.save('d:/a.xls')
'''

#新建一个xlsx文件
xlsx=xlsxwriter.Workbook('d:/a.xlsx')
#新建一个shee
table=xlsx.add_worksheet('Sheet1')
#写入数据
table.write(0,0,'你好')
#关闭xlsx
xlsx.close()
