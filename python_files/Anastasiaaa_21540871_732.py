a = list(map(int,input().split()))
a.sort()
a[1] -= a[0]
a[2] -= a[0]
a[0] -= a[0]
if a[2] == 0: print(0)
elif a[1] == a[2]: print(a[2] - 1)
elif a[1] and a[2]:
	a[2] -= 1
	x = a[2]
	y = a[2] - a[1]
	print(x+y)
else: print((a[2] - 1)*2)