s = input().split(" ")
a = int(s[0])
b = int(s[1])
arr = []
def foo(i):
    if i > b:
        return False
    if i == b:
        arr.append(i)
        return True
    ai = foo(i * 2)
    bi = foo(i * 10 + 1)
    if ai:
        arr.append(i)
        return True
    if bi:
        arr.append(i)
        return True
if foo(a):
    print("YES")
    print(len(arr))
    for i in range(0,len(arr)):
        print(arr[len(arr) - i - 1], end=' ')
else:
    print("NO")