import copy
n, m = map(int, input().split())
a = list(map(int, input().split()))
d = copy.copy(a)
a.sort()
s = n // m
b = [0] * m
cnt = 0
q = 0
for el in a:
    if el <= m and b[el - 1] < s:
        b[el - 1] += 1
        q += 1
ans = (n - q - n % m)
print(s, ans)
a = d
q = copy.copy(b) #
pos = 0
for el in a:
    if el <= m and b[el - 1] > 0:
        b[el - 1] -= 1
        print(el, end = ' ')
    else:
        while pos < m and q[pos] >= s:
            pos += 1
        if pos < m:
            q[pos] += 1
            print(pos + 1, end = ' ')
        else:
            print(el, end = ' ')
    #print(d)