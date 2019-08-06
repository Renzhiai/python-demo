import csv

sublist=[]
update_csv_path='C:/Users/zhiai.ren/Desktop/gy.csv'
new_csv_path='C:/Users/zhiai.ren/Desktop/new.csv'
with open(update_csv_path,'r') as csvf:
    #准备一个csv文件，写入整理的数据
    #添加一个参数 newline='' 防止空行,
    new_csv=open(new_csv_path,'w',newline='')
    writer=csv.writer(new_csv)

    #读取所有的csv文件内容
    readall=csv.reader(csvf)
    #逐行读取
    for columns in readall:
        desc=columns[2].split('\n')
        print(desc[0])
        if columns[5]=='' and columns[8]=='':
            new_line=columns[1]+':'+desc[0]
        if columns[5]!='' and columns[8]=='':
            new_line=columns[1]+'('+columns[5]+'):'+desc[0]
        if columns[5]=='' and columns[8]!='':
            new_line=columns[1]+'('+columns[8]+'):'+desc[0]
        if columns[5]!='' and columns[8]!='':
            new_line=columns[1]+'('+columns[8]+'/'+columns[5]+'):'+desc[0]
        sublist.append(new_line)
        writer.writerow(sublist)
        if len(sublist)!=0:
            sublist=[]
    new_csv.close()
