l = [1, 2, 3, 4, 5, 6, 7, 8]
# for item in l:
#     print(item)

# d = {'name': 'heyu', 'dob': '2000-01-01', 'gender': 'male'}
# for k in d:
#     print(k)
# for v in d.values():
#     print(v)
# for k, v in d.items():
#     print('k: {}, v: {}'.format(k, v))
#
# for index in range(0, len(l)):
#     if index < 5:
#         print(l[index])
for index, v in enumerate(l):
    if index >= 5:
        print(v)
