n = input()
obsv = [int(x) for x in input().split()]
if obsv[-1] == 15:
    print("DOWN")
elif obsv[-1] == 0:
    print("UP")
elif n == "1":
    print(-1)
elif obsv[-1] > obsv[-2]:
    print("UP")
else:
    print("DOWN")