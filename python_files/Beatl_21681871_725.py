if True:
  s = input()

  r = int(s[0 : len(s)-1])
  #print(r)
  p = s[len(s)-1]
  #print(p)
  
  r-= 1

  res = (r // 4)*16

  if (r % 4 == 1) or (r % 4 == 3):
    res+= 7
  

  if(p == 'f'):
    res+= 1
  if(p == 'e'):
    res+= 2
  if(p == 'd'):
    res+= 3
  if(p == 'a'):
    res+= 4
  if(p == 'b'):
    res+= 5
  if(p == 'c'):
    res+= 6

  print(res)