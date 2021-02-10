n,m=map(int,input().split())
lst = list(map(int, input().split()))
res = 1;
for i in reversed(range(len(lst))):
    if i > 0 and lst[i] - lst[i-1] <= m:
        res = res + 1;
    else:
        break

print(res)