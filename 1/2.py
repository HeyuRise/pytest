# name = input('your name:\n')
# gender = input('you are a boy?(y/n)\n')
#
# welcome_str = 'Welcome to the matrix {prefix} {name}'
# welcome_dic = {
#     'prefix': 'Mr.' if gender == 'y' else 'Mrs.',
#     'name': name
# }
# print('authorizing...')
# print(welcome_str.format(**welcome_dic))
import re

# a = input()
# b = input()
# print('a + b = {}'.format(int(a) + int(b)))


def parse(text):
    text = re.sub(r'[^\w]', ' ', text)
    text = text.lower()
    word_list = text.split(' ')
    word_list = filter(None, word_list)
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] = word_cnt[word] + 1
    print(word_cnt)
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[0], reverse=False)
    return sorted_word_cnt


with open('d:/in.txt', 'r') as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('d:/out1.txt', 'a') as fout:
    for word, freq in word_and_freq:
        fout.write('{}: {}\n'.format(word, freq))


