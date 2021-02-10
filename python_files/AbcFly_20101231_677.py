n,h = map(int, input().split())
al = list(map(int, input().split()))
for i in range(n):
    if al[i]>h:
        al[i]=2
    else:
        al[i]=1
print(sum(al))