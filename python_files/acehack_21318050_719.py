n = int(input())
xs = list(map(int, input().split()))
if xs[-1] == 15:
    print("DOWN")
elif n == 1:
    if xs[0] == 0:
        print("UP")
    else:
        print("-1")
else:
    if xs[-2] < xs[-1]:
        print("UP")
    else:
        if xs[-1] == 0:
            print("UP")
        else:
            print("DOWN")