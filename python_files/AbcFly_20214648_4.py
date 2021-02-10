nl = {}
ans = []
for i in range(int(input())):
    s = input()
    c = nl.get(s)
    if c is None:
        ans+=["OK"]
        nl[s]=1
    else:
        ans+=[s+str(c)]
        nl[s]=c+1
        
print("\n".join(ans), end="")