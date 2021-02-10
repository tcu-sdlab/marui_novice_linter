from operator import *
s = [i for i, x in enumerate("A" + input() + "A") if x in "AEIOUY"]
print(max(map(sub, s[1:], s)))