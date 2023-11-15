def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 5 == 0:
        return n + f(n//5+1)
    return n + f(n+6)

for n in range(100000):
    try:
        if f(n) > 1000:
            print(n)
            break
    except:
        continue
#131
