n,d= map(int,input().split())
res= [0]
for i in range(d):    
    if input().count("0"):
        res+=[res[i]+1]        
    else:
        res+=[0]
res.sort(reverse=True)
print(res[0])