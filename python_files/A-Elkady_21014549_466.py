n,m,a,b=map(int,input().split())
print(min((n//m)*b+a*(n%m),((n//m)+1)*b,n*a))