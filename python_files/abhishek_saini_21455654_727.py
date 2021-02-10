import re
line = input()
line = re.findall(r"[0-9.]+", line)
# for i in range(0,26):
# 	p = str(chr(ord('a')+i))
# 	# print p
# 	line="".join(line).split(p)
a=0
b=0
# print (line)
for val in line:
	n = len(val)
	if n<=2:
		a+=int(val)
		continue
	j = n
	if val[n-3]=='.':
		b+=int(val[n-2:])
		j = n-2
	curr = 0
	i = 0
	while i<j:
		if val[i]!='.':
			curr=curr*10+int(val[i])
		i+=1
	a+=curr
a+=b//100
b=b%100
a=str(a)
n=len(a)
for i in range(n):
	if (n-i)%3==0 and i!=0:
		print ('.',end="")
	print (a[i],end="")
if b!=0:
	print ('.',end="")
	if b<10:
		print ('0',end="")
	print (b,end="")