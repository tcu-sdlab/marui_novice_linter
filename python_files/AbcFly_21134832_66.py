n = input()
l = len(n)
dl = ["127", "32767", "2147483647", "9223372036854775807"]
ai = 0
if l<len(dl[0]):
    ai=0
elif l==len(dl[0]) and n<=dl[0]:
    ai=0
elif l<len(dl[1]):
    ai=1
elif l==len(dl[1]) and n<=dl[1]:
    ai=1
elif l<len(dl[2]):
    ai=2
elif l==len(dl[2]) and n<=dl[2]:
    ai=2
elif l<len(dl[3]):
    ai=3
elif l==len(dl[3]) and n<=dl[3]:
    ai=3
else:
    ai=4
print(["byte", "short", "int", "long", "BigInteger"][ai])