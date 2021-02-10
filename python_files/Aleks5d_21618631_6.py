from sys import setrecursionlimit
setrecursionlimit(1000000000)

def main():
    stick=[int(i) for i in input().split()]
    stick.sort()
    if stick[-1]<stick[-2]+stick[-3]:
        print("TRIANGLE")
    elif stick[-2]<stick[-3]+stick[-4]:
        print("TRIANGLE")
    elif stick[-1]==stick[-2]+stick[-3]:
        print("SEGMENT")
    elif stick[-2]==stick[-3]+stick[-4]:
        print("SEGMENT")
    else:
        print("IMPOSSIBLE")

main()