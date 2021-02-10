n = int(input())
ans = [len(x) for x in input().split('W') if len(x)]
print(len(ans))
print(*ans)