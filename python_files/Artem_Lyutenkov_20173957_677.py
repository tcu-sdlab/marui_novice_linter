n,h=map(int,input().split())
a=list(map(int,input().split()))
w=n
for i in range(n):
	if a[i]>h:w+=1
print(w)