from math import floor
def f(n, m):
    if m == 1:
        return ((n*(n-1))//2, (n*(n-1))//2)
    else:
        mxn = n-m+1
        mx = (mxn*(mxn-1))//2
        rem = floor(n/m)
        y = n - rem*m
        x = m-y
        mn = (x*((rem*(rem-1))/2)) + (y * (rem*(rem+1)/2))
        return (int(mn), mx)

n, m = [int(x) for x in input().strip().split(' ')]
mi, mx = f(n, m)
print("%d %d" % (mi, mx))