str = input()
for i, ch in enumerate(str):
    ch = int(ch)
    if i == 0 and ch == 9:
        print(9, end='')
    else:
        print(min(ch, 9 - ch),end = '')