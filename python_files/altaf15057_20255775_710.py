N=int(input())
numbers = [int(n) for n in input().split()]
numbers.sort()
if(N%2==1):
    Ans=numbers[N//2]
    print(Ans)
else:
    Ans=numbers[(N//2)-1]
    print(Ans)