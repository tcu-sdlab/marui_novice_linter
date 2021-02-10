input()
ms = input().split("W")
ans = []
for ss in ms:
    if ss!='':
        ans+=[str(len(ss))]
print(len(ans))
if len(ans)>0:
    print(" ".join(ans))