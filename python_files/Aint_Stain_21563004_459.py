inputsize=int(input())
ara=list(map(int,input().split()))
counta=0
ara.sort()
difference=ara[inputsize-1]-ara[0]
if(not difference==0):
    counta=ara.count(ara[-1])*ara.count(ara[0])
else:
    counta=inputsize*(inputsize-1)//2
#for i in range (inputsize):
    #if i==i+1:
        #count1+=1
print(difference,end=" ")
print(counta)