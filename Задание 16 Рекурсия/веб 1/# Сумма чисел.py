def f(n):
    k = 0
    k += n + 1
    if n > 1:
        k += n + 5
        k += f(n-1)
        k += f(n-2)
    return k
print(f(30))
# 19997545
