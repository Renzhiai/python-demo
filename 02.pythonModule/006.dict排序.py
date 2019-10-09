#coding:utf-8
#这是一个dict
price={
	"yu":15.7,
	"ji":59.1,
	"ya":13.2,
	"zhu":22.8,
	"niu":45.7
}

min_price=min(zip(price.values(),price.keys()))
max_price=max(zip(price.values(),price.keys()))

print("sorted price:")
price_sorted=sorted(zip(price.values(),price.keys()))
for price,name in price_sorted:
	print("    ",name,price)


arr=[4,1,6,4,7,2,9,10,3]
sort_arr=sorted(arr)
for a in sort_arr:
	print (a)
