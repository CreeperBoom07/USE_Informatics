def f(line):
    m = 1
    for n in ''.join(map(str, line)):
        m*= int(n)
    return m



with open('9_7350.csv') as file:
    lst = []
    for line in file:
        temp = [int(x) for x in line.strip().split(',')]
        lst.append(temp)

k = 0
for line in lst:
    if f(line) > sum(line):
        k += 1
print(k)

# 3649
