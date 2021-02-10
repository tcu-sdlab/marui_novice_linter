s = input()


current = 0
result = 0
for i in s:
    numb = ord(i) - ord('a')
    result += min(abs(current - numb),
                  abs(26 - numb + current),
                  abs(26 + numb - current))
    current = numb
print(result)