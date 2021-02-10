for i in range(int(input())):
    w = input()
    if len(w) <= 10:
        print(w)
    else:
        print(w[0] + str(len(w) - 2) + w[-1])