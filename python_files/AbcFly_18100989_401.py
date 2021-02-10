from math import ceil
n,x = map(int, input().split())
data = list(map(int, input().split()))
cnt = abs(sum(data))

print(ceil(cnt/x))