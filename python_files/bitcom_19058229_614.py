# your code goes here
arr = input().split(' ')
l = int(arr[0])
r = int(arr[1])
k = int(arr[2])
cur = int(1)
while cur < l:
	cur *= k
	
fl = False
ans = 0
while (cur <= r):
	fl = True
	print(cur, end=' ')
	cur *= k
	
if fl == False:
	print(-1)