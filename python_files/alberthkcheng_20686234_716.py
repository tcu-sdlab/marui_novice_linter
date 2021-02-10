n,c = map(int,input().split(" "))

t = list(map(int,input().split(" ")))

m = 0
ans = 1
if n > 1:
	for i in range(n-1):
		if t[i+1] - t[i] > c:
			m = i+1
	# print(m)
	ans = n-m

print(ans)