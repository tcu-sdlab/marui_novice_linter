(m,n) = (int(i) for i in input().split())
l = [n]
chls = []
while 1:
	if n<m: break
	if n % 2 == 0:
		n = n/2
		chls.append(int(n))
	else:
		if n % 10 == 1:
			n = (n-1)/10
			chls.append(int(n))
		else:
			break
	if n == m: break

if n == m:
	print('YES')
	print(len(chls)+1)
	for i in range(len(chls)-1, -1, -1):
		print(chls[i], end=' ')
	print(l[0], end='')


else:
	print('NO')