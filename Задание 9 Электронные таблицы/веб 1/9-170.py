with open(file='9-170.csv', mode='r', encoding='utf-8') as file:
    k = 0
    for line in file:
        temp = [int(i) for i in line.split(',')]
        temp2 = [i for i in temp if temp.count(i) == 2]
        temp1 = [i for i in temp if temp.count(i) == 1]
        if len(temp1) == 4 and len(temp2)==2 and sum(temp1)/4 <= sum(temp2):
            #print(temp1, temp2)
            k += 1
print(k)
            
    


