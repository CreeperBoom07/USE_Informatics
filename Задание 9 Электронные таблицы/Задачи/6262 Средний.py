def f(line):
    temp = 0
    for num in line:
        if num % 2 != 0:
            temp += 1
    return temp == 3



with open('9_6262.csv') as file:
    lst = [[int(num) for num in line.split('\t')] for line in file]


k = 0
for line in lst:
    if (len(set(line)) < len(line)) ^ f(line):
        k += 1
print(k)

# 1852


