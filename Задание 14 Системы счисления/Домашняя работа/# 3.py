n = 2 * 27**7 + 3 ** 10 - 9
k = 0
while n:
    if n % 3 == 0:
        k += 1
    n //= 3
print(k)
# 13
