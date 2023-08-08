def f(line):
    d = {}
    for n in line:
        d[n] = d.get(n, 0) + 1

    vals = list(d.values())
    
    return vals.count(2) == 1 and vals.count(1) == 4 \
       and ((sum(i for i in d if d[i] == 1) / 4) <= sum(i for i in d if d[i] == 2))


with open('09_9778.csv') as file:
    lst = []
    for line in file:
        temp = [int(i) for i in line.split(';')]
        lst.append(temp)


for line in range(len(lst)):
    if f(lst[line]):
        print(line+1)
        break

# 34
