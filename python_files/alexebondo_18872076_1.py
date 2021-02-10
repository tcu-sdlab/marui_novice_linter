a=str(input())
m=""
n=""
x=""
i=0
while a[i] !=" ":
      n=n+a[i]
      i+=1
i+=1
while a[i] !=" " :
      m=m+a[i]
      i+=1
i=i+1
while i < len(a) :
      x=x+a[i]
      i+=1
m=int(m)
n=int(n)
x=int(x)
if m%x == 0 :
      a1=m/x
else :
      a1=int(m/x)+1
if n%x == 0 :
      a2=n/x
else :
      a2=int(n/x)+1
print (int(a1*a2))