#coding:utf-8
from collections import Counter

num=[1,2,3,4,5,6,7,8,9,1,2,3,4,56,7,4,3,6,3,2,5,7,5,3,1,8,9,4,7,89,4,5,4,5,7,8,4,2,1,3]
words=["a","b","c","b","a","d","e","a","b","a","b","a","d","d","d"]
#统计所有数字出现次数
num_counts=Counter(num)
#统计所有字母出现次数
words_counts=Counter(words)
#统计前三名
top_three=num_counts.most_common(3)
#统计前两名
top_two=words_counts.most_common(2)
print(top_three)
print(top_two)

