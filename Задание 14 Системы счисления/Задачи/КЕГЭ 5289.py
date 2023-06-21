def isprime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


k = 0
for x in range(0, 18):
    n1 = 5*18**3 + 6*18**2 + x*18 + 3
    n2 = 4*18**2 + x*18 + 9
    n3 = 5*18**3 + 7*18**2 + x*18 + 1
    total = n1 + n2 - n3
    if isprime(total):
        k += 1
print(k)

# 8
