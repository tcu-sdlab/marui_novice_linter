id={}
ans=""
src = input()
for i in range(10):
    id[input()]=i
for j in range(8):
    ans+=str(id[src[j*10:j*10+10]])
print(ans)