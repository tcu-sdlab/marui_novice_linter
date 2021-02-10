k = int(input())*2
s = ""
for i in range(4):
    s+=input()
ls = []
for c in "0123456789":
    ls.append(s.count(c))
if max(ls)>k:
    print("NO")
else:
    print("YES")