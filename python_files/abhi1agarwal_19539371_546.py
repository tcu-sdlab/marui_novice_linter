n=int(input())
a=input()
a=a.split()
#print(a)
for i in range(n):
	a[i]=int(a[i])
a=sorted(a)
pre=0
ans=0
for i in range(n):
	if a[i]<=pre:
		ans=ans+pre-a[i]+1
		pre=pre+1
	else :
		pre=a[i]
print(ans)