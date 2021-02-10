st = input()
letters = "qwertyuiopasdfghjklzxcvbnm"
for c in letters:
 st = st.replace(c, ' ')
st = st.split()
sm = 0
for s in st:
 cents = "00"
 if len(s) > 2 and s[len(s)-3] == '.':
  cents = s[-2:]
  s=s[:-3].replace('.','')
 else:
  s = s.replace('.','')
 s = s + cents
 sm = sm + int(s)
cents = str(sm%100)[:2]
s = str(sm//100)
st = ""
for i in range(len(s), 0, -3):
 st = '.' + st
 if i-3 > 0:
  st = s[i-3:i] + st   
 else:
  st = s[0:i] + st
if len(cents) == 2:
 st = st + cents
elif len(cents) == 1 and cents != "0":
 st = st + "0" + cents
else:
 st = st[0:-1]
print(st)