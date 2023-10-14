with open('./9_6999.csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]

k = 0
for line in data:
    tr = [n for n in line if n % 3 == 0]
    if max(line) - min(line) <= sum(tr) and len(tr) == 3:
        k += 1
print(k)
# 1835s
