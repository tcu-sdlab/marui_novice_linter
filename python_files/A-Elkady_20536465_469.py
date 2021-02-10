n=int(input())
p=list(map(int,input().split()[1:]))
q=list(map(int,input().split()[1:]))
p.extend(q);a=set(p)
if len(a)==n:print("I become the guy.")
else :print("Oh, my keyboard!")