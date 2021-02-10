n = int(input())
nl = [int(i)%2 for i in input().split()]
print(nl.index(nl.count(1)==1)+1)