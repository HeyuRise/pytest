# 字典 一系列无序元素的组合，其长度大小可变，元素可以任意地删减和改变
# 字典是一对键（key）和值（value）的配对
tel = {'jack': 14568, 'xxx': 5974}
print(tel)

print(tel['jack'])

del tel['xxx']
print(tel)

tel['aaaa'] = 456213
print(tel)

print(list(tel))
print(sorted(tel))
print(tel)

print('aaaa' in tel)
print('aaaa' not in tel)

a = [tel[x] for x in sorted(tel)]
print(a)
