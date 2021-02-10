n,m = map(int, input().split())
A = [0] * n
B = [0] * n
per = 0
per2 = 0
for i in range(m):
    a,b= map(int, input().split())
    if A[a-1] == 0:
        A[a-1] = 1
        per+=1
    if B[b-1] == 0:
        B[b-1] = 1
        per2 +=1
    print((n-per) * (n-per2))