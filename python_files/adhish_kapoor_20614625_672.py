# cook your dish here
n=int(input())
a=input()
a=list(a)
c=0
a.sort()
if(n>26):
    print(-1)
else:
    for i in range(n-1):
         if(a[i]==a[i+1]):
               c+=1
    print(c)