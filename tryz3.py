# -*- coding: utf-8 -*-

# z3をインポート
from z3 import *
x, y = Ints('z y')
t = Then(Tactic("solve-eqs"),Tactic('simplify'))
t = Tactic("solve-eqs")
s=t(Not(x)).as_expr()
print(s)
