n,h,k = map(int, input().split())
a = list(map(int, input().split()))

i,rem,ans = 0,0,0

while i < n:
	while i < n and rem + a[i] <= h:
		rem += a[i]
		i += 1
	ans += rem // k
	rem %= k
	if(i < n and rem + a[i] > h):
		rem = 0
		ans+=1
if(rem > 0):
	ans += 1
print(ans)