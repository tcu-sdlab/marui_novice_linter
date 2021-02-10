x1,y1,x2,y2=map(int,input().split())
a=(y2-y1+2)//2
b=(x2-x1+1)
c=(a*b)-((x2-x1)//2)
print(int(c))