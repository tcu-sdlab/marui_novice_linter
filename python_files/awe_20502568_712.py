s = input()
countr = 0
countu = 0
for i in s:
	if i == 'U':
		countu += 1
	elif i == 'D':
		countu -= 1
	elif i == 'R':
		countr += 1
	else:
		countr -= 1
if (countr + countu) % 2 == 1:
	print(-1)
else:
	print((abs(countr) + abs(countu)) // 2)