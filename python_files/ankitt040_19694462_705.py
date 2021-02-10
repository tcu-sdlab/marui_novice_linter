n= int( str(input()))

print('I hate',end='')
for i in range(n-1):
    if(i%2==0):
        print(' that I love',end='')
    else:
        print(' that I hate',end='')
print(' it')