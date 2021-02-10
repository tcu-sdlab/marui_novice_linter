input()
l = [int(x) for x in input().split()]
Min = l[0]
Max = l[0]
ans = 0
for x in l[1:]:
	if x < Min:
		ans += 1
		Min = x
	if x > Max:
		ans += 1
		Max = x
print(ans)