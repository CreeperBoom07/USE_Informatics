def f(right, down):
    if right == down == 11:
        return 1
    if right > 11 or down > 11:
        return 0
    return f(right+1, down) + f(right, down+1)

print(f(1, 1))


# 184756
