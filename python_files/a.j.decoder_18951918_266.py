n,t=map(int,input().split())
q=input()
for qwerty in range(t):
    t=''
    i=0
    while i<n:
        if q[i]=='B' and i<n-1 and q[i+1]=='G':
            t+='GB'
            i+=1
        else:
            t+=q[i]
        i+=1
    q=t
print(q)