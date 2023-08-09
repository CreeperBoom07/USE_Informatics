with open('09_6016.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]


k = 0
for line in data:
    if len(set(line)) == 3:
        a, b, c = sorted(line)
        if c**2 < (a**2 + b**2):
            k += 1
print(k)


# 1312      
