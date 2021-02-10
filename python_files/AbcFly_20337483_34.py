n = int( input())
al = list(map(int, input().split()))
hl = []
for i in range(n):
    hl += [abs(al[(i+1)%n]-al[i])]
index = hl.index(min(hl))
print(index+1, (index+1)%n+1)