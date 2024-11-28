# coding=utf-8

l1 = [1, 2, 3]
l2 = [4, 5]
print(list(zip(l1, l2))) # [(1, 4), (2, 5)]


d1 = {'sex': 'man', 'age': 18}
d2 = {'name': 'ming', 'score': 99}

print(dict(zip(d1, d2))) # {'sex': 'name', 'age': 'score'}

print(list(zip(d1, d2))) # [('sex', 'name'), ('age', 'score')]

print(list(zip(d1.items(), d2.items()))) # [(('sex', 'man'), ('name', 'ming')), (('age', 18), ('score', 99))]