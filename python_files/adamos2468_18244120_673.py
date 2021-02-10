def magic(lit):
	for i in range(len(lit)):
		lit[i]=int(lit[i])
	return lit
def min(a, b):
	if(a<b):
		return a
	else:
		return b
n=int(input())
ti=input().split()
ti=magic(ti)
ti.append(0)
ti.sort()
for i in range(1, n+1):
	if(ti[i]-ti[i-1]>15):
		ans=ti[i-1]
		break
	else:
		ans=ti[i]

print (min(ans+15, 90))