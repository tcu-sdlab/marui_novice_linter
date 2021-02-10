n = int(input())
data = list(map(int, input().split()))
n = sum(map(lambda x: x & 1 > 0, data))
if n & 1:
  msg = "NO"    
else:
  flag = False
  msg = "YES"
  for v in data:
    if not v and flag:
      msg = "NO"    
    elif v & 1 > 0:
      flag = not flag
print(msg)