'''Петя составляет пятибуквенные слова из букв ТИМАШЕВСК.
   Он выбирает только те слова, в которых количество гласных
   больше количества согласных и гласная буква не стоит рядом с Ш.
   Сколько таких слов может составить Петя?
   ОТВЕТ: 9288'''
from itertools import product as pd

k = 0

'''РЕШЕНИЕ 1'''
# def prov(word):
#     for i in 'ИАЕ':
#         if i + 'Ш' in word or 'Ш' + i in word:
#             return False
#     return True
#
#
# for x in pd('ТИМАШЕВСК', repeat=5):
#     s = ''.join(x)
#     if prov(s):
#         # Гласные
#         for letter in 'ИЕ':
#             s = s.replace(letter, 'А')
#         # Согласные
#         for letter in 'ТМВСК':
#             s = s.replace(letter, 'Ш')
#
#         if s.count('А') > s.count('Ш'):
#             k += 1
# print(k)

'''РЕШЕНИЕ 2'''

for x in pd('ТИМАШЕВСК', repeat=5):
    s = ''.join(x)
    for c in 'МВСК':
        s = s.replace(c, 'Т')
    for c in 'ИЕ':
        s = s.replace(c, 'А')
    if s.count('А') > s.count('Т') + s.count('Ш') and all(i not in s for i in ('АШ', 'ША')):
        k += 1
print(k)
