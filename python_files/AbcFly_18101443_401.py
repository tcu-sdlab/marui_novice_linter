n,k = map(int,input().split())
set1 = set(range(1,n))
for i in range(k):
    mylist = list(map(int,input().split()[1:]))
    set1 -= set(mylist)
set2 = set(set1)
for i in range(1,n):
    if i in set2:
        set2-=set([i+1])
        
print(len(set2),len(set1))