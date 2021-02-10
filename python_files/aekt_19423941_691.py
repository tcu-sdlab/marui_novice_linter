n = int(input())
s = 0
for a in input().split():
  s += int(a)
if n == 1: s = n-s
print('YES' if s == n-1 else 'NO')