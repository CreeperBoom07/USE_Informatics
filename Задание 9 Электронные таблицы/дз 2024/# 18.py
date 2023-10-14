with open('./09_10910.csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]

k = 0
for line in data:
    if line.count(min(line)) == 1:
        if len(line) != len(set(line)):
            p = [n for n in line if line.count(n) > 1]
            if max(line) + min(line) < sum(p):
                k += 1
print(k)
# 447
