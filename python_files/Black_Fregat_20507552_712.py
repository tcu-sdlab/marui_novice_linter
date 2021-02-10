s = input()
if len(s) % 2:
	print(-1)
else:	
	d = {"U":0, "D":0, "L":0, "R":0}
	for ch in s:
		d[ch] += 1
	d1 = abs(d["U"]-d["D"])
	d2 = abs(d["L"]-d["R"])
	print((d1+d2)//2)