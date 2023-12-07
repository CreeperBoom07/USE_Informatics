from fnmatch import *

for x in range(0, 10**10, 133):
    s = str(x)
    if fnmatch(s, '1?2157*4') and int(s[1]) % 2 == 0:
        if len(s) != 7:
            if all(int(i) % 2 != 0 for i in s[6:-1]):
                print(x, x//133)
        else:
            print(x, x//133)
##122157574 918478
##1021575394 7681018
##1421575554 10688538
##1821575714 13696058
