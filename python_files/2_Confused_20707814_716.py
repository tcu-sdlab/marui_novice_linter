n=int(input())
k=1
m=2
aux=2
tmp = 4
while n > 0:
	print((m*m - aux)//k)
	k+=1
	aux = m
	m += tmp
	tmp += 2
	n -=1