def f(line):
    s = ''
    for n in range(len(line)-1):
        if line[n] > line[n+1]:
            s += '0'
        elif line[n] < line[n+1]:
            s +='1'
    return s[0] == '0' and s[-1] == '1' and '10' not in s and s.count('01') == 1



#print(f([460,673,173,556,385]))


with open('./9_5724.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]


k = 0
for line in data:
    if f(line):
        k += 1
print(k)

# 116

