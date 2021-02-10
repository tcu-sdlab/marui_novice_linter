s=int(input())
while s>0:
    
    n =str(input())
    print(n) if len(n)<11 else print ("{}{}{}".format(n[0],len(n)-2 ,n[-1]) )
    s-=1