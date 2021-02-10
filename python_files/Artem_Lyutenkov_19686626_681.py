n=int(input())
a = b = c = 0
while a*1234567 <= n:
	cur = a*1234567
	b = 0
	while cur+b*123456<=n:
		if (n-cur-b*123456)%1234==0:print('YES');exit()
		b+=1
	a+=1
print('NO')