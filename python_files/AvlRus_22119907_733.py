n=[0]+[sum(map(int,('-'+input()).split())) for i in range(int(input()))]
s,a,b=sum(n),min(n),max(n)
print(n.index(b if s<a+b else a))