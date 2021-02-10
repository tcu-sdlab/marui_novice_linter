a,b=list(map(int,input().split()))
ans = "YES"
for i in range(a):
    str=input()
    for j in range(1,len(str)):
        if str[0]!=str[j]:
            ans="NO"
    if i>0 and first==str:
            ans="NO"
    first=str
print(ans)