with open(file='17_9786.txt', mode='r', encoding='utf-8') as file:
    lst = [int(i) for i in file]
    max_25 = max([i for i in lst if str(i)[-2:] == '25'])
    total_lst = []
    for i in range(len(lst) - 2):
        k = 0
        if 999 < abs(lst[i]) < 10000:
            k += 1
        if 999 < abs(lst[i+1]) < 10000:
            k += 1
        if 999 < abs(lst[i+2]) < 10000:
            k += 1
        if k <= 2 and ((lst[i] + lst[i+1] + lst[i+2]) <= max_25):
            total_lst.append(lst[i] + lst[i+1] + lst[i+2])
print(len(total_lst), max(total_lst), sep='\n')
