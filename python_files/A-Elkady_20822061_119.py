from fractions import gcd
a,b,n=map(int,input().split());x=0
while(n>0):
                x=gcd(a,n)
                n-=x
                if x>n:print('0');break
                x=gcd(b,n)
                n-=x
                if x>n:print('1');break