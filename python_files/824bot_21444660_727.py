import sys
sys.setrecursionlimit(10**9)
a, b = map(int, input().split())
temp = a
f = False
res = []
def rec(n):
    global f
    global res
    if n == b:
        res.append(n)
        f = True
        return True
    else:
        if n*2 <= b:
            if rec(n*2) == True:
                res.append(n)
                return True
            elif rec(n*10 + 1) == True:
                res.append(n)
                return True


rec(a)
if f:
    print("YES")
    print(len(res))
    print(" ".join(map(str,res[::-1])))
else:
    print("NO")