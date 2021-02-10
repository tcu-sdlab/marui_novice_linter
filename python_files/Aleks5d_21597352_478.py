def main():
    a, b=[int(i) for i in input().split()]
    m=a//b
    n=b-a%b
    print((m-1)*n*m//2+(b-n)*(m+1)*m//2, (a-b+1)*(a-b)//2)


main()