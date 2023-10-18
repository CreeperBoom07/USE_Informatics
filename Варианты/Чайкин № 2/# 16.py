
def f(n, k):
    k += 1 
    if n > 1:
        return f(n-2, k), f(n//2, k)
        k += 1
    k += 1
_, k = f(127, 0)
print(k)
