a, k = list(map(int, input().split()))
c = a # цена одной лопаты
n = k # купюра отличная от 10
i = False
while i == False:
   if (c - n) % 10 == 0:
      print(int(c / a))
      i = True
      break
   if c % 10 == 0:
      print(int(c / a))
      i = True
      break
   else:
      c += a