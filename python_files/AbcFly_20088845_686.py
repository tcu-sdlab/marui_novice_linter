n = int(input())
al = list(map(int,input().split()))
for i in range(n):
    for j in range(n-1):
        if al[j]>al[j+1]:
            al[j],al[j+1] = al[j+1],al[j]
            print(j+1, j+2)