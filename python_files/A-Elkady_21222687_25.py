n=int(input())
s=list(map(int,input().split()))
even=0;odd=0;x=0;y=0
for i in range(n):
                if s[i]%2==0:
                        even+=1
                        x=i
                else:
                        odd+=1
                        y=i   
print([(x+1),(y+1)][min(even,odd)==odd])