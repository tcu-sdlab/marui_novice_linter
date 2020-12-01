import ast
import astor
from z3 import *

class OneNodeSearcher():
    mode = False # モード
    # node: 現在のノード,count: ifの位置関係を確認するための変数, previous: , conditions:
    def one_search(self, node, count = 0, previous = {}, conditions = []):
        if type(node) is ast.If: # まず起点となるif文を探す
            if count - 1 in previous:
                if previous[count - 1] not in conditions:
                    conditions.append(previous[count - 1])
                conditions.append(node.test)
                self.mode = True
            else:
                if self.mode:
                    self.mode = False
                conditions = []
            previous[count] = node.test
        else:
            # ifのカウントから抜けたとき
            if self.mode:
                # z3用の変数定義
                t = Then(Tactic("solve-eqs"),Tactic('simplify'))
                z3var = {}
                # 条件式のz3処理
                z3_list = []
                for i in conditions:
                    # 条件式に含まれる変数をz3用にフォーマット
                    self.test_var_search(i)
                    for j in self.valiables:
                        z3var[j] = Int(j)
                    # 条件式ごとに処理をする
                    g  = Goal()
                    z3_list.append(self.expr_investigate(i, g, t, z3var))
                    print(vars(i))
                    z3var = {}
                print(z3_list)
                self.mode = False
            conditions = []
        cnt = 0
        for child in ast.iter_child_nodes(node):
            cnt = cnt + 1
            self.one_search(child, cnt, previous, conditions)
    valiables = []

    def test_var_search(self, node):
        if type(node) is ast.BoolOp:
            for i in node.values:
                self.test_var_search(i)
        elif type(node) is ast.Compare:
            self.test_var_search(node.left)
            for j in node.comparators:
                self.test_var_search(j)
        elif type(node) is ast.BinOp:
            self.test_var_search(node.left)
            self.test_var_search(node.right)
        elif type(node) is ast.Name :
            if node.id not in self.valiables:
                self.valiables.append(node.id)
        elif type(node) is ast.Constant:
            pass
        else:
            print("unknown class")

    def expr_investigate(self, i, g, t, z3var):
        """
        どのような条件かによって処理する
        """
        if type(i) is ast.Compare:
            # 演算子を用いている場合
            op = type(i.ops[0])
            print(op)
            if op is ast.Gt:
                g.add(z3var[i.left.id].__gt__(i.comparators[0].value))
                print(t(g).as_expr())
            elif op is ast.LtE:
                g.add(Not(z3var[i.left.id].__lt__(i.comparators[0].value)))
                print(t(g).as_expr())
            return t(g).as_expr()

        elif type(i) is ast.BoolOp:
            conditions = []
            bool_list = []
            if type(i.op) is ast.And:
                bool_list.append()
                for k in i.values:
                    if type(k) is ast.Compare:
                        # 演算子を用いている場合
                        op = type(k.ops[0])
                        print(op)
                        if op is ast.Gt:
                            conditions.append(z3var[k.left.id].__gt__(k.comparators[0].value))
                        elif op is ast.LtE:
                            conditions.append(Not(z3var[k.left.id].__lt__(k.comparators[0].value)))
                    elif type(k) is ast.BoolOp:
                        bool_list.append(k)
                        # 繰り返し
                g.add(And(conditions[0], conditions[1]))
                print(t(g).as_expr())
            return 0

def main():
    """
    main
    """
    # file_name = r'c:\Users\maru\Documents\Github\marui_novice_linter\tryz3.py'
    file_name = r'c:\Users\maru\Documents\Github\marui_novice_linter\pydat.py'
    with open(file_name, 'r', encoding="utf-8_sig") as sourse_file:
        source = sourse_file.read()

    tree = ast.parse(source, file_name)

    # FiveSixNodeVisitor().visit(tree)
    # TwoNodeVisitor().visit(tree)
    OneNodeSearcher().one_search(tree)
if __name__ == '__main__':
    main()