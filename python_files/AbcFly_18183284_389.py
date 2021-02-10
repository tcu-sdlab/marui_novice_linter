n = int(input())
data = list(map(int,input().split()))
data.sort()
while data[n-1]>data[0]:
    data[n-1]-=data[0]
    data.sort()
print(sum(data))