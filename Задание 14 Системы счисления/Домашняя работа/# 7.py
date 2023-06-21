for x in range(1, 10000):
    n = 4**1014 - 2**x + 12
    if bin(n)[2:].count('0') == 2000:
        print(x)
        break

# 2002
