n = int(input())
dl = list(map(int, input().split()))
rdl = dl[::-1]
su, du = 0, 0
ul = [0]
dl_ = [0]
for i in range(1,n):
    if dl[i-1]<=dl[i]:
        su+=1
    else:
        su=0
    if rdl[i-1]<=rdl[i]:
        du+=1
    else:
        du=0
    ul.append(su)
    dl_.append(du)
dl_=dl_[::-1]
for k in range(n):
    ul[k]+=dl_[k]
print(max(ul)+1)