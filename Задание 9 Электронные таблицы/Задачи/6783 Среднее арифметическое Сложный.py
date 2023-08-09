# Повторяющиеся числа и среднее арифметическое

with open(file='./9_6783.csv', mode='r', encoding='utf-8') as file:
    lst = [[int(val) for val in line.split(',')] for line in file]

k = 0
for line in lst:
    s_np = []
    s_p = []
    for num in line:
        if line.count(num) == 1:
            s_np.append(num)
        else:
            s_p.append(num)
    if len(set(s_p)) == 1 and len(s_p) == 3:
        if sum(s_np)/len(s_np) < sum(s_p):
            k += 1
print(k)
