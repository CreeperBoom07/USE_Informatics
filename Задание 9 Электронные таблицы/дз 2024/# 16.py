with open('./09_8609.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]

k = 0
for line in data:
    if len(line) == len(set(line)):
        a, b, c, d, e = sorted(line)
        if (a+e)*2 <= (b+c+d)*3:
            k += 1
print(k)
# 2776
