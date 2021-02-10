def Count(n):
	if n == 0:
		return 0
	c = Count(n // 10)
	return n % 10 if n % 10 > c else c

def QNum(n):
	if n <= 0:
		return

	nn = n
	newN = 0
	string = ""
	p = 0
	out = 0
	while nn > 0:
		d = nn % 10
		nd = d - 1 if d > 0 else 0
		ndd = 1 if d > 0 else 0

		nn = nn // 10

		newN += nd * 10 ** p
		out += ndd * 10 ** p
		p += 1

	print(out)
	QNum(newN)

n = int(input())
print(Count(n))
QNum(n)