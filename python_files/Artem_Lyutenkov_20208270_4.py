n = int(input())
a = dict()
for i in range(n):
	s = input()
	if s in a.keys():
		print(s + str(a[s]))
		a[s] += 1
	else:
		print('OK')
		a[s] = 1