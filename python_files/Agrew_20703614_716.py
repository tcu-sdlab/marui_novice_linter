n = int(input())
start = 2
level = 1
while (level<=n):
    target = level*level*(level+1)*(level+1)
    print ((target-start)//level)
    start = level*(level+1)
    level = level + 1