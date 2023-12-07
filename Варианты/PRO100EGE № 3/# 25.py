
for x in '02468':
    for y in '13579':
        for z in '13579':
            for i in '13579':
                n = int(f'1{x}2157{y}{z}{i}4')
                if n % 133 == 0:
                    print(n, n//133)
        
