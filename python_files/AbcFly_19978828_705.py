n = int(input())
sl = [" that I love"," that I hate"]
res="I hate"
for i in range(2,n+1):
    res+=sl[i%2]
res+=" it"
print(res)