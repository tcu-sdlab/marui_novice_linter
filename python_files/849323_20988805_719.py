n  = int(input())
s = input()
s = list(s)

sr = ['r','b'] * (n//2)
sb = ['b','r'] * (n//2)
if n%2==1:
    sr.append('r')
    sb.append('b')

kb,kr = 0,0

for i in range(n):
    if s[i]!=sr[i]:
        if s[i] =='b':
            kb+=1
        else:
            kr+=1

u1 = min(kb,kr) + max(kb,kr) - min(kb,kr)

kb,kr = 0,0

for i in range(n):
    if s[i]!=sb[i]:
        if s[i] =='b':
            kb+=1
        else:
            kr+=1
            
u2 = min(kb,kr) + max(kb,kr) - min(kb,kr)

print(min(u1,u2))