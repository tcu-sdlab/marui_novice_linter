n = int(input())
ans=[]
for i in range(n):
    ans += [input()]
ans = "\n".join(ans)
if ans.count("OO"):
    print("YES")
    print(ans.replace("OO", "++",1))
else:
    print("NO")