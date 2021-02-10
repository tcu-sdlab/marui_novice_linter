s = input()
a = 'aBCcDEeFfGghiJjKkLlmNnPQRrSstuyZz'
b = 'AbdHIMOopqTUVvWwXxY'
c = 'AdbHIMOoqpTUVvWwXxY'
f = True
for x in a:
  if x in s:
    f = False
n = len(s)
if f:
  for i in range(0, n):
    if c[b.index(s[i])] != s[n-i-1]:
      f = False
print('TAK' if f else 'NIE')