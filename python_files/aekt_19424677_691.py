s = input()
a = 'aBCcDEeFfGghiJjKkLlmNnPQRrSstuyZz'
b = 'AbdHIMOopqTUVvWwXxY'
c = 'AdbHIMOoqpTUVvWwXxY'
f = True
n = len(s)
for i in range(0, n):
  if s[i] in a:
    f = False
  elif c[b.index(s[i])] != s[n-i-1]:
    f = False
  if f == False:
    break
print('TAK' if f else 'NIE')