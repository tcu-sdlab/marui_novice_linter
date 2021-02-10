n = int(input())
data = list(map(int,input().split()))    
s1 = s2 = 0
l=0
r=n-1
for i in range(n):
    if data[l]>=data[r]:
        t=data[l]
        l+=1
    else:
        t=data[r]
        r-=1
    if i%2==0:
        s1+=t
    else:
        s2+=t
print(s1,s2)