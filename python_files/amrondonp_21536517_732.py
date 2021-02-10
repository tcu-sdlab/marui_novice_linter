numbers = [int(n) for n in input().split()]
b = numbers[0]
d = numbers[1]
s = numbers[2]

ans = max(numbers)*3 - sum(numbers)

for i in range(3):
	op1 = max(numbers)*3 - sum(numbers)

	op2 = op1
	if b > d and b > s:
		op2 = b*3 - sum(numbers) - 2
	elif d>=b and d>s:
		op2 = d*3 - sum(numbers) + 1
	else:
		op2 = s*3 - sum(numbers) + 1

	op3 = op1
	if b > d and b > s:
		op3 = b*3 - sum(numbers) - 1
	elif d>=b and d>s:
		op3 = d*3 - sum(numbers) - 1
	else:
		op3 = s*3 - sum(numbers) + 2

	ans = min(ans,min(op3,op2))
	aux = b
	b = d
	d = s
	s = aux

print (ans)