# cook your dish here
from sys import stdout
p=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
f=[0]*15
x=0
flag=0
while x<15 and flag==0:
	stdout.write(str(p[x])+'\n')
	stdout.flush()
	r=input()
	if r=='yes':
		f[x]=1
		t=p[x]*p[x]
		while(t<=100):
			stdout.write(str(t) + '\n')
			stdout.flush()
			r=input()
			t*=p[x]
			if r=='yes':
				stdout.write(str('composite' + '\n'))
				stdout.flush()
				flag=1
				break
			else:
				break
	x+=1
if flag==0:
	if f.count(1)==0 or f.count(1)==1:
		stdout.write('prime' + '\n')
	else:
		stdout.write('composite' + '\n')
	stdout.flush()