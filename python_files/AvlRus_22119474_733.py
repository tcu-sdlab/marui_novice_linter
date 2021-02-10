n=[sum(map(int,('-'+input()).split())) for i in range(int(input()))]
s,a,b=sum(n),min(n),max(n)
if abs(s+a*(-2))>abs(s) and abs(s+a*(-2))>abs(s+b*(-2)) :print(n.index(a)+1)
elif abs(s+b*(-2))>abs(s):print(n.index(b)+1)
else:print(0)