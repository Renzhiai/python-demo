#coding:utf-8
import os

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
l = [x * x for x in range(1, 11)]

# [4, 16, 36, 64, 100]
l = [x * x for x in range(1,11) if x % 2 == 0]

# ['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']
l = [m + n for m in "abc" for n in "xyz"]

# 列出所有目录和文件
l = [d for d in os.listdir("c:/")]

# ['hello', 'world', 'ibm', 'zone']
L = ["Hello", "World", "IBM", "Zone"]
l = [s.lower() for s in L]

# 生成器
# 不必创建完整的 list，从而节省大量的空间。这种一边循环一边计算的机制，称为生成器： generator。
# 创建 L 和 g 的区别仅在于最外层的[]和()， L 是一个 list，而 g 是一个generator
g = (x * x for x in range(1, 11))
#print(next(g))
#print(next(g))
#print(next(g))
for n in g:
	print(n)


# yield类似于return，如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个generator
def odd():
	print("step1")
	yield(100)
	print("step2")
	yield(2)
	print("step3")
	yield(3)

if __name__=="__main__":
	g = odd()
	print(next(g))
	# next(g)
	# next(g)
	