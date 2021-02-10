n, k = map(int, input().split())
HASH = [0] * 101

for i in range(n):
    s = input()
    # print (s)
    HASH[len(s)] += 1

ans = len(input())
res = sum(HASH[:ans])

print (1 + res + int(res/k) * 5,
       res + HASH[ans] + int((res + HASH[ans] - 1) / k) * 5)