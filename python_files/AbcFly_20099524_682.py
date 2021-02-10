input()
al = list(map(int, input().split()))
al.sort()
cur = 1
for a in al:
    if cur<=a:
        cur+=1
print(cur)