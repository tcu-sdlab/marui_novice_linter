import collections


n = int(input())
p = input().split()
flag = True

for i in range(n):
    string = input()
    
    c = collections.Counter(string)

    t = 0
    for letter in 'aeiouy':
        t += c[letter]

    if t != int(p[i]):
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")