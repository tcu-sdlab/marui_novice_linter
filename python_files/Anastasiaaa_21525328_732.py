k,r = map(int,input().split())
for i in range(1,10):
	x = (i * k) % 10
	if x == r or x == 0  :
		print(i)
		break