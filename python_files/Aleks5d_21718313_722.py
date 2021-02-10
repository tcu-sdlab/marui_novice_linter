import math as m

def main():
    time = int(input())
    x, y = [int(i) for i in input().split(':')]
    if y//10>5:
        y=y%10+50
    if time==24:
        if x//10>2:
            x=x%10
        if(x%10>=4) and (x//10>=2):
            x=x-x%10+3

    else:
        if x==0:
            x=1
        elif x//10>1:
            x=x%10
            if x==0:
                x+=10
        elif (x%10>2) and (x//10>=1):
            x=x - x%10 + 1


    if(x<10):
        print('0', end='')

    print(x, ':', sep='', end='')
    if y<10:
        print('0', end='')
    print(y)



main()