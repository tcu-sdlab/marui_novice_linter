n, k = map(int, input().split())
s = list(input())
dot = s.index(".")

pos =-1
for i in range(dot+1, n):
  if s[i] > "4":
    pos = i
    break
    
if pos < 0:
  print("".join(s))
else:  
  for j in range(k):
    if s[pos-1-j] != "4":
      break
  pos = pos-1-j    
  while pos >= 0 and (s[pos] == "9" or pos == dot):
    pos -= 1
    
  if pos < 0:
    print("1", end = "")
    print("0"*dot)
  elif pos < dot: 
    print("".join(s[:pos]), end = "")
    print(chr(ord(s[pos])+1), end = "")
    print("0"*(dot-pos-1))
  else:  
    print("".join(s[:pos]), end = "")
    print(chr(ord(s[pos])+1))