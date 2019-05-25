# 元组 一个元组由几个被逗号隔开的值组成
# 而元组是静态的，长度大小固定，无法增加删减或者改变

t = 12345, 54321, 'hello!'
print(t[0])
#
# u = t, (1, 2, 3, 4)
# print(u)
# t[0] = 1
# print(u)
#
# v = ([1, 2, 3], [3, 2, 1])
# print(v)

# empty = ()
# singleton = 'xxxx',
# print(len(empty))
# print(len(singleton))
# print(singleton)

x, y, z = t
print(x, y, z)
