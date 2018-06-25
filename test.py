# coding:utf-8
from uiautomator import device as d
import time
from datetime import datetime
import sys
from math import sqrt
from collections import Counter


# while True:
#     if d(resourceId='com.tcl.eshow:id/iv_qr_code_content').wait.exists():
#         print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+u' 二维码存在')
#     else:
#         break
#     time.sleep(1800)

# a = str(-32)
# for i in a:
#     print(i)
  
# print(-2**32)
# print(2**32)

# print(321 >= 2**32)
# print('-1234556'[::-1])
# print(-sys.maxint)
# print(2**31)
# print(cmp(-2, 0))

# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# m = 200
# list1 = []
# for i in range(2, m + 1):
# 	flag = 1
# 	for j in range(2, int(sqrt(m + 1)) + 1):
# 		if i % j == 0 and i != j:
# 			flag = 0
# 			break
# 	if flag == 1:
# 		list1.append(i)
# print(list1)

# arr = [2,3,1,5,1,2,1,3]
# for i in range(len(arr)):
# 	for j in range(i,len(arr)):
# 		if arr[i] > arr[j]:
# 			arr[i],arr[j] = arr[j],arr[i]
# print(arr)

# result = []
# for i in list(set(arr)):
# 	count = 0
# 	for j in arr:
# 		if j == i:
# 			count = count + 1
# 	result.append((i,count))
# print(result)

# a = 110
# print(100 < a < 150)

