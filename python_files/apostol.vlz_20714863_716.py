s = str(input())
s = s.strip()
k = 0
result = False
while True:
    if (len(s) - k < 26):
        break
    t = s[k:26 + k]
    k = k + 1
    x = set(t)
    b = t.count("?")
    if "?" in x:
        x.remove("?")
    if (len(x) + b == 26):
        result = True
        t = list(t)
        for i in range(len(t)):
            if t[i] == "?":
                for z in range(26):
                    if chr(ord("A") + z) not in t:
                        t[i] = chr(ord("A") + z)
                        break
        res = "".join(t)
        res = s[0:k - 1] + res
        res = res + s[26 + k - 1:]
        res = res.replace("?", "A")
        print(res)
        break
if not result:
    print("-1")