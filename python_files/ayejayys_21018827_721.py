n = int(input().strip())
s = input().strip()
i = 0
l = []
start = 0
while i < n:
    if s[i] == 'B':
        start = i
    else:
        i += 1
        continue
    while i < n and s[i] == 'B':
        i+=1
    l.append(i-start)
print(len(l))
if len(l):
    print(" ".join([str(x) for x in l]))