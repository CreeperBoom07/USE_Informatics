for x in range(1, 100):
    n = 36**17 - 6**x + 71
    s = 0
    while n:
        s += n % 6
        n //= 6
    if s == 61:
        print(x)
        break
# 24


    
