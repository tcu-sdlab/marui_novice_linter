def roundroot():
    global root
    i = len(root)-1
    while i>=0:
        root[i]+=1
        if root[i] == 10 and i!=0:
            root[i] = 0
            i-=1
        else:
            break

def printA(a):
    for i in a:
        print(i,end='')


n,t = [int(i) for i in input().split()]

num = input()

for i in range(len(num)):
    if num[i]=='.':
        break

root = [int(j) for j in num[:i]]
dec = [int(j) for j in num[i+1:]]

n = len(dec)

#print(dec)

itrack = -1


for i in range(n):
    if dec[i]>=5:
        itrack = i
        break

if itrack == -1:
    itrack = n-1

while (itrack>=1 and t>0):
    if dec[itrack] < 5:
        break
    j = itrack - 1
    t-=1
    while (j>=0):
        dec[j]+=1
        if dec[j]==10:
            dec[j] = 0
            j-=1
        else:
            break
    if j==-1:
        roundroot()
    itrack = j
        
if (itrack>=0 and t>0 and dec[0]>=5):
    roundroot()
    printA(root)
else:
    printA(root)
    print('.',end='')
    for i in range(itrack+1):
        print(dec[i],end='')