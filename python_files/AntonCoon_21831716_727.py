a, b = map(int, input().split())
ansver = [b]
while True:
	if b % 2 == 0:
		b = b/2
		ansver.append(b)
	else:
		b -= 1
		b = b/10
		ansver.append(b)
	if b == a:
		print('YES')
		print(len(ansver))
		for i in range(len(ansver)):
			print(int(ansver[len(ansver) - i - 1]), end=' ')
		break
	if b < a:
		print('NO')
		break