# -*- coding: utf-8 -*-

# z3をインポート
from z3 import *
x, y = Ints('z y')
t = Then(Tactic("solve-eqs"),Tactic('simplify'))
s=t(x > 10)
print(s)

g  = Goal()
g.add(x > 10)
g.add(x < 8)

t1 = Tactic('simplify')
t2 = Tactic('solve-eqs')
t  = Then(t1, t2)
print (t(g).as_expr())