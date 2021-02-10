n = int(input())
l = [0 for i in range(n)]
r = [0 for i in range(n)]
leftSumm = 0
rightSumm = 0
for i in range(n):
    l[i], r[i] = list(map(int, input().split()))
    leftSumm += l[i]
    rightSumm += r[i]

result = -1
maxresult = abs(leftSumm - rightSumm)
for i in range(n):
    tempLeft = leftSumm - l[i] + r[i]
    tempRight = rightSumm -r[i] + l[i]
    if abs(tempLeft - tempRight) > maxresult:
        maxresult = abs(tempLeft - tempRight)
        result = i
print(result+1)