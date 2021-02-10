s = input()
check_lst = [0] * 26
str_len = len(s)


def test():
    for c in check_lst:
        if c > 1:
            return 0
    return 1


def print_str(start):
    target_str = ''
    lost_str = ''
    lost_index = 0
    for c in range(26):
        if not check_lst[c]:
            lost_str += chr(65 + c)
    for i in s[start:start + 26]:
        if i != '?':
            target_str += i
        else:
            target_str += lost_str[lost_index]
            lost_index += 1
    return s[:start].replace('?', 'A') + target_str + s[start + 26:].replace('?', 'A')


def check():
    for i in range(26):
        if s[i] != '?':
            check_lst[ord(s[i]) - 65] += 1
    if test():
        return print_str(0)
    else:
        start = 0
        while start < str_len - 26:
            if s[start] != '?':
                check_lst[ord(s[start]) - 65] -= 1
            if s[start + 26] != '?':
                check_lst[ord(s[start + 26]) - 65] += 1
            if not test():
                start += 1
            else:
                return print_str(start + 1)
        return -1


if len(s) < 26:
    print(-1)
else:
    print(check())