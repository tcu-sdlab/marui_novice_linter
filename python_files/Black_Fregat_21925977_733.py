s = input()
ss = list(map(lambda x, y: (x in "AEIOUY", y), s, range(len(s))))
ss = list(filter(lambda x: x[0], ss)) 
ss = list(map(lambda x: x[1], ss)) 
ss0 = [-1]
ss0.extend(ss)
ss.append(len(s))
print(max(map(lambda x, y: x-y, ss, ss0)))