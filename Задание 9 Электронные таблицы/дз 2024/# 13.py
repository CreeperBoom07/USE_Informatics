with open('9_9740.csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]

k = 0
for line in data:
    p = [n for n in line if line.count(n) == 3]
    np = [n for n in line if line.count(n) == 1]
    if len(p) == 3 and len(np) == 4:
        if sum(np)/len(np) <= p[0]:
            k += 1
print(k)
        
# 36
