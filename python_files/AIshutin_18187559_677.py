n, h = map(int, input().split())
arr=list(map(int, input().split()))
cnt=n
for el in arr:
    if el>h:
        cnt+=1
print(cnt)