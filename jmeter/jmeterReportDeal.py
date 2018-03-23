#coding:utf-8
import xlsxwriter

# 新建一个xlsx文件
xlsx = xlsxwriter.Workbook('d:/a.xlsx')
# 新建一个shee
table = xlsx.add_worksheet('Sheet1')
resultTxt = open('C:/Users/zhiai/Desktop/result.txt')
lines = resultTxt.readlines()
for i in range(len(lines)):
    for j in range(len(lines[i].split(','))):
        table.write(i, j, lines[i].split(',')[j])
# 关闭txt
resultTxt.close()
# 关闭xlsx
xlsx.close()