kata = input()
max = 0
j = 0
for i in kata:
	if i in 'AEIOUY':
		j = 0;
	else:
		j += 1;
		if (j > max) : max = j
print(max+1)