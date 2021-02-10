inp = input()
pan = len(inp)
c = inp[pan-1]
r = int(inp[:-1])
tambah = 0
if (c == 'a'):
	tambah = 4
elif (c == 'b'):
	tambah = 5
elif (c == 'c'):
	tambah = 6
elif (c == 'd'):
	tambah = 3
elif (c == 'e'):
	tambah = 2
elif (c == 'f'):
	tambah = 1

r = r-1
div = r // 4
mod = r % 4
ans = div * 16
if (mod == 1):
	ans += 7
elif (mod == 3):
	ans += 7

ans += tambah
print(ans)