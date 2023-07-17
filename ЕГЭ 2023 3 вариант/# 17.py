with open('17_9840.txt') as file:
    total = []
    lst = [int(i) for i in file]
    max_lst = max([i for i in lst if len(str(abs(i))) == 4 and str(i)[-2:] == '39'])**2
    for i in range(len(lst)-1):
        if ((len(str(abs(lst[i]))) == 4) + (len(str(abs(lst[i+1]))) == 4)) == 1:
            if (lst[i] + lst[i+1])**2 <= max_lst:
                total.append(lst[i] + lst[i+1])
print(len(total), max(total), sep='\n')
