ara=list(map(int, input().split()))
ara.sort()
if ara[0]+ara[1]>ara[2] or ara[1]+ara[2]>ara[3]:
    print("TRIANGLE")
elif ara[0]+ara[1]==ara[2] or ara[1]+ara[2]==ara[3]:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")