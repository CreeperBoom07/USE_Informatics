from itertools import permutations as pm 



with open('./9_6081.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]


k = 0
for line in data:
    if len(set(line)) == 5 and any(sum(s[:3]) == sum(s[3:]) for s in pm(line)):
        k += 1
print(k)


# 127
