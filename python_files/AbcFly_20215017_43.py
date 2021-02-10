sl = []
for i in range(int(input())):
    sl+=[input()]
ans = []
for s in set(sl):
    ans+=[[sl.count(s), s]]
ans.sort(reverse=True)
print(ans[0][1])