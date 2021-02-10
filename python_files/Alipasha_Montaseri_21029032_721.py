q=input().split()
for i in range(2):
    q[i]=int(q[i])
n=q[0]
k=q[1]
seconds1=0
l=[]
wast1=0
wast2=0
seconds2=0
answer=0
for i in range(n+1):
    if n==i:
        answer=input()
    else:
        l.append(input())
for i in range(len(l)):
    if len(answer)>len(l[i]):
        seconds1=seconds1+1
        if seconds1%k==0:
            wast1=wast1+5
    if len(answer)>=len(l[i]):

        if seconds2%k==0 and seconds2!=0:
            wast2=wast2+5
        seconds2=seconds2+1
print(str(seconds1+wast1+1)+" ",end="")
print(str(seconds2+wast2),end="")