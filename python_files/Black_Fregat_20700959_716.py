n = int(input())
current = 2
for i in range(n):
  next = (i+1) * (i+2)
  press = (i+1) * (i+2) * (i+2) - current // (i+1)
  current = next  
  print(press)