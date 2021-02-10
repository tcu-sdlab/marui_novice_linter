s = 'I hate '
for i in range(2, int(input()) + 1):
    s += 'that I ' + ('hate ' if i % 2 else 'love ')
print(s + 'it')