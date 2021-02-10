n = int(input())

odd = list(filter(lambda m: m % 2 == 1, range(1,(n**2+1))))
even = list(filter(lambda m: m % 2 == 0, range(1,(n**2+1))))

magic_square = []

for i in range(n):
	if i == 0:
		s = "01" * (n//2)
		if n%4==1:
			s = "1" + s
		else:
			s = s + "0"
		magic_square.append(s)
	else:
		last = int(magic_square[i-1], 2)
		fil_a = "1" * i + "0" * (n-i)
		fil_b = "0" * (n-i) + "1" * i
		s = format(last^int(fil_a,2)^int(fil_b,2), 'b').zfill(n)
		magic_square.append(s)

# print(magic_square)

ans = []

for row in magic_square:
	l = []
	for col in row:
		if col == "1":
			l.append(odd.pop())
		else:
			l.append(even.pop())
	ans.append(l)

for i in ans:
	print(" ".join(map(str,i)))