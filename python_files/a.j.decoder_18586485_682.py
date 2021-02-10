a,b=map(int,input().split())
re=0
res=0
for i in range(1,1+5):
    re=(b+(i%5))//5
    t=(a+(5-i))//5
    res+=re*t
print(res)