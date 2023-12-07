with open('9_ok_11879.csv') as file:
    data = [[int(x) for x in line.split(',')] for line in file]
k = 0
for line in data:
    c = 0
    tr = [n for n in line if line.count(n)==3]
    unic = [n for n in line if line.count(n)==1]
    if len(tr) == 3 and len(unic) == 4:
        c += 1
    if line == sorted(line):
        c += 1
    if c <= 1:
        k += 1
print(k)
# 14018
