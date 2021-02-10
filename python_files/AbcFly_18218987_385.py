s = input()
ans = 0
sindex = 0
for i in range(s.count("bear")):
    cindex = s.index("bear",sindex)
    ans+=(len(s)-cindex-3)*(cindex-sindex+1)
    sindex = cindex + 1
print(ans)