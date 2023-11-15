with open('9_11452.csv') as file:
    data = [[int(x) for x in line.split(',')] for line in file]

k = 1
for line in data:
    dv = [n for n in line if line.count(n) == 2]
    unic = [n for n in line if line.count(n) == 1]
    if len(dv) == 2 and len(unic) == 4:
        if dv[0] >= sum(unic)/len(unic):
            print(k)
            break
    k += 1
# 34
