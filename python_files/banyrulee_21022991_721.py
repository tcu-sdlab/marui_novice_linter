n = int(input())
s = input()

a = s.split('W')

print(len(a) - a.count(''))
for i in a:
    if i != '':
        print(len(i), end=' ')