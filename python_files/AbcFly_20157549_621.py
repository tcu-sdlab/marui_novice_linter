n = int(input())
al = list(map(int, input().split()))
ol = []
ans=0
for a in al:
    if a%2>0:
        ol+=[a]
ans = sum(al)
x = len(ol)
if x>0 and x%2==1:
    ans-=min(ol)
print(ans)