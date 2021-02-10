n = int(input())
t = 0
for i in range(n):
    a,b = list(map(int,input().split()))
    if a==b: t = t + 1
if t == n : print("Poor Alex")
else:
    print("Happy Alex")