def f(line):
    c = 0
    for num in line:
        if num % 2 != 0:
            c += 1
        else:
            c = 0
        if c == 3:
            return True
    return False


with open('./9_5451.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]


    
k = 0
for line in data:
    if f(line):
        k += 1
print(k)

# 248
