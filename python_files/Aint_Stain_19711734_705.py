#Ami ekta  bokchod
n =int(input())
a=list(map(int,input().split()))
b=2
for i in a:
    if i % 2 == 0:
        b=3-b
    print(b)