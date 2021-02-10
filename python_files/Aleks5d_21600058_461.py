n=int(input());l=sorted(map(int,input().split()))
print(sum([l[i]*(i+2) for i in range(n)])-l[-1])