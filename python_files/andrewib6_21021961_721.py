num = int(input())
row = [str(in_str) for in_str in input()]

count = 0
length_B = None
len_array = []
prev = 'W'
for i in range(len(row)):
    current = row[i]
    if prev == 'W' and current == 'B' :

        count +=1
        length_B = 1
    elif prev == 'B' and current == 'B':
        length_B += 1

    elif prev == 'B' and current == 'W':
        len_array.append(length_B)
    prev = current

current = 'W'
if prev == 'B' and current == 'W':
    len_array.append(length_B)


print(count)
string = ''
for i in range(len(len_array)):
    string += str(len_array[i])
    if i < len(len_array) - 1:
        string += ' '


print(string)