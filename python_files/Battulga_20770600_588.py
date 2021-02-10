n = int(input())
i = tmp = 1
while(i*i <= n):
    i+=1
    if(n%i==0):
        tmp *= i
        while(n%i==0):
            n //= i
print(n*tmp)