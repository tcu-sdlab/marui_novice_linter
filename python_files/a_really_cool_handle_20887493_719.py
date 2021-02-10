n = int(input())
days = [int(x) for x in input().split()]

if days[-1] == 15:
    print ("DOWN")
elif days[-1] == 0:
    print ("UP")
elif n == 1:
    print (-1)
elif days[-2] > days[-1]:
    print ("DOWN")
else:
    print ("UP")