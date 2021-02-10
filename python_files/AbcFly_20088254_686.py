n,x = map(int, input().split())
l = 0
for i in range(n):
    o,s = input().split()
    s = int(s)
    if o=="+":
        x+=s
    elif x>=s:
        x-=s
    else:
        l+=1
print("%d %d" % (x, l))