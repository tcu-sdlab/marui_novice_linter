string = input()
wow = string.split(' ')
c = 0
for i in wow:
	if c == 1:
		b = i
		break
	a = i
	c = 1
s = b
b = int(b)
a = int(a)
c = 1
while b > a:
	c += 1
	if (b % 10) == 1:
		b = b // 10		
	elif (b % 2) == 0:
		b = b // 2
	else :	
		break
	s = str(b) + ' ' +s

if b == a:
	print('YES')
	print(c)
	print(s)
else:
	print('NO')