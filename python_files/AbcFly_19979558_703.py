n = int(input())
mc = [0,0]
for i in range(n):
    m,c = map(int,input().split())
    if m>c: mc[0]+=1
    elif m<c: mc[1]+=1
if mc[0]>mc[1]:
    print("Mishka")
elif mc[0]<mc[1]:
    print("Chris")
else:
    print("Friendship is magic!^^")