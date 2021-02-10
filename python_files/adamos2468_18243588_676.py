def max(a, b):
	if(a>b):
		return a
	else:
		return b

def magic(lista):
	for i in range(len(lista)):
		lista[i]=int(lista[i])
	return lista

n=int(input())
lis=input()
lis=lis.split()
lis=magic(lis)
mith=-1
math=-1
for i in range(n):
	if(lis[i]==1):
		mith=i
	if(lis[i]==n):
		math=i
	if(mith!=-1 and math!=-1):
		break
ans=max(max(mith, math), max(n-1-mith, n-1-math))
print (ans)