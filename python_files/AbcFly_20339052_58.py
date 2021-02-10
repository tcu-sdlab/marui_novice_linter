s = input()
S = "hello"
index=0
for i in s:
    if i == S[index]:
        index+=1
        if index==5:
            break
print(["NO","YES"][index==5])