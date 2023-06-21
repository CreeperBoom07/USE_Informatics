from itertools import product as pd

k = 0
p = 0
last_temp = 0
# for x in pd('ЧН7', repeat=10):
#     if x.count('7') == 5:
#         s = ''.join(x)
#         if 'Н7' not in s and '7Н' not in s and '77' not in s:
#             if x[0] == 'Ч':
#                 k += 3*8**4
#             else:
#                 k += 4*8**4
for x in pd('01234567', repeat=10):
    p += 1
    temp = round(p*100/1073741824, 2)
    if temp != last_temp:
        print(temp)
        last_temp = temp
    if x[0] != '0' and x.count('7') == 5:
        s = ''.join(x)
        s = s.replace('1', 'Н').replace('3', 'Н').replace('5', 'Н')
        if '7Н' not in s and 'Н7' not in s and '77' not in s:
            k += 1
print(k)

# 5888
