n = int(input())
A = list(map(int,input().split()))
tf = False
ma = max(A)
mi = min(A)
sr = (ma+mi)/2
for i in A:
    if i==ma or i==mi or i==sr:
        tf = True
    else:
        print('NO')
        exit()
if tf:        
    print('YES')