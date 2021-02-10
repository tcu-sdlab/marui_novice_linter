x = input().lower()
t = []
for i in x:
    if not i in 'aeiouy':
        t.append(i)
t = ''.join(['.' + i for i in t])
print(t)