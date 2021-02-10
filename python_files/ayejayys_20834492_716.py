n,c = [int(x) for x in input().strip().split(' ')]
arr = list(map(lambda x:int(x), input().strip().split(' ')))
i = n-1
while ((arr[i] - arr[i-1]) <= c and i > 0):
   i-=1 
print(n-i)