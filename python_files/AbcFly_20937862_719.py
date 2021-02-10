n = int(input())
al = list(map(int, input().split()))
ans = 0
if n==1:
    if al[0]==0:
        ans=1
    elif al[0]==15:
        ans=2
else:
    if al[n-1]==15 or (al[n-1]<al[n-2] and al[n-1]>0):
        ans=2
    else:
        ans=1


print([-1,"UP","DOWN"][ans])