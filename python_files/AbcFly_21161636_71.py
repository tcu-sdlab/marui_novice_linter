sl = []
for i in range(int(input())):
    s = input()
    if len(s)>10:
        s=s[0]+str(len(s)-2)+s[::-1][0]
    sl.append(s)
print("\n".join(sl))