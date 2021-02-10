a,b = input(), input()
ans=""
for i in range(len(a)):
    if a[i]==b[i]: ans+="0"
    else: ans+="1"
print(ans)