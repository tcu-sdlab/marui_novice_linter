s = input()
S = s.upper()
tl = len(s)
cnt = 0
for i in range(tl):
    if s[i]==S[i]:
        cnt+=1
if cnt>tl//2:
    print(S)
else:
    print(s.lower())