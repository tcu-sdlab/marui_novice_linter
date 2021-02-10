n, k = map(int, input().split())

ps = []
for i in range(0, n):
    ps.append(input())
pwd = input()

ps.sort(key=lambda p: len(p))

c = sum(len(p) < len(pwd) for p in ps)
mn = c + c // k * 5 + 1

c = sum(len(p) <= len(pwd) for p in ps)
mx = c + (c - 1) // k * 5

print("%d %d" % (mn, mx))