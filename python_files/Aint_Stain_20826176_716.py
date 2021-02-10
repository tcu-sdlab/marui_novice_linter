n,c=list(map(int,input().split()))
ara=list(map(int,input().split()))
k=1
for i in range(n-1):
	if (ara[i+1]-ara[i])<=c:
		k+=1
	else:
		k=1
print(k)