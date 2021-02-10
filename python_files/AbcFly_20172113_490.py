n = int(input())
tl = list(map(int, input().split()))
al = [[],[],[],[]]
for i in range(n):
    al[tl[i]]+=[i+1] 
ans = min([len(al[1]),len(al[2]),len(al[3])])
print(ans)
for i in range(ans):
    print("%d %d %d" % (al[1][i],al[2][i],al[3][i]))