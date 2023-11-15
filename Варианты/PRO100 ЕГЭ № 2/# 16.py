def f(n):
    if n < 10:
        return n
    return n%10 + 8*f(n//10)

print(f(10**30))
