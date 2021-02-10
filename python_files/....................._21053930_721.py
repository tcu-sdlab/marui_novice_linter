n, k = input().split()
a = []
for i in range(int(n)):
	a.append(input())
ans = input()
ceq = 0
cle = 0
s = ''
mx = len(ans)
for ax in a:
	if len(ax) < mx:
		cle += 1
	elif len(ax) == mx:
		ceq += 1
err = (cle) / int(k)
tmn = int(err) * 5 + cle + 1
err = (cle+ceq-1) / int(k)
tmx = int(err) * 5 + cle + ceq
print(str(int(tmn))+' '+str(int(tmx)))