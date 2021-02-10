x=int(input())
a='+'
b='-'
d=int(0)
while x>0:
    y=str(input())
    if a in y:
        d+=1
    elif b in y:
        d-=1
    x-=1
print(d)