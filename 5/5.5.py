# 字典
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
