res=0
xx=input()
k,n,w=xx.split()
k=int(k)
n=int(n)
w=int(w)
res=(k*w*(w+1))>>1
if res>n:
	print(int(res-n))
else :
	print(0)