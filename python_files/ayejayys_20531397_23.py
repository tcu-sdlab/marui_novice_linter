s = input().strip()
mx = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        k = 0
        while ((j+k) < len(s) and s[i+k] == s[j+k]):
            k += 1
        mx = max(mx, k)
print(mx)