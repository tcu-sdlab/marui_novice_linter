n,k = map(int,input().split())
ll = []
for i in range(n):
    ll.append(len(input()))
ll.sort()
l = len(input())
ft = ll.index(l)+1
lt = n-ll[::-1].index(l)
print(ft+((ft-1)//k)*5, lt+((lt-1)//k)*5)