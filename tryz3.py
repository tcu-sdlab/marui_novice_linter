# -*- coding: utf-8 -*-

# z3をインポート
from z3 import *
x, y = Ints('z y')
t = Then(Tactic("solve-eqs"),Tactic('simplify'))
s=t(x > 10)
print(s)

g  = Goal()
g.add(And(x > 8, x < 10))

t1 = Tactic('simplify')
t2 = Tactic('solve-eqs')
t  = Then(t1, t2)
print (t(g))