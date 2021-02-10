a,b,c=map(int,input().split())
s=1
m=1
while s<=b:
  if s>=a and s<=b:
    print(s)
    m=0
  
  s*=c

if m==1:
  print(-1)