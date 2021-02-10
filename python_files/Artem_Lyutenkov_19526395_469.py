n = int(input())
print('I become the guy.' if len(set(input().split()[1:] + input().split()[1:])) == n else 'Oh, my keyboard!')