n,m = map(int,input().split())
a = list(map(int,input().split()))
k = 0
for i in range(n-1):
	x = a[i]+a[i+1]
	if x < m: 
		k += m - x
		a[i+1] += m - x
print(k)
print(*a)