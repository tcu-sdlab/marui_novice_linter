x, y, z = map(int, input().split())
x1, y1, z1 = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
if y < 0:
	ans += A[0]
if y > y1:
	ans += A[1]
if z < 0:
	ans += A[2]
if z > z1:
	ans += A[3]
if x < 0:
	ans += A[4]
if x > x1:
	ans += A[5]
print(ans)