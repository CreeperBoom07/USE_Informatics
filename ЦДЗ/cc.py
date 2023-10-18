n = 74
s = ''
while n:
    s = str(n%4) + s
    n //= 4
print(s)
