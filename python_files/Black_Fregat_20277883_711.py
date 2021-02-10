n = int(input())
data = [list(map(int, input().split())) for i in range(n)]

if n == 1:
  print(1) 
else:  

  for i in range(n):
    if 0 in data[i]:
      y = i
      x = data[i].index(0)
      break

  sums = [0]*n
  sg = 0 
  sp = 0    
  plus = set()
  minus = set()    
  for i in range(n):
    temp = sum(data[i])
    if i == y:
      minus.add(temp)
    else:
      plus.add(temp)
      
    sums = [sums[k] + data[i][k] for k in range(n)]
    sg += data[i][i]  
    sp += data[i][n-i-1]

  for i in range(n):
    if i == x:
      minus.add(sums[i])
    else:
      plus.add(sums[i])
      
  if x == y:
    minus.add(sg)
  else:
    plus.add(sg)
  
  if x == n-y-1:
    minus.add(sp)
  else:
    plus.add(sp)
  
  res = -1
  if len(plus) == 1 and len(minus) == 1:
    res = plus.pop() - minus.pop()
  if res <= 0:
    res = -1
  print(res)