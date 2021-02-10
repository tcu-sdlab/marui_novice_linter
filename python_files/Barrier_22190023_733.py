import sys

n = int(input())
ta = input().split()
a = [int(x) for x in ta]
m = int(input())
tb = input().split()
b = [int(x) for x in tb]

sum1,sum2 = 0,0 
for i in a:
    sum1 += i
for i in b:
    sum2 += i

if sum1 != sum2:
    print('NO')
    sys.exit(0)
    
s = []
idx = 0
for i in range(m):
    t = b[i]
    oo = idx
    mm = idx
    
    while t > 0:
        t -= a[idx]
        if a[mm] < a[idx]:
            mm = idx
        idx += 1
    if t < 0:
        print('NO')
        sys.exit(0)
    
    if mm == oo:
        while mm+1<idx and a[mm]==a[mm+1]:
            mm = mm+1
    
    flag = 0
    if mm-1>=oo and a[mm]>a[mm-1]:
        flag = 1
    elif mm+1<idx and a[mm]>a[mm+1]:
        flag = 2
    elif idx-oo == 1:
        continue
    
    if flag == 0:
        print('NO')
        sys.exit(0)
    elif flag == 1:
        for x in range(mm,oo,-1):
            s.append([x-oo+i,'L'])
        for x in range(mm,idx-1):
            s.append([i,'R'])
    elif flag == 2:
        for x in range(mm,idx-1):
            s.append([mm-oo+i,'R'])
        for x in range(mm,oo,-1):
            s.append([x-oo+i,'L'])

print('YES')
for x in s:
    print(str(x[0]+1)+' '+str(x[1]))