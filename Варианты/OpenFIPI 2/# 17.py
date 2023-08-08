with open(file='17_7267.txt', mode='r', encoding='utf-8') as file:
    lst = [int(n) for n in file]
    m = min(lst)
    total = []
    for i in range(len(lst)-1):
        if lst[i] % 117 == m or lst[i+1] % 117 == m:
            total.append(lst[i]+lst[i+1])
print(len(total), max(total), sep='\n')
