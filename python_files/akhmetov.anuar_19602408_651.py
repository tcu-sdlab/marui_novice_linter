t = input
p = print
r = range
n = int(t())
a = list(map(int, t().split()))
from collections import Counter
s = Counter(a)
p(n - max(s.values()))