from fnmatch import *

for x in range(0, 10**9, 169):
    if fnmatch(str(x), '123*567?'):
        print(x, x//169)
##12325677 72933
##12385672 73288
##123165679 728791
##123225674 729146
##123515678 730862
##123575673 731217
##123865677 732933
##123925672 733288
