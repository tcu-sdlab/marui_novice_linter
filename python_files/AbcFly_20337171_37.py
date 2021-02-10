n = int( input())
cl = [0]*1005
ll = list(map(int, input().split()))
for l in ll:
    cl[l]+=1
cl.sort(reverse=True)
print("%d %d" % (cl[0], len(set(ll))))