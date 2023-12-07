from string import ascii_uppercase as up

abc = '0123456789' + up
abc = abc[:16]
n2 = int('79', 16)
for c1 in abc[::-1]:
    for c2 in abc[::-1]:
        n1 = int(f'1{c1}DED{c2}CED', 16)
        if n1 % n2 == 0:
            print(n1, n1//n2)
##8555171053 70703893
##6407666925 52955925
##5065538797 41863957
