s=input()
aa=list(s)
bb=list(s)
length=len(s)
q=int(input())
while(q!=0):
	a=(input()).split()
	a[0]=int(a[0])-1
	a[1]=int(a[1])-1
	a[2]=int(a[2])
	count=0
	temp=a[2]%(a[1]-a[0]+1)
	lenn=(a[1]-a[0]+1)
	for i in range(a[0]+temp,a[0]+lenn):
		bb[i]=aa[a[0]+count]
		count+=1
		#print(count)
	for i in range(a[0],a[0]+temp):
		bb[i]=aa[a[0]+count]
		count+=1
		#print(count)
	for i in range(length):
		aa[i]=bb[i]
	q=q-1;
for i in range(length):
	print(bb[i],end="")
print()