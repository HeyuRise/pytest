# 集合 一系列无序的、唯一的元素组合

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print('apple' in basket)
print('xxx' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
