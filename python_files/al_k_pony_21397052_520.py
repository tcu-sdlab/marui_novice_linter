import string
input()
print('NO'if(set(string.ascii_lowercase)-set(input().lower()))else'YES')