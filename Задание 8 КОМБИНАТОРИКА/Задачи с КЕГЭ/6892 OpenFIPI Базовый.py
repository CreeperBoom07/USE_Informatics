from itertools import product as pd

'''1 СПОСОБ'''
# def f(n):
#     s = ''
#     while n:
#         s = str(n%6) + s
#         n //= 6
#     if s.count('2') == 1:
#         if s[0] == '2' and int(s[1]) % 2 == 0:
#             return True
#         if s[-1] == '2' and int(s[-2]) % 2 == 0:
#             return True
#         if int(s[s.index('2')-1]) % 2 == 0 and int(s[s.index('2')+1]) % 2 == 0:
#             return True
#     return False
#
#
# k = 0
# for num in range(6**5, 6**6):
#     if f(num):
#         k += 1
#
# print(k)
#
# # 3700
'''2 СПОСОБ'''
k = 0
lst = ['12', '21', '32', '23', '25', '52']
for x in pd('012345', repeat=6):
    s = ''.join(x)
    if s[0] != '0' and s.count('2') == 1 and all(False if i in s else True for i in lst):
        k += 1
print(k)