import sys

n = int(input())
a = 1234567
b = 123456
c = 1234
da = {0}
db = {0}
dc = {0}

try:
	for i in range(812):
		for j in range(8102):
			if (n - (a * i) - (b * j) < 0):
				break
			if (n - (a * i) - (b * j)) % c == 0:
				sys.exit(0)
	print("NO")
except:
	print("YES")