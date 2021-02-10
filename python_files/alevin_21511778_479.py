a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

sum_0 = a + b + c
sum_1 = a + b * c
sum_2 = a * (b + c)
sum_3 = a * b * c
sum_4 = (a + b) * c
sum_5 = a * b + c
sum_o = max(sum_0, sum_1, sum_2, sum_3, sum_4, sum_5)
print(sum_o)