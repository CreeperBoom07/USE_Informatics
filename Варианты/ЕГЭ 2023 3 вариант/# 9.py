def f1(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    k = list(d.values())
    if k.count(2) == 2 and k.count(1) == 3 and d[max(d)] == 1:
        print(d)
        return True


with open('9_9832.csv') as file:
    lst = []
    row1 = list(map(int, file.readline()[3:].split(';')))
    lst.append(row1)
    for i in file:
        row = list(map(int, i.split(';')))
        lst.append(row)
    # print(lst)
    for i in range(len(lst)):
        if f1(lst[i]):
            print(sum(lst[i]))
            print(i+1)
            break

# 261
