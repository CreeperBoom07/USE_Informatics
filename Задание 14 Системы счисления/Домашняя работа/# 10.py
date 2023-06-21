n = 5 * 216**1156 - 4 * 36**1147 + 6**1153 - 875
s = ''
while n:
    s = str(n % 6) + s
    n //= 6
print(abs(s.count('5') - s.count('0')))

# 1182

