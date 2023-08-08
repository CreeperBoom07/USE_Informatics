def f(num):
    s = 0
    while num:
        s += num % 2
        num //= 2
    return bin(s)[2:]

lst = {}
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + r + '00'
    else:
        r = r + f(n)
    if int(r, 2) > 190:
        lst[int(r, 2)] = n
        
print(lst[min(lst)])
        
