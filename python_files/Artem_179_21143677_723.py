n,m = map(int, input().split())
A = dict()
per = list(map(int, input().split()))
cou =[0] * m
for j in range(n):
    if per[j] <= m:
        cou[per[j]-1] +=1
ans = 0
ans2 = n//m
s = 0
for j in range(n):
    num = per[j]
    while s <= m-1:
        if cou[s] < ans2:
            if num > m:
                per[j] = s+1
                cou[s] +=1
                if cou[s] >= ans2:
                    s +=1
                ans +=1
                break
            else:
                if num != s+1 and cou[num-1] > ans2:
                    cou[num-1] -= 1
                    ans +=1
                    cou[s] +=1
                    per[j] = s+1
                    if cou[s] >= ans2:
                        s+=1
                    break
                else:
                    break
                    
            
        else:
            s+=1       
    else:
        break
print(ans2, ans)
print(' '.join(map(str, per)))