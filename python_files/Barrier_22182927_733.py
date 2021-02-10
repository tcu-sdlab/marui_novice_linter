a = input()
a = a.strip()
l = len(a)
s = set('AEIOUY')
pre = -1
Max = 0
for i in range(l):
    if a[i] in s:
        temp = i - pre
        pre = i
        if Max < temp:
            Max = temp
Max = max(Max,l-pre)
print(Max)