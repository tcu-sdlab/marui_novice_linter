n=int(input())
tl = list(map(int, input().split()))
time=cnt=0
while cnt <15 and time<90:
    time+=1
    if tl.count(time)>0:
        cnt=0
    else:
        cnt+=1
print(time)