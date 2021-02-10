n = int(input())
s = list(input())

order = "rb"
data0 = sum(map(lambda x, y: order.index(x) == 0 and y % 2 == 0 , s, range(n)))
data1 = sum(map(lambda x, y: order.index(x) == 1 and y % 2 == 1 , s, range(n)))
count1 = max(data0, data1) 

order = "br"
data0 = sum(map(lambda x, y: order.index(x) == 0 and y % 2 == 0 , s, range(n)))
data1 = sum(map(lambda x, y: order.index(x) == 1 and y % 2 == 1 , s, range(n)))
count2 = max(data0, data1) 
   
print(min(count1, count2))