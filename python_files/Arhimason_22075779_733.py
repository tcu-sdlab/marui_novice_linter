st = input()
string = st + 'A'
c = 1
tc = 1
glasn = ['A', 'E', 'I', 'O', 'U', 'Y']
for i in string:
	if i not in glasn:
		tc+=1
	else:
		if c<tc:
			c = tc
		tc = 1
print(c)