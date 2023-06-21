
def f(n):
    k = 0
    while n:
        k += 1
        if k > 4:
            return False
        n //= 5
    return True
counter = 0
for n in range(1, 100000):
    if f(n) and len(bin(n)[2:]) >= 5 and n % 16 == 12:
        counter += 1
print(counter)

# 38
