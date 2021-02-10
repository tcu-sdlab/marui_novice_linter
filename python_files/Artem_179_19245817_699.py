from collections import deque
n = int(input())
A = list(map(int, input().split()))
answer = 0
t = 0
answer = 0
for i in range(n):
    if A[i] == 0:
        t = 0
    elif A[i] == 1:
        if t != 1:
            answer +=1
            t = 1
        else:
            t = 0
    elif A[i] == 2:
        if t!=2:
            answer +=1
            t = 2
        else:
            t = 0
    else:
        if t == 1:
            t = 2
            answer+=1
        elif t == 2:
            t = 1
            answer +=1
        else:
            t = 0
            answer+=1
print(n-answer)