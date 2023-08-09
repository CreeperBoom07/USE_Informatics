with open('./9_5664.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]

k = 0
for line in data:
    if any(x%10 == 4 for x in (line[0]*line[1], line[0]*line[2], line[1]*line[2])):
        k += 1
print(k)

# 965
