with open('./09_6602.csv') as file:
    lst = [[int(num) for num in line.split(',')] for line in file]

k = 0
for line in lst:
    s_p = []
    s_np = []
    for num in line:
        if line.count(num) == 1:
            s_np.append(num)
        else:
            s_p.append(num)
    if len(s_p) == 2:
        if sum(s_np)/len(s_np) >= sum(s_p):
            k += 1
print(k)

# 64
