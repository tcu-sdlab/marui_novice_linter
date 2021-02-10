chars = input()
code = input()
i = 0
count = 0
a = []
while i < int(chars):
	if code[i] == 'B':
		count += 1
	if code[i] == 'W':
		if count > 0:
			a.append(count)
		count = 0
	i += 1
s = ''
if count > 0:
	a.append(count)
for x in a:
	s += str(x)+' '
print(len(a))
print(s)