import sys

n, k = map(int, sys.stdin.readline().split(" "))

count = [0] * 101

for i in range(n):
    count[len(sys.stdin.readline().strip())] += 1

password_length = len(sys.stdin.readline().strip())

before_length = 0
for i in range(password_length):
    before_length += count[i]

min_passwords = before_length + 1
max_passwords = before_length + count[password_length]


print(str(min_passwords + (((min_passwords - 1) // k) * 5)) + " " + str(max_passwords + (((max_passwords - 1) // k) * 5)))