n,m,k = map(int, input().split(" "))

paths = []
answer = -1

for i in range(m):
	paths.append(map(int, input().split(" ")))

if k > 0:
	storage = set(map(int, input().split(" ")))
else:
	storage = []

for path in paths:
    p = list(path)
    if answer == -1:
        if (p[0] in storage) ^ (p[1] in storage):
            answer = p[2]
    elif p[2] < answer:
        if (p[0] in storage) ^ (p[1] in storage):
            answer = min(answer, p[2])

print(answer)