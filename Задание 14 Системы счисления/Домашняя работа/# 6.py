for x in range(1, 10000):
    n = 4**2015 + 2**x - 2 ** 2015 + 15
    if bin(n)[2:].count('1') == 500:
        print(x)
        break

# 2510
