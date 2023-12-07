def f(n):
    return g(n-1)

def g(n):
    if n < 10:
        return n
    return g(n-2)+1

k = 0
for n in range(1, 101):
    x = f(n) 
    if x > 0 and int(x**0.5)**2 == x:
        k += 1
print(k)
# 12
