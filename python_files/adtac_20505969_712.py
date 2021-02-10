n = int(input())

r = [int(x) for x in input().split()] + [0]

a = []
for i in range(n):
    a.append(r[i] + r[i + 1])
print(" ".join([str(x) for x in a]))