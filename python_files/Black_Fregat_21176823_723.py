def flatt(z):
  return [x for y in z for x in y]

n = int(input())
s = input()
ss = flatt(map(lambda x: x.split(")"), s.split("(")))

s_in = flatt(map(lambda x: x.split("_"), ss[1::2]))
s_out = flatt(map(lambda x: x.split("_"), ss[0::2]))

n1 = max(map(len, s_out))
n2 = sum(map(lambda x: x != "", s_in))

print(n1, end = " ")
print(n2)