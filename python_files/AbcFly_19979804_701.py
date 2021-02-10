n = int(input())
al = list(map(int,input().split()))
for i in range(n):
    al[i]=[al[i],i+1]
al.sort()
for i in range(n//2):
    print(al[i][1],al[n-i-1][1])