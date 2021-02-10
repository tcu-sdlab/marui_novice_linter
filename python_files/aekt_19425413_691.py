x = input()
if '.' not in x:
  x += '.'
a, b = x.split('.')
e = -len(b)
x = a + b
l, r = 0, len(x)-1
while x[l] == '0' and l < r:
  l += 1
while x[r] == '0' and l < r:
  r -= 1
  e += 1
a, b = x[l], x[l+1:r+1]
e += len(b)
if len(b) > 0:
  a += '.' + b
if e != 0:
  a += 'E' + str(e)
print(a)