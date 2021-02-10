n, k = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]

l = []

for i in s:
    if i <= 0 or i < s[k - 1]: break
    l.append(i)

print(len(l))