def f1(line):
    if len(line) == len(set(line)):
        return round((max(line)+min(line)) / 2) in line
    return False


def f2(line):
    if len(set(line)) < len(line):
        s_p = 0
        s_n = 0
        for i in line:
            if line.count(i) > 1:
                s_p += i**2
            else:
                s_n += i**2
        return s_p < s_n
    return False

        
with open('./9_7335.csv') as file:
    lst = []
    for line in file:
        temp = [int(x) for x in line.split(';')]
        lst.append(temp)


k = 0
for line in lst:
    if f1(line) ^ f2(line):
        k += 1
print(k)


# 1151
