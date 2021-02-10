import re

s = input().strip()
# s = "0                          ".strip()

mas = re.split("[a-z]+", s)

res = []

for el in mas:
	if not len(el):
		continue
	if len(el) > 3 and el[-3] == ".":
		el = el[:-3] + "," +  el[-2 :]

	res.append(el)


ans = .0

for el in res:
	el = el.replace(".", "")
	el = el.replace(",", ".")
	ans += float(el)

ans = float("{0:.2f}".format(ans))


s = str(ans).replace(".", ",")

if len(s) <= 2:
	print(s)
	exit(0)
# elif len(s) == 3:
# 	if "," in s:
# 		res = s[0] + "." + s[2]
# 		print(res)
# 	else:
# 		print(res)
# 	exit(0)

if not ("," in s):
	result = s[0]
	for i in range(1, len(s)):
		if not ((len(s) - i) % 3):
			result += "."
		result += s[i]
		print(result)
		exit(0)

ans_int, ans_frac = int(s[:s.index(",")]), (s[s.index(",") + 1:]) 

# print(ans_int, ans_frac)

a = str(ans_int)

result = a[0]

for i in range(1, len(a)):
	if not ((len(a) - i) % 3):
		result += "."
	result += a[i]

if int(ans_frac) != 0:
	result += "."
	result += ans_frac
	if len(ans_frac) == 1:
		result += "0"
print(result)