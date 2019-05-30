l = []
for n in range(0, 10):
    l.append(str(n))
l = ' '.join(l)
print(l)


def query_data(namespace, table):
    return namespace + ' ' + table


path = 'hive://ads/training_table'
namespace = path.split('//')[1].split('/')[0]  # 返回'ads'
table = path.split('//')[1].split('/')[1]  # 返回 'training_table'
data = query_data(namespace, table)
print(data)

s = ' my name is jason '
print(s.lstrip())
print(s.rstrip())
print(s.strip())

code = 1
name = 'xxx'
print('no data available for person with id: {}, name: {}'.format(code, name))

print(list(range(0, 10000)))

