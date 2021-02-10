def A():
    num = [int(x) for x in input().split()]
    dist = 999
    for i in range(1, 101):
        dist = min((abs(num[0] - i) + abs(num[1] - i) + abs(num[2] - i)), dist)
    print(dist)

A()