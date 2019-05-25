# 列表 列表是动态的，长度大小不固定，可以随意地增加、删减或者改变元素

# num = [1, 4, 3, 3]
# append
# num.append(10)
# print(num)


# extend
# b = [678, 876, 4]
# b.extend(num.__iter__())
# print(b)


# index
# print(num.index(3, 0, len(num) - 1))


# count
# print(num.count(3))

# x = ["aaddddddddddddd", "hghb", "cghghgc", "ddg"]
# sort
# x.sort(key=lambda s: len(s), reverse=False)
# print(x)


# deque
# queue = deque(x)
# print(queue.pop())
# print(queue.popleft())
#
# squares = list(map(lambda d: d ** 2, range(20)))
# print(squares)
# squares = [d ** 2 for d in range(20)]
# print(squares)

# a = [(x, y) for x in range(3) for y in [3, 1, 4] if x != y]
# a.append(1)
# print(a)

# vec = [-4, -2, 0, 2, 4]
# vec2 = [x * 2 for x in vec]
# print(vec2)
#
# vec3 = [abs(x * 2) for x in vec]
# print(vec3)

# freshFruit = ['  banana', '  loganberry ', 'passion fruit  ']
# freshFruit[0] = freshFruit[0].strip()
# print(freshFruit)
#
# x = [a.strip() for a in freshFruit]
# print(x)

# d = [(x, x*2) for x in range(10)]
# print(d)

# vec4 = [[1,2,3], [4,5,6], [7,8,9]]
# f = [x for g in vec4 for x in g]
# print(f)

# s = [str(round(pi, i)) for i in range(1, 6)]
# print(s)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print([[row[i] for row in matrix] for i in range(4)])
# print(list(zip(*matrix)))

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)
# del a
# print(a)

