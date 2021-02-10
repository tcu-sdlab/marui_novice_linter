input()
s = input() + 'W'

cnt = 0
ans = []
for c in s:
    if c is 'W':
        if cnt > 0:
            ans.append(cnt)
            cnt = 0
    else:
        cnt += 1

print(len(ans))
print(" ".join(map(str, ans)))