def check(L, pair, maxVolume):
	dAB = {}
	for i in range(len(L)):
		a, b, c = L[i]
		if a > b:
			a, b = b, a
		l = dAB.get((a, b), [])	
		l = l + [(c, int(i/3) + 1)]
		l.sort()

		dAB[(a, b)] =  l[-2:]
	for a, b in dAB:
		if len(dAB[(a, b)]) < 2:
			continue
		l = dAB[(a, b)]
		cFirstMax, p1 = l[0]
		cSecondMax, p2 = l[1]

		if min(a/2, b/2, (cFirstMax + cSecondMax)/2) > maxVolume:
			maxVolume = min(a/2, b/2, (cFirstMax + cSecondMax)/2)
			pair = [p1, p2]	
	# print(dAB)
	return (pair, maxVolume)
N = int(input())																																																																																																					
L = []
for n in range(N):
	L.append(list(map(int, input().split())))
maxVolume = 0
pair = []
for i in range(N):
	a, b, c = L[i]
	if min(a/2, b/2, c/2) > maxVolume:
		maxVolume = min(a/2, b/2, c/2)
		pair = [i + 1]
#a, c, b
x = []
for i in range(N):
	 x.append((min(L[i][2], L[i][1]), max(L[i][2], L[i][1]), L[i][0]))
	 x.append((min(L[i][0], L[i][2]), max(L[i][0], L[i][2]), L[i][1]))
	 x.append((min(L[i][0], L[i][1]), max(L[i][0], L[i][1]), L[i][2]))
pair, maxVolume = check(x, pair, maxVolume)
print(len(pair))
pair.sort()
for p in pair:
	# print(p)
	print(p, end=' ')
print()