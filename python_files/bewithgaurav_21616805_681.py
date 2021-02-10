# cook your dish here
n=int(input())
a=1234567
b=123456
c=1234
flag=0
flag2=0
for i in range(10000):
	for j in range(10000):
		x=(a*i) + (b*j)
		
		if x>n:
			flag2=1
			break

		if (n-x)%c==0:
			flag=1
			break
		#print(i,j,x)
	if flag:
		break
if flag:
	print('YES')
else:
	print('NO')