n = int(input())
a = set(map(int, input().split()))

if len(a) < 3:
	print("YES") 
elif len(a) > 3:
	print("NO") 
else:
	aa = list(a)
	aa.sort()
	if 2*aa[1] == aa[0] + aa[2]: 
		print("YES") 
	else:
		print("NO")