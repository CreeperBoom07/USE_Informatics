def f(n):
    k = 0
    k += 1
    if n >= 1:
        k += 2 + f(n-1) + f(n-3)
    return k
print(f(40))
# 22947841
