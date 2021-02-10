import sys

n = int(sys.stdin.readline())
chars = list(sys.stdin.readline().strip())

count = 0
curSize = 0

sizes = []

for i in range(n):
    if chars[i] == "B":
        curSize += 1
    elif chars[i] == "W":
        if curSize != 0:
            count += 1
            sizes.append(curSize)
            curSize = 0

if curSize != 0:
    sizes.append(curSize)
    count += 1

print(count)
if count != 0:
    print(" ".join(map(str, sizes)))