n = int(input())
al = list(map(int,input().split()))
s= 0
for i in al:
    s+=i-1
    print([1,2][(s-1)%2])