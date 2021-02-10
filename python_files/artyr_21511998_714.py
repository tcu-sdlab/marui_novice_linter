a = input().split()

l = a[0]
r = a[1]
l1 = a[2]
r1 = a[3]
k = a[4]

ansl = int(max(int(l), int(l1)))
ansr = int(min(int(r1), int(r)))

ans = 0
if int(k) >= int(ansl) and int(k) <= int(ansr):
	ans = -1

result = ans+ansr-ansl+1;

if int(r) < int(l1):
	print(0)
elif int(result) < 0:
	print(0)
else:
	print(int(ans)+int(ansr)-int(ansl)+int(1))