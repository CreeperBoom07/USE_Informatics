with open('9_5126.csv') as file:
    date = [[int(n) for n in line.split(',')] for line in file]
k = 0
for line in date:
    p = [n for n in line if line.count(n) == 3]
    np = [n for n in line if line.count(n)==1]
    if len(p) == len(np) == 3:
        if sum(np)/len(np) <= sum(p):
            k +=1
print(k)
# 125
