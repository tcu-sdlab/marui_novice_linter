n  = int(input())
vl = ['a','e','i','o','u','y']
cl = list(map(int, input().split()))
flag=True
for i in range(n):
    ts = input()
    if flag:
        sum = 0
        for v in vl:
            sum+=ts.count(v)
        if sum!=cl[i]:
            flag=False
print(["NO","YES"][flag])