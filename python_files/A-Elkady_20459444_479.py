a=int(input())
b=int(input())
c=int(input())
x1=a+(b*c);x2=a*(b+c);x3=a*b*c;x4=(a+b)*c; x5=a+b+c;
ls=[x1,x2,x3,x4,x5]
ls.sort()
print(ls[-1])