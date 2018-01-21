# coding:utf-8
import xlrd
import xlsxwriter
import os

#待处理文件路径(创建好文件夹)
file_path='d:/excel_deal/'
#处理结果路径(创建好文件夹)
file_copy_path='d:/excel_copy/'
#获取对应目录下所有文件
for filename in os.listdir(file_path):
    #如果该目录下，有文件后缀名为xlsx或者xls就处理该文件
    if os.path.splitext(filename)[1]=='.xlsx' or os.path.splitext(filename)[1]=='.xls':
        #打开Excel文件读取数据
        data=xlrd.open_workbook(file_path+filename)
        #获取一个工作表
        table=data.sheets()[0]  #通过索引顺序获取
        #获取行数和列数
        nrow=table.nrows
        ncolumn=table.ncols
        #新建一个xlsx文件
        xlsx=xlsxwriter.Workbook(file_copy_path+'copy_'+filename)
        #新建一个sheet
        table_copy=xlsx.add_worksheet('Sheet1')
        #关键字
        keywords=['BHX1','CWL1','EDI4','EUK5','GLA1','LTN1','LTN2','LTN3','LTN4','LBA1','XUKA','XUKD','MAN1']
        #去掉空格，定义一个新的行号
        row=-1
        new_rows=[]
        #循环获取列表数据
        for i in range(nrow):
            #如果AV列有Amazon.co.uk，AT列有以上关键字
            if table.cell(i,47).value==u'Amazon.co.uk' and table.cell(i,45).value in keywords:
                row=row+1
                for j in range(ncolumn):
                    table_copy.write(row,j,table.cell(i,j).value)
        xlsx.close()