a = int(input(''))
if a%2:
    n = (a-1)//2
    b = 2*n*n+2*n
    c = 2*n*n+2*n+1
else:
    n = a//2
    b = n*n-1
    c = n*n+1
if a<= 2:
    print('-1')
else:
    print('%d %d' % (b,c))