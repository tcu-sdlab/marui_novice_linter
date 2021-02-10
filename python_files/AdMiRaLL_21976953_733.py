s = input()
glas = ["A", "E", "I", "O", "U", "Y"]
prev = -1
result = 0
for i in range(len(s)):
    if s[i] in glas:
        result = max(i - prev, result)
        prev = i
result = max(i - prev + 1, result)
print(result)