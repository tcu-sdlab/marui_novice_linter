n = int(input())
fr = list(map(int, input().split()))
k = int(input())
to = list(map(int, input().split()))

def process(l, off):
  #print(l, end=": ")
  #print(off)
  res = []
  m = max(l)
  mi = l.index(m)
  if mi == 0 and all(map(lambda x: x == m, l)):
    return res
  if not mi:
    for i in range(1, len(l)):
      if l[i] < m:
        mi = i-1
        res.append((off+i-1, 'R'))
        break

  for i in range(mi,0,-1):
    res.append((off+i, 'L'))
  for i in range(len(l) - len(res) - 1):  
    res.append((off, 'R'))
  #print(res)  
  return res  

#print(fr)
#print(to)
   
st = 0
res = []
good = True
for off in range(k):
  x = to[off]
  #print(x)
  if st == n:
    good = False
    break
  elif x == fr[st]:
    st += 1
  else:  
    s = 0
    for fn in range(st, n):
      s += fr[fn]
      if s == x:
        t = process(fr[st:fn+1], off+1)
        if t:
          st = fn + 1
          res.extend(t)
        else:  
          good = False
        break
      elif s > x:  
        good = False
        break
    if not good: break
  
if good: good = (st == n)  
  
if good:
  print("YES")  
  for x,y in res:
    print(x, end = " ")
    print(y)
else:  
  print("NO")