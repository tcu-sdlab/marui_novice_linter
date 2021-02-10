#import math
#c = 100000
#print(int(math.log2(c) * c * 2))
def main():
    n = int(input())
    arr = [0] + sorted(list(map(int, input().split())))
    for i in range(int(input())):
        L = 0   
        R = n + 1
        m = int(input())
        while R - L > 1:
            M = (R + L) // 2
            if arr[M] <= m:
                L = M
            else:
                R = M
        print(L)
main()