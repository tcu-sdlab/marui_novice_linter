s = input()
word = "CODEFORCES"
valid = False

for x in range(len(word) + 1):
    begin = word[:x]
    end = word[x:]
    valid = valid or (s.startswith(begin) and s.endswith(end))

print("YES" if valid else "NO")