import sys
#sys.stdin = open("apples.in","r")
#sys.stdout = open("apples.out","w")


n, d = list(map(int, sys.stdin.readline().split()))
lst = []
day = []
for i in range(d):
    lst.append(input())
for i in range(d):
    for j in range(n):
        if lst[i][j] == "0":
            day.append(1)
            break
    else:
        day.append(0)

cnt = 0
maxx = 0
for i in day:
    if i == 1:
        cnt += 1
        if cnt > maxx:
            maxx = cnt
    else:
        cnt = 0
print(maxx)


    
#sys.stdin.close()
#sys.stdout.close()