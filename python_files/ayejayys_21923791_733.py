s = input()
mx = 0  
last = -1
vowels = list('AEIOUY')
for i in range(len(s)):
    if s[i] in vowels:
        mx = max(mx, i-last)
        last = i
mx = max(mx, i-last+1)
print(mx)