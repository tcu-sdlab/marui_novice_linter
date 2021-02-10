y=int(input())
for i in range(y+1,9013,1):
    if(len(set(str(i)))==len(str(i))):
        print(i)
        break