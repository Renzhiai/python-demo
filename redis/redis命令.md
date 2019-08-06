|命令| 描述|
|-|-|
./redis-server|
./redis-cli|
config get *					|	获取所有配置
set score 'a'			|			设置成绩为a，string类型最大存储为512M
get score					|		获取score的值
del score				|			删除
hmset myhash name 'mm' age '19'	|	设置hash键值对，每个hash可以存储232-1键值对(40多亿)
hget myhash age				|		获取hash键值
del myhash name			|			删除name
lpush mylist a b c d 		|		给list放置4个元素，列表最多可存储232-1元素(40多亿)
rpush mylist a b c d|
lrange mylist 0 3				|	取4个值|
sadd myset a a b			|		给set加两个值，集合中最大的成员数为 232 - 1(40多亿)
smembers myset			|			取值
zadd myzset 0 b				|		给zset有序集合加值，这是根据score取值的，score越小，排名越靠前
zadd myzset 0 c				|		
zadd myzset 1 a				|		
zrange myzset 0 100		|			取值
|
select 1 							|切换到数据库1，Redis默认支持16个数据库，不支持命令，不支持单独设置密码
|select 0							|切换到数据库0
|flushall					|		清空redis里面所有数据库的数据，一个空Redis实例占用的内在只有1M左右
|flushdb					|			删除当前数据库的key
|info							|	获取 Redis 服务器的各种信息和统计数值|
|save						|		该命令将在 redis 安装目录中创建dump.rdb文件
|config get dir			|			恢复数据：备份文件(dump.rdb)移动到 redis 安装目录并启动服务
|config set requirepass pwd	|		设置redis密码
|auth pwd						|	输入密码
|config get maxclients		|		获取最大连接数
|ping|
|redis-cli -h host -p port -a password |远程连接redis|
|
string字符串|
exists key	|						判断key是否存在
expire key 30			|			设定key 30秒过期
keys s*e					|		查找符合的key
presist key				|			key永久保存
ttl key						|		以秒为单位，返回给定 key 的剩余生存时间
randomkey				|			随机返回一个key
rename key newkey	|				修改key的名称
type key						|	返回 key 所储存的值的类型|
GETRANGE key 1 2	|				截取key的第1和第2位
SETNX key value		|				key 不存在时设置 key 的值
SETRANGE key 1 555	|				设置key的值得，从第1位开始，后面设置为555
STRLEN key					|		返回key的长度
INCR key						|	将 key 中储存的数字值增一
INCRBY key increment	|			将 key 所储存的值加上给定的增量值
DECR key						|	将 key 中储存的数字值减一
DECRBY key decrement	|			将 key 所储存的值减去给定的减量值
APPEND key value			|		追加
|
哈希表|
HEXISTS hash field			|		哈希表指定的字段是否存在
|HKEYS hash						|	获取所有哈希表中的字段
|HVALS hash						|	获取哈希表中所有值
|HGETALL hash 					|	获取在哈希表中指定 key 的所有字段和值
|HLEN hash						|	获取哈希表中字段的数量
|
列表|
BLPOP list timeout		|			移出并获取第一个元素， 如果没有就等待超时或发现可弹出元素为止
BRPOP list timeout		|			移出并获取列表的最后一个元素
LINDEX list index			|		通过索引获取列表中的元素
LLEN list							|获取列表长度
LINSERT list BEFORE\|AFTER value1 value2 |	在value1之前或之后插入value2
LPOP list				|			移除并获取列表的第一个元素
RPOP list				|			移除最后一个元素
LRANGE list start stop	|			获取列表指定范围内的元素
LSET list index value		|		通过索引设置列表元素的值
LTRIM list start stop		|		截取元素，区间内的保留
|
set集合|
SCARD set					|		获取集合的成员个数
SMEMBERS key		|				返回集合中的所有成员
SDIFF set1 [set2] 		|			获取所有集合的差集
SDIFFSTORE set set1 [set2]	|返回给定所有集合的差集并存储在 set 中
SINTER set1 [set2] 				|	返回给定所有集合的交集
SINTERSTORE set key1 [key2] |返回给定所有集合的交集并存储在 set 中
SISMEMBER set member 		|		判断 member 元素是否是集合的成员
SMOVE set1 set2 member		|		将 member 元素从set1集合移动到set2集合
SPOP set						|	移除并返回集合中的一个随机元素
SRANDMEMBER set [count]|				返回集合中一个或多个随机数
SUNION set1 [set2]				|	返回所有给定集合的并集
SUNIONSTORE set set1 [set2]|			所有给定集合的并集存储在 set 集合中
|
SUBSCRIBE redisChat				|	消息订阅
PUBLISH redisChat "Redis"		|	消息发布
|
multi						|		开始事务
exec						|		执行事务内的命令
discard					|			取消事务