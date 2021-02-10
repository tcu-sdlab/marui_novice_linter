n=int(input())
s=input()
l=[]
sp=s.split('W')
for a in sp:
    tmp=sum(1 if b=='B' else 0 for b in a)
    if tmp!=0:
        l.append(tmp)
print(len(l))
if len(l)!=0:
    print(' '.join(str(a) for a in l))