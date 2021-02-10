n,d = map(int, input().split())
al = list(map(int, input().split()))
m = int(input())
ans = 0
if m>n:
    ans=sum(al)-(m-n)*d
else:
    al.sort()
    ans=sum(al[:m])
print(ans)