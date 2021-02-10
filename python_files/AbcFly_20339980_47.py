n = int(input())
al = []
for i in range(1,500):
    ans=i*(i+1)//2
    if ans<501:
        al+=[ans]
    else:
        break
print(["NO","YES"][al.count(n)])