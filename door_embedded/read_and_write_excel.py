#coding:utf-8
import xlrd
import xlwt
import xlsxwriter

#文件路径
file_path='d:/test.xlsx'
#打开Excel文件读取数据
data=xlrd.open_workbook(file_path)
#获取一个工作表
table_read=data.sheets()[1]  #通过索引顺序获取
#新建一个xlsx文件
xlsx=xlsxwriter.Workbook('d:/a.xlsx')
#新建一个sheet
table_write=xlsx.add_worksheet('Sheet1')
#获取行数和列数
nrow=table_read.nrows
# print(nrow)
ncolumn=table_read.ncols
# print(ncolumn)
#循环获取列表数据
for y in range(nrow):
    for x in range(ncolumn):
        print(table_read.cell(y,x).value)
        if table_read.cell(y,x).value!=None and table_read.cell(y,x).value!='' and table_read.cell(y,x).value!='\n':
            if isinstance(table_read.cell(y,x).value,float) and table_read.cell(y,x).value<100000:
                table_write.write(y,x,'0'+str(int(table_read.cell(y,x).value)))
            else:
                table_write.write(y,x,table_read.cell(y,x).value)
#关闭xlsx
xlsx.close()
