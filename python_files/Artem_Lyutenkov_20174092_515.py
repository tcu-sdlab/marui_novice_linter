a, b, s = map(int, input().split())
print('Yes' if (abs(a) + abs(b)) <= s and (s - abs(a) - abs(b)) % 2 == 0 else 'No')