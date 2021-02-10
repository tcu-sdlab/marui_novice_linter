s=input().split("+")
s.sort()
x=s[0]
for i in range(1,len(s)):
                x=x+'+'+s[i]
print(''.join(x))