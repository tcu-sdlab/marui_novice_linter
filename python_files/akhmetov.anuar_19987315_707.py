t = input
p = print
r = range
n, m = map(int, t().split())
ans = "#Black&White"
colors = 'CMY'
for i in r(n):

    s = t().split()
    for j in s:
        if j in colors:
            ans = "#Color"
            p(ans)
            exit()
p(ans)