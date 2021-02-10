n=int(input())
s = input()
l = len(s)
if l>26:
    print(-1)
else:
    print(l-len(set(s)))