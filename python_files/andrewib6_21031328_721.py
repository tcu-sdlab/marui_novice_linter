[num_passwords, num_tries] = [int(item) for item in input().split()]
passwords = []
for _ in range(num_passwords):
    passwords.append(len(input()))
password_len = len(input())

passwords.sort()

min = 0
max = len(passwords)
count = 0
time = 0

for i in range(len(passwords)):
    time +=1
    if passwords[i] == password_len:
        if min == 0:
            min = time
        if i < len(passwords)-1:
            if passwords[i+1] != password_len:
                max = time
                break
        else:
            max = time
    count +=1
    if count == num_tries:
        time +=5
        count =0

print(min, max)