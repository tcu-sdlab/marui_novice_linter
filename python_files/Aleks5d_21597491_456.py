def key(a):
    return a[0]

def main():
    count = int(input())
    arr=[]
    for i in range(count):
        temp=[int(i) for i in input().split()]
        arr.append(temp)
    arr.sort(key=key)
    for i in range(count-1):
        if (arr[i][0]<arr[i+1][0]) and (arr[i][1]>arr[i+1][1]):
            print("Happy Alex")
            return 0
    print("Poor Alex")


main()