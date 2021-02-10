s = list(input())
last = ""

for i in range(len(s)):
	if s[i] == last:
		if i + 1 == len(s):
			if last != "a":
				s[i] = "a"
			else:
				s[i] = "b"
		else:
			if s[i+1] != "a" and last != "a" :
				s[i] = "a"
			elif s[i+1] == "b" or last == "b":
				s[i] = "c"
			else:
				s[i] = "b"
	last = s[i]

print("".join(s))