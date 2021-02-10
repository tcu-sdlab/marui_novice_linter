s = input()
r = int(s[:-1]) - 1
st = s[-1]

if st == 'f':
    st = 1
if st == 'e':
    st = 2
if st == 'd':
    st = 3 
if st == 'a':
    st = 4
if st == 'b':
    st = 5
if st == 'c':
    st = 6
ans = r // 4 * 16
r = r % 4
if r == 0 or r == 2:
    ans += st
else:
    ans += st + 7
print(ans)