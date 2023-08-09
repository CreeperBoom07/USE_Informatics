with open('./9_5489.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]

k = 0
for line in data:
    if len(set(line)) == 5:
        ch = []
        nch = []
        for n in line:
            if n % 2 == 0:
                ch.append(n)
            else:
                nch.append(n)
        if len(ch) > len(nch) and sum(ch) < sum(nch):
            k += 1
print(k)

# 241
