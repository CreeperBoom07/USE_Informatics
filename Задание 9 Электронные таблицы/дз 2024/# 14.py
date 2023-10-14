with open('09_9778.csv') as file:
    data = [[int(n) for n in line.split(';')] for line in file]
k = 1
for line in data:
    p = [n for n in line if line.count(n) == 2]
    np = [n for n in line if line.count(n) == 1]
    if len(p) == 2 and len(np) == 4:
        if p[0] >= sum(np)/len(np):
            print(k)
            break
    k += 1
# 34
