abc = '0123456789AB'
n = 6*144**26 + 11*12**75 - 48
s = ''
while n:
    s = abc[n%12] + s
    n //= 12
print(s.count('B'))
# 51
