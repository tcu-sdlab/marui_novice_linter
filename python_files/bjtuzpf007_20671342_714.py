num = int(input())
multiset = [0] * 2 ** 18
t = str.maketrans('0123456789', '0101010101')

while num:
    opr = input().split()
    if opr[0] == '+':
        multiset[int(opr[1].translate(t), 2)] += 1
    elif opr[0] == '-':
        multiset[int(opr[1].translate(t), 2)] -= 1
    elif opr[0] == '?':
        print(multiset[int(opr[1], 2)])
    num -= 1