s = input()
index = s.find("^")
ls = []
for k,c in enumerate(s):
    if str.isdigit(c):
        ls.append(int(c)*(index-k))
ans = sum(ls)
if ans<0:
    print("right")
elif ans>0:
    print("left")
else:    
    print("balance")