with open('9 (1).csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]
lst = []
for line in data:
    dv = [n for n in line if line.count(n) == 2]
    unic = [n for n in line if line.count(n) == 1]
    if len(dv) == 4 and len(unic) == 4 and min(line) not in dv:
        lst += [*line]
print(sum(lst)/len(lst))
# 56
