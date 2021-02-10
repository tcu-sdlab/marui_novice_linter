s = input()
notfound = True

if len(s) >= 26:
  d = {'?':0}
  for ch in s[:26]:
    if ch != '?':
      if ch in d:
        d[ch] += 1
      else:  
        d[ch] = 1
        
  for i in range(len(s) - 25):
    if max(d.values()) < 2:
      ss = list(s[i:i+26])
      fill = list(filter(lambda c: c not in d or d[c] == 0, [chr(i+ord('A')) for i in range(26)]))
      for k in range(26):
        if ss[k] == '?':
          ss[k] = fill.pop()
      print(s[:i].replace("?", "A"), end = "")    
      print("".join(ss), end = "")    
      print(s[i+26:].replace("?", "Z"))    
      
      notfound = False
      break
    if i < len(s) - 26:  
      ch = s[i]  
      if ch != '?':
        d[ch] -= 1
        
      ch = s[i+26]  
      if ch != '?':
        if ch in d:
          d[ch] += 1
        else:  
          d[ch] = 1
        
if notfound:   
  print(-1)