(n, k) = map(int, input().split())

result = {}

for i in range(n):
    p = input()
    if not result.get(len(p)):
        result[len(p)] = 1
    else:
        result[len(p)] += 1

password = input()
aim = len(password)
errors = 0
m = 0

for key in sorted(result.keys()):
    if key < aim:
        m += result[key]
        errors += result[key]
        m += (int(errors / k) * 5)
        errors %= k
    else:
        errors += result[key] - 1
        print(m + 1, m + result[key] + (int(errors / k) * 5))
        break