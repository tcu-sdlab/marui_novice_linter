a=int(input())
b=list(map(int, input().split()))
b.sort()
#for number in b:
 #   print(number)
print(' '.join(str(q) for q in b))