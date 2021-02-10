n=int(input())
res = "NO"
for i in range(n):
    before,after = map(int, input().split()[1:])
    if before>=2400 and after>before:
        res = "YES"
print(res)