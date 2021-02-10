s = input()
cur = 'a'
count = 0
for ch in s:
  x = (26 + ord(ch) - ord(cur)) % 26
  count += min(x, 26-x) 
  cur = ch
print(count)