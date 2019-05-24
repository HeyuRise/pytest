knights = {'ssssss': 'sdagsdf', 'gasdfasf': 'hhhhhhh'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['wwww', 'dsafasd', 'fasdfav']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
x = list(zip(questions, answers))
print(x)
for i, j in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(i, j))
