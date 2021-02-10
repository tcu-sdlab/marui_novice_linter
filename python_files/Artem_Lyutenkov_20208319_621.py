n = int(input())
inp = list(map(int,  input().split()))
sm = 0
mn = 100000000000000000
for i in inp:
   if i % 2:
      mn = min(i,mn)
   sm += i
if sm % 2:
   sm -= mn
print(sm)