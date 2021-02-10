def addo(n, num, lista):
	for i in range(n):
		lista.append(num)
	return lista

lis=[]
lis=addo(1001, False, lis)

n=int(input())
nums=input().split()
for i in range(n):
	k=int(nums[i])
	lis[k]=True

for i in range(2, 1001):
	if(lis[i]==lis[i-1] and lis[i]==lis[i-2] and lis[i]==True):
		print ('YES')
		raise SystemExit

print ('NO')