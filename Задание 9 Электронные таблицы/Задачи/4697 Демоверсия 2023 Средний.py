def f(line):
    s_p = []
    s_np = []
    for n in line:
        if line.count(n) == 1:
            s_np.append(n)
        else:
            s_p.append(n)
    return sum(s_np)/len(s_np) <= sum(s_p)
    


with open('./9_4697.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]


k = 0
for line in data:
    if len(set(line)) == 5 and f(line):
        k += 1
print(k)

# 2241

