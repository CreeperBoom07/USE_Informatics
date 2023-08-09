def f(line):
    sort_line = sorted(line)
    d = sort_line[1] - sort_line[0]
    for n in range(5):
        if (sort_line[n+1] - sort_line[n]) != d:
            return False
    return True

with open('./9_5627.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]

k = 0
for line in data:
    if (len(set(line)) < 6) or f(line):
        k += 1
print(k)

# 525

