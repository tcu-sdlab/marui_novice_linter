n = int(input())
s = input()
types = set(list(s))
current_d = {}
i = j = 0
mn = len(s)
check = False
while j < n:
    while j < n and set(current_d) != types:
        current_d[s[j]] = current_d.get(s[j], 0)+1
        j += 1
    
    while set(current_d) == types:
        check = True
        current_d[s[i]] -= 1
        if not current_d[s[i]]:
            del current_d[s[i]]
        i += 1
    
    if check:
        mn = min(j-i+1, mn)
print(mn)