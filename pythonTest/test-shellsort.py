#coding:utf-8
import random
import time

'''''
随机生成0~10000000之间的数值
'''
def getrandata(num):
    a=[]
    i=0
    while i<num:
        a.append(random.randint(0,100))
        i+=1
    return a

def shellSort(arr):
    dist=len(arr)/2
    while dist>0:
        for i in range(dist,len(arr)):
            tmp=arr[i]
            while i>=dist and arr[i]<arr[i-dist]:
                arr[i],arr[i-dist]=arr[i-dist],arr[i]
                i=i-dist
        dist/=2


if __name__=='__main__':
    arr=getrandata(10)
    arr=[9,8,7,6,5,4,9,2,1,0]
    print(arr)
    start_time=time.time()
    shellSort(arr)
    print(time.time()-start_time)
    print(arr)
