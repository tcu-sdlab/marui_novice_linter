import math
def lcm(a, b):
	return (a*b)//math.gcd(a, b)
n,a,b,p,q = map(int, input().split())
both = (n//lcm(a,b))
ans = (both)*max(p,q) + ((n//a - both) * p) + ((n//b - both) * q);
print(ans)