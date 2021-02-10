from collections import defaultdict
import sys, os, math

if __name__ == "__main__":
    #n, m = list(map(int, input().split()))
    #sys.stdout.flush()
    s = input()
    time = input()
    ans = ''
    num = 0
    num += int(time[1])
    num += 10 * int(time[0])
    if s == "12":
        if num >= 1 and num <= 12:
            ans += time[:2]
        else:
            if time[1] == '0':
                ans += "10"
            else:
                ans += ('0' + time[1])
    else:
        if num >= 0 and num <= 23:
            ans += time[:2]
        else:    
            ans += ('0' + time[1])        
    ans += ":"
    if time[3] not in "012345":
        ans += "0"
    else:
        ans += time[3]
    ans += time[4]
    print(ans)