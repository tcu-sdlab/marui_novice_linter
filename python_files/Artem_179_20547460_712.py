x, y = map(int, input().split())
per = 0 if x !=y else 3
ans = 0
per1 = y
per2 = y
per3 = y
while per < 3:
    if per1 <= per2 and per1 <= per3:
        if per3 + per2 - 1 >= x:
            per += 1
            per1 = x
        else:
            per1 = per3 + per2 - 1
    elif per2 <= per1 and per2 <= per3:
        if per3 + per1 - 1 >= x:
            per += 1
            per2 = x
        else:
            per2 = per3 + per1 - 1    
    elif per3 <= per2 and per3 <= per1:
        if per1 + per2 - 1 >= x:
            per += 1
            per3 = x
        else:
            per3 = per1 + per2 - 1    
    ans += 1
print(ans)