n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
data = list(map(lambda x: x[0]-x[1], data))
order = [sum(data)]
order.extend(map(lambda x: order[0]-2*x, data))
print(order.index(max(order, key=abs)))