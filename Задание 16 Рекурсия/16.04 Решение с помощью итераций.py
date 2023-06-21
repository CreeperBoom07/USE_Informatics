f = [0] * 10**6
for n in range(len(f)):
    if n <= 3:
        f[n] = n
    else:
        if n % 2 == 0:
            f[n] = n+f[n-1]
        else:
            f[n] = n*n + f[n-2]
print(len([i for i in f if 1 <= i < 10**8]))
