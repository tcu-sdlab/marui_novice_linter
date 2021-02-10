commands = input()
if len(commands) % 2 != 0:
    print(-1)
else:
    left_right = 0
    top_bot = 0
    for i in commands:
        if i == "R":
            left_right += 1
        elif i == "L":
            left_right -= 1
        elif i == "U":
            top_bot += 1
        elif i == "D":
            top_bot -= 1
    print((abs(top_bot) + abs(left_right))// 2)