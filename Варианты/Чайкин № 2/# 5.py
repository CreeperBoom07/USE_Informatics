def f(n):
    s = 0
    while n:
        s += n%10
        n //= 10
    return s % 2 == 0 
def f1(r):
    lst = [int(n) for n in list(r)]
    return str(max(lst))

for n in range(1, 1000):
    R = oct(n)[2:]
    if f(n):
        R = R + str(n%3)
    else:
        R = f1(R) + R
    if int(R, 8) > 127:
        print(n)
        break
# 10
        
    
