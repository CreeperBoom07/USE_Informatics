with open('./09_6357.csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]

k = 0
for line in data:
    p = [n for n in line if line.count(n) > 1]
    np = [n for n in line if line.count(n) == 1]
    if len(p) > 0 and len(np) > 0:
        sr_p = sum(p)/len(p)
        sr_np = sum(np) / len(np)
        if sr_np < sr_p:
            k += 1
print(k)
# 1770
