b=int(input())+1
a=str(b)
n=len(a)
while 1:
    k=1
    for i in range(n-1):
        if a[i] in a[i+1:]:
            k=0
            break
    if k:
        print(a)
        exit()
    else:
        b+=1
        a=str(b)