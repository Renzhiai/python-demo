# coding:utf-8

def groupByElement(lst):
    ''' 元素分组 '''
    result = [[]]
    length = len(lst)
    i = 0
    for i in range(length-1):
        if lst == lst[i + 1]:
            result[-1].append(lst)
        else:
            result[-1].append(lst)
            result.append([])

    result[-1].append(lst)
    return result

if __name__=='__main__':
    l=[1,2,2,3,4,2,5,6]
    print(groupByElement(l))