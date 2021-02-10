v = "aeiouy"
n = int(input())
p = list(map(int, input().split()))
d = [sum(map(lambda x: x in v, input())) for i in range(n)]
if d == p:
  print("YES")
else:  
  print("NO")