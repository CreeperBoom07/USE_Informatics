n = 51*7**12 - 7**3 - 22
s = 0
while n:
    s += n % 7
    n //=7
print(s)
# 70
