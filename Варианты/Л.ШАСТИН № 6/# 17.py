with open('./17_8611.txt') as file:
    data = [int(num) for num in file]
    max_3 = max([i for i in data if 99 < i < 1000])
    lst = []
    for x in range(len(data)-1):
        if (99 < data[x] < 1000) ^ (99 < data[x+1] < 1000):
            if (data[x]*data[x+1]) % max_3 == 0:
                lst.append(data[x]*data[x+1])
print(len(lst), min(lst), sep='\n')
    
