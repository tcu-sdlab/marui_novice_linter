n=int(input())
a = 2*(n//7)
b = n%7
print(a+(b==6),a+min(2,b))