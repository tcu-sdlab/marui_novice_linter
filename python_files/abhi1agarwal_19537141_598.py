s=['1']+list(input())
m=int(input())
n=len(s)-1;
yy=list(s)
i=0
while i<m:
	xx=input()
	l,r,k=xx.split()
	l=int(l)
	r=int(r)
	k=int(k)
	k=k%(r-l+1)
	j=l
	# yy=[] # r-l+1
	ind=((-k+r-l+1)%(r-l+1) + (r-l+1) )%(r-l+1)
	while j<=r :
		yy[j]=s[l+ind]
		# print(ind)
		ind=ind+1;
		if ind>=r-l+1:
			ind=ind-(r-l+1)
		j=j+1
		# print l+((j-l-k)%(r-l+1)+r-l+1)%(r-l+1)
	s=list(yy)
	i=i+1
i=1
while i<=n :
	print(s[i],end="")
	i=i+1
print()