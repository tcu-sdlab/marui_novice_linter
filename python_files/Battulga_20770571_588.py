n = int(input())
i = 2
tmp = 1
while(i*i <= n):
    if(n%i==0):
        tmp=tmp*i
        while(n%i==0):
            n = n//i
    i=i+1
print(n*tmp)