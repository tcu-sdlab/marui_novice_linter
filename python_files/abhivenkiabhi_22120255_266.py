a,b=map(int,input().split())
c=input()
i=0
while b>0:
    c=c.replace('BG','GB')
    b=b-1
print(c)