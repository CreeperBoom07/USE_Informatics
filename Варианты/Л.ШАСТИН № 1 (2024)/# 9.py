with open('9 (2).csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]

k = 1
s = 0
for line in data:
    if line == sorted(line) or len(set(line)) != 5:
        s += k
    k += 1
print(s)
# 274725
