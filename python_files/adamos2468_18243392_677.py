lis=input()
lis=lis.split()
n=int(lis[0])
h=lis[1]
c=0
lis=input()
lis=lis.split()
for i in range(n):
	if(int(lis[i])>int(h)):
		c+=2
	elif(int(lis[i])<=int(h)):
		c+=1
print(c)