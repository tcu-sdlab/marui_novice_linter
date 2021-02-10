l1, r1, l2, r2, k = map(int, input().split())
d = min(r1, r2) - max(l1, l2) + 1
if k >= max(l1, l2) and k <= min(r1, r2):
	d -= 1
print(max(0, d))