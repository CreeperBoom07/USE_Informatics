for x in range(0, 100):
    n = 4*625**1920 + 4*125**x - 4*25**1940 - 3*5**1950 - 1960
    s = ''
    while n:
        s = str(n%5) + s
        n //= 5
    if s.count('0') == 1891:
        print(x)
        break
# 20
