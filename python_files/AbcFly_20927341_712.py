cnt = []
ms = input()
cnt+=[ms.count('U')]
cnt+=[ms.count('D')]
cnt+=[ms.count('R')]
cnt+=[ms.count('L')]
ans = abs(cnt[0]-cnt[1])+abs(cnt[2]-cnt[3])
if ans%2==1:
    print(-1)
else:
    print(ans//2)