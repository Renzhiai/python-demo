# coding:utf-8
import datetime
import time

# 打印当前时间时间戳
print(time.time())
# 打印当前日期时分秒毫秒
print(datetime.datetime.now())
# 打印当前日期时分秒
print(time.strftime("%Y-%m-%d %H:%M:%S"))

sft = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
print(sft, type(sft))

# 自己设置时间
dt = datetime.datetime(2016, 2, 14, 12, 50)
print(dt)
# 计算毫秒数，小数位表示毫秒数
ts = datetime.datetime(2016, 2, 14, 12, 50).timestamp()
print(ts)
# 毫秒数转换成时间
dt = datetime.datetime.fromtimestamp(ts)
print(dt)
# str转为datetime
day = datetime.datetime.strptime("2016-8-1 12:12:30", "%Y-%m-%d %H:%M:%S")
print(day)

# # 时间加上
begin_time = '2023-05-09'
days = 10
end_time = datetime.datetime.strptime(begin_time, "%Y-%m-%d") + datetime.timedelta(days=days)
print(end_time)