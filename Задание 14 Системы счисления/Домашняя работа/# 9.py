n = 6*144**26 + 11*12**75 - 48
alphabet = '0123456789AB'
k = 0
while n:
    if alphabet[n % 12] == 'B': # или n % 12 == 11
        k += 1
    n //= 12
print(k)

# 51
