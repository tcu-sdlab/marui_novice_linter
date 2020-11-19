# -*- coding: utf-8 -*-

# z3をインポート
from z3 import *
x, y = Ints('x y')
t = Then(Tactic("solve-eqs"),Tactic('ctx-solver-simplify'))
s=t(And(x * 2 == 4,y > x))
print(s)

x, y = Reals('x y')
g  = Goal()
g.add(x > 0, y > 0, x == y + 2)
print(g)

print(type(x))
t1 = Tactic('simplify')
t2 = Tactic('solve-eqs')
t  = Then(t1, t2)
print (t(g))