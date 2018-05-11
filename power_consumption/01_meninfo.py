# coding:utf-8
import subprocess
import time
import datetime

# 每隔一段时间获取指定app的meninfo
'''
adb shell dumpsys meminfo | find "com.oecommunity.oeshop"
'''

# 设置结果保存路径
csv_path = 'd:/autoTest/meminfo.csv'
# 需要测试的包
# packageName='com.oecommunity.oeshop'
packageName = 'com.tcl.eshow'
# 测试次数
times = 100000000
# 测试时间间隔，单位秒
interval = 1
# 执行的命令
cmd = 'adb shell dumpsys meminfo |find "' + packageName + '"'
for i in range(times):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	# 以换行分割成list
	result = proc.communicate()[0].split('\n')
	# print(result)
	# 统计所有进程内存大小，格式[进程1的内存,进程2的内存,进程3的内存,......]
	sizes = []
	# 统计单个进程占用内存大小
	size = ''
	# 统计某个应用实际内存大小（一个应用包含多一个或者一个以上进程的总和）
	memsize = 0
	# 去掉重复的内容
	result_copy = []
	# 去掉重复的内容
	for mem in result:
		# 去掉空格
		mem = mem.replace(' ', '')
		# 如果men不在result_copy里面，且men不等于''
		if not mem in result_copy and not mem == '':
			result_copy.append(mem)
	# print(result_copy)
	for mem in result_copy:
		# 一个一个读取字符
		for char in mem:
			# 如果是数字就拼接起来
			if char.isdigit():
				size = size + char
			else:
				# 不是数字，拼接完毕，把size加入到sizes，初始化size
				sizes.append(size)
				size = ''
				break
	if sizes == []:
		print(u'没有获取到内存信息')
	else:
		# 每个size相加
		for size in sizes:
			memsize = memsize + int(size)
	# 获取当前时间
	ltime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# ltime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	with open(csv_path, 'a') as csvf:
		# csv文件加逗号，可以换列输出
		csvf.write(ltime + ',' + str(memsize))
		csvf.write('\n')
	print(ltime)
	print(ltime + u' 第' + str(i + 1) + u'次:' + str(memsize))
	# 间隔10秒
	time.sleep(interval)
