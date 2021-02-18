import ast
import astor
from z3 import *
import linecache
import csv

pattern5 = 0
pattern6 = 0
pattern2 = 0
pattern1 = 0
lineno_list = []
class FiveSixNodeVisitor(ast.NodeVisitor):
    """
    パターン5,6
    """

    def visit_FunctionDef(self, node):
        """
        自作関数に対するビジター
        """
        pattern_num = 0
        node.body.append("")
        for i in range(len(node.body) - 1):
            if type(node.body[i]) is ast.If and type(node.body[i].body[0]) is ast.Return \
            and node.body[i].body[0].value is not None and 'value' in vars(node.body[i].body[0].value):
                if type(node.body[i].body[0].value.value) is bool \
                and node.body[i].body[0].value.value:
                    linenum = -1

                    if  type(node.body[i + 1]) is ast.Return \
                    and 'value' in vars(node.body[i + 1].value):
                        if type(node.body[i + 1].value.value) is bool \
                        and not node.body[i + 1].value.value:
                            linenum = node.body[i + 1].lineno
                    elif node.body[i].orelse:
                        if type(node.body[i].orelse[0]) is ast.Return \
                        and 'value' in vars(node.body[i].orelse[0].value):
                            if type(node.body[i].orelse[0].value.value) is bool and not node.body[i].orelse[0].value.value:
                                linenum = node.body[i].orelse[0].lineno
                    if linenum != -1:
                        source = astor.to_source(node.body[i].test).replace("\n","")

                        if type(node.body[i].test) is ast.Compare or type(node.body[i].test) is ast.BoolOp:
                            pattern_num = 5
                            global pattern5
                            pattern5 = pattern5 + 1
                            source = source.rstrip(")").lstrip("(")
                            
                        elif type(node.body[i].test) is ast.Call:
                            pattern_num = 6
                            global pattern6
                            pattern6 = pattern6 + 1
                        else:
                            pattern_num = "undefined"
                        global lineno_list
                        lineno_list.append(node.body[i].lineno)
                        lineno_list.append(linenum)
                        print("line {0} ~ {1}: {2} returns Boolean,so you may not need if-statement.(pattern-{3})".format(node.body[i].lineno, linenum, source, pattern_num))
                        print("I suggest this code should be written")
                        print("     return " + source)

        del(node.body[-1])
        return node
class TwoNodeVisitor(ast.NodeVisitor):
    except_list = []
    elif_check = 0
    def visit_If(self, node):

        if node not in self.except_list and node.orelse == []:

            conditions, lineno = self.search_childIf(node)
            if conditions:
                if len(conditions) > 1:
                    global lineno_list
                    lineno_list.append(node.lineno)
                    lineno_list.append(lineno)
                    global pattern2
                    pattern2 = pattern2 + 1
                    print("line {0} ~ {1} :These conjoining conditions{2} using nested if statements can be simplified by using and operator.(pattern-2)"\
                        .format(node.lineno, lineno, conditions))
                    print("I suggest this code should be written")
                    if self.elif_check == 1:
                        sentence = "     elif "
                    else:
                        sentence = "     if "
                    i = 0
                    count = 1
                    for i in range(len(conditions) - 1):

                        sentence = sentence + conditions[i]
                        if len(sentence) > 80 * count:
                            sentence = sentence + " \\\n     and "
                            count = count + 1
                        else:
                            sentence = sentence + " and "
                    sentence = sentence + conditions[i + 1] + ":"
                    print (sentence)
                self.elif_check = 0
                conditions.clear()
        if node.orelse:
            self.elif_check = 1
            self.visit(node.orelse[0])
            self.elif_check = 0
        self.generic_visit(node)
        return node
    def search_childIf(self, node, conditions_sub = []):
        condition = astor.to_source(node.test).replace("\n","")
        if type(node.test) is ast.Compare:
            condition = condition.rstrip(")").lstrip("(")
        conditions_sub.append(condition)

        if type(node.body[0]) is ast.If and not node.body[0].orelse and len(node.body) == 1:
            self.except_list.append(node)
            return self.search_childIf(node.body[0], conditions_sub)
        else:
            return conditions_sub, node.lineno
def AST_Reader(ast_code):

    count = 0
    strdata = str(ast.dump(ast_code))
    clist = list(strdata)
    mode = 0
    for i in clist:
        if mode == 1:
            mode = 0
            if i == ')' or i == ']':
                print(i,end='')
            else:
                count = count + 1
                print()
                for _ in range(count):
                    print("   ",end='')
                print(i,end='')
        else:
            if i == '(' or i == '[':
                mode = 1
                print(i,end='')
            elif i == ')' or i == ']':
                count = count - 1
                print()
                for _ in range(count):
                    print("   ",end='')
                print(i,end='')
            elif i == ',':
                print(i)
                print("  ",end='')
                for _ in range(count - 1):
                    print("   ",end='')

            else:

                print(i,end='')
    print()
# def search_if(node):
class OneNodeSearcher():
    is_continuous = False # 連続していることを判定する
    # node: 現在のノード,count: ifの位置関係を確認するための変数, previous: 前までに検出された条件式を格納する辞書型変数, conditions:
    def one_search(self, node, count = 1, count_two = 0, previous = {}, conditions = None, lineno = None):
        if lineno is None:
            lineno = []
        if conditions is None:
            conditions = []
        if type(node) is ast.If: # まず起点となるif文を探す
            # キー"count - 1"の要素がpreviousにあるとき，つまりこのifの直前にifがある場合
            if count - 1 in previous:
                # previous[count - 1]がconditionsの中にないとき（条件の重複を防ぐため）
                if previous[count - 1] not in conditions and previous[str(count - 1)] == count_two:

                    # そのprevious[count - 1]を末尾に追加
                    conditions.append(previous.pop(count - 1))
                    rainn = previous.pop(1 - count)
                    lineno.append(rainn)
                # conditionsの末尾に現在のcountの条件文を追加
                if not node.orelse:
                    conditions.append(node.test)
                    lineno.append(node.lineno)

                    # 連続していることを判定する
                    self.is_continuous = True
            else:
                self.process_when_exiting_if(conditions, lineno)
                conditions = []
                lineno = []

            # previousにキーをcountとした条件文のリストを登録することによって一時的に記憶
            previous[count] = node.test
            previous[-count] = node.lineno
            previous[str(count)] = count_two
        else:
            self.process_when_exiting_if(conditions, lineno)
            conditions = []
            lineno = []
        cnt = 0
        for child in ast.iter_child_nodes(node):
            # 子ノードに対して再帰する
            cnt = cnt + 1
            count_two = count_two + 1
            self.one_search(child, cnt, count_two, previous, conditions, lineno)

    def process_when_exiting_if(self, conditions, lineno):
        # ifのカウントから抜けたとき
        if self.is_continuous:
            # 以下連続が切れた時から判定処理を行う

            # z3処理結果格納用の変数定義
            z3var = {}
            z3_list = []

            # 条件式ごとに処理をする
            for i in conditions:
                # 条件式に含まれる変数をz3用にフォーマット
                var_list = self.search_variable_name(i)
                for j in range(len(var_list)):
                    z3var[var_list[j]] = Int(var_list[j])

                # z3を用いて条件文の具体的な表現を解析し，リストに格納する
                result, eq_flag = self.expr_investigate(i, z3var)
                if type(result) is list:
                    result = list(set(result))
                z3_list.append(result)
                z3var = {}
            # 解析結果から冗長なコードの条件に当てはまるか調べる
            self.conditions_analyze(z3_list, lineno, eq_flag)

            self.is_continuous = False

    def conditions_analyze(self, condition_list, lineno, eq_flag):
        """
        解析結果から冗長なコードの条件に当てはまるか調べる
        """
        if len(condition_list) != 1:
            if eq_flag:
                t = Tactic("simplify")
            else:
                t = Then(Tactic("solve-eqs"),Tactic('simplify'))
            while len(condition_list) != 1:
                tmp = condition_list.pop(0)
                if type(tmp) is list:
                    for i in range(len(tmp)):
                        tmp[i] = t(Not(tmp[i])).as_expr()
                    g = tmp
                else:
                    g = t(Not(self.conditions_integrate(tmp))).as_expr()
                result = []
                global lineno_list
                global pattern1
                for i in condition_list:
                    if type(g) is list:
                        for k in g:
                            if type(i) is list:
                                tmp = self.list_analyze(i, k)
                                if tmp != None:
                                    if not tmp in result:
                                        result.append(tmp)
                                        pattern1 = pattern1 + 1
                                        lineno_list.append(lineno[0])
                                        lineno_list.append(lineno[-1])
                                        print("line:{0} ~ line:{1}, condition \"{2}\" may be simplified by elif-statement".format(lineno[0], lineno[-1], result))
                    else:
                        if type(i) is list:
                            tmp = self.list_analyze(i, g)
                            if tmp != None:
                                if not tmp in result:
                                    result.append(tmp)
                                    pattern1 = pattern1 + 1
                                    lineno_list.append(lineno[0])
                                    lineno_list.append(lineno[-1])
                                    print("line:{0} ~ line:{1}, condition \"{2}\" may be simplified by elif-statement".format(lineno[0], lineno[-1], result))


    def conditions_integrate(self, conditions, g = True):
        """
        docstring
        """
        if type(conditions) is list:
            for i in conditions:
                g = self.conditions_integrate(i, g)
            return g
        else:
            return And(g, conditions)
    def list_analyze(self, i, g):
        for j in i:
            if type(j) is list:
                self.list_analyze(j, g)
            else:
                if j == g:
                    return j

    def search_variable_name(self, node, variables = None):
        if variables is None:
            variables = []
        """
        プログラム内で使われている変数の名前を検索する関数
        """
        if type(node) is ast.BoolOp:
            temporary = []
            for i in node.values:
                tem = self.search_variable_name(i, temporary)
                temporary = temporary + tem
            return temporary
        elif type(node) is ast.Compare:
            tmp1_list = self.search_variable_name(node.left, variables)
            for j in node.comparators:
                tmp1_list.extend(self.search_variable_name(j, variables))
            return tmp1_list
        elif type(node) is ast.BinOp:
            return variables + self.search_variable_name(node.left) + self.search_variable_name(node.right)
        elif type(node) is ast.Name :
            tmp_list = []
            if node.id not in variables:
                tmp_list = variables + [node.id]
            return tmp_list
        elif type(node) is ast.UnaryOp:
            return self.search_variable_name(node.operand, variables)
        elif type(node) is ast.Constant or type(node) is ast.Call:
            return []
        elif type(node) is ast.Subscript or type(node) is ast.List or type(node) is ast.Subscript or type(node) is ast.Tuple or type(node) is ast.Attribute or type(node) is ast.Set:
            return variables
        else:
            print(astor.to_source(node))
            print(node)
            print("unknown class = {}".format(vars(node)))
            return variables
    def expr_investigate(self, i, z3var):

        """
        どのような条件かによって処理する
        """
        # z3用の変数定義
        g  = Goal()
        # 演算子を用いている場合
        if type(i) is ast.Compare:
            op = type(i.ops[0])
            left = self.bin_analyze(z3var, i.left)
            right = self.bin_analyze(z3var, i.comparators[0])
            if type(left) is ast.Subscript or type(left) is ast.Call or type(right) is ast.Subscript or type(right) is ast.Call  \
            or type(right) is str or type(left) is str or type(right) is ast.List or type(left) is ast.List or type(left) is ast.Attribute or type(right) is ast.Attribute:
                return False, False
            else:
                if op is ast.Gt:
                    if type(left) is not z3.z3.ArithRef:
                        g.add(right.__lt__(left))
                    else:
                        g.add(left.__gt__(right))
                    g.add(left.__gt__(right))
                elif op is ast.LtE:
                    if type(left) is not z3.z3.ArithRef:
                        g.add(Not(right.__lt__(left)))
                    else:
                        g.add(Not(left.__gt__(right)))
                elif op is ast.Eq:
                    if type(left) is not z3.z3.ArithRef:
                        g.add(right.__eq__(left))
                    else:
                        g.add(left.__eq__(right))
                elif op is ast.Lt:
                    g.add(left.__lt__(right))
                if not g:
                    return [], False
                return g[0], False

        elif type(i) is ast.BoolOp:
            conditions, bool_list, eq_flag = self.bool_analyze(i, z3var)
            if eq_flag:
                t = Tactic("simplify")
            else:
                t = Then(Tactic("solve-eqs"),Tactic('simplify'))
            if len(conditions) > 1:
                if type(conditions[0]) is z3.z3.ArithRef or type(conditions[1]) is z3.z3.ArithRef or type(conditions[0]) is ast.Subscript or type(conditions[1]) is ast.Subscript:
                    return False, False
                if str(And(conditions[0], conditions[1])).startswith("And"):
                    result = []
                    for k in conditions:
                        if k == False:
                            result.append(k)
                        else:
                            result.append(t(k).as_expr())
                    return result, eq_flag
                else:
                    return t(And(conditions[0], conditions[1])).as_expr(), eq_flag
            return conditions, eq_flag
        else:
            return False, False

    def bin_analyze(self, z3var, node):
        if type(node) is ast.BinOp:
            if type(node.left) is ast.BinOp or type(node.left) is ast.Compare or type(node.left) is ast.UnaryOp:
                left_value = self.bin_analyze(z3var, node.left)
            elif type(node.left) is ast.Name:
                left_value = z3var[node.left.id]
            elif type(node.left) is ast.Constant:
                left_value = node.left.value
            else:
                return node.left
            if type(node.right) is ast.BinOp:
                right_value = self.bin_analyze(z3var, node.right)
            elif type(node.right) is ast.Name:
                right_value = z3var[node.right.id]
            elif type(node.right) is ast.Constant:
                right_value = node.right.value
            elif type(node.right) is ast.Compare:
                right_value = self.bin_analyze(z3var, node.right)
            else:
                return node.right
            if type(left_value) is ast.Call or type(right_value) is ast.Call or type(left_value) is ast.Subscript or type(right_value) is ast.Subscript:
                return False
            else:
                if type(node.op) is ast.Sub:
                    return left_value - right_value
                elif type(node.op) is ast.Mod:
                    return left_value % right_value
                elif type(node.op) is ast.Mult:
                    return left_value * right_value
                elif type(node.op) is ast.Add:
                    return left_value + right_value
                elif type(node.op) is ast.LShift or type(node.op) is ast.BitAnd or type(node.op) is ast.FloorDiv:
                    return False
                elif type(node.op) is ast.Pow:
                    return left_value * left_value
                elif type(node.op) is ast.Div:
                    return left_value / right_value
                else:
                    print(node.op)
        elif type(node) is ast.Name:
            return z3var[node.id]
        elif type(node) is ast.Constant:
            return node.value
        elif type(node) is ast.UnaryOp:
            if type(node.op) is ast.USub:
                operand = self.bin_analyze(z3var, node.operand)
                if type(operand) is ast.Call:
                    return False
                return -operand
        elif type(node) is ast.BoolOp:
            conditions, bool_list, eq_flag = self.bool_analyze(node, z3var)
            return conditions[0]
        else:
            return node
    def bool_analyze(self, i, z3var, bool_list = [], conditions = None, eq_flag = False):
        """
        docstring
        """
        if conditions is None:
            conditions = []
        boolean = type(i.op)
        if boolean is ast.And:
            # ANDのとき
            # andであることをリストに記憶しておく
            bool_list.append(i.op)
            for k in i.values:
    
                if type(k) is ast.Compare:
                    # 演算子を用いている場合
                    op = type(k.ops[0])
                    left = self.bin_analyze(z3var, k.left)
                    right = self.bin_analyze(z3var, k.comparators[0])
                    if type(left) is ast.Subscript or type(left) is ast.Call or type(right) is ast.Subscript or type(right) is ast.Call  or type(right) is str or left == False or right == False:
                        conditions.append(False)
                    else:
                        if type(left) is not z3.z3.ArithRef:
                            tmp = left
                            left = right
                            right = tmp
                        if op is ast.Gt:
                            conditions.append((left).__gt__(right))
                        elif op is ast.Lt:
                            conditions.append((left).__lt__(right))
                        elif op is ast.LtE:
                            if type(left) is int:
                                final = right.__lt__(left)
                            else:
                                final = (left).__gt__(right)
                            conditions.append(Not(final))
                        elif op is ast.GtE:
                            conditions.append(Not((left).__lt__(right)))
                        elif op is ast.Eq:
                            eq_flag = True
                            conditions.append((left).__eq__(right))
                        elif op is ast.NotEq:
                            conditions.append(Not((left).__eq__(right)))
                elif type(k) is ast.BoolOp:
                    conditions, bool_list, eq_flag = self.bool_analyze(k, z3var, bool_list, conditions)
                elif type(k) is ast.UnaryOp:
                    # conditions, bool_list, eq_flag = self.bool_analyze(k, z3var, bool_list, conditions)
                    eq_flag = self.eq_exists(k)
                    print(self.bin_analyze(z3var, k.operand))
                    conditions.append(self.bin_analyze(z3var, k.operand))
                    if type(conditions[0]) is z3.z3.ArithRef or type(conditions[0]) is ast.Subscript:
                        conditions.append(False)
                    else:
                        if eq_flag:
                            t = Tactic("simplify")
                        else:
                            t = Then(Tactic("solve-eqs"),Tactic('simplify'))
                        conditions.append(t(Not(conditions[0])).as_expr())
        elif boolean is ast.Or:
            bool_list.append(i.op)
            for k in i.values:
                if type(k) is ast.Compare:
                    # 演算子を用いている場合
                    op = type(k.ops[0])
                    left = self.bin_analyze(z3var, k.left)
                    right = self.bin_analyze(z3var, k.comparators[0])
                    if type(left) is ast.Subscript or type(left) is ast.Call or type(right) is ast.Subscript or type(right) is ast.Call  or type(right) is str or type(left) is str or left == False:
                        conditions.append(False)
                    else:
                        if op is ast.Gt:
                            conditions.append((left).__gt__(right))
                        elif op is ast.Lt:
                            conditions.append((left).__lt__(right))
                        elif op is ast.LtE:
                            conditions.append(Not((left).__gt__(right)))
                        elif op is ast.GtE:
                            conditions.append(Not((left).__lt__(right)))
                        elif op is ast.Eq:
                            eq_flag = True
                            conditions.append((left).__eq__(right))
                        elif op is ast.NotEq:
                            conditions.append(Not(left.__eq__(right)))
                elif type(k) is ast.UnaryOp:
                    # conditions, bool_list, eq_flag = self.bool_analyze(k, z3var, bool_list, conditions)
                    eq_flag = self.eq_exists(k)
                    tmp = self.bin_analyze(z3var, k.operand)
                    if type(tmp) is z3.z3.ArithRef or type(k.operand) is ast.Call:
                        conditions.append(False)
                    else:
                        conditions.append(tmp)
                        if eq_flag:
                            t = Tactic("simplify")
                        else:
                            t = Then(Tactic("solve-eqs"),Tactic('simplify'))
                        if type(k.op) is ast.Not:
                            conditions.append(t(Not(conditions[0])).as_expr())
                elif type(k) is ast.BoolOp:
                    conditions, bool_list, eq_flag = self.bool_analyze(k, z3var, bool_list, conditions, eq_flag)
                elif type(k) is ast.Call:
                    conditions.append(False)
                elif type(k) is ast.Name:
                    conditions.append(z3var[k.id])
            if eq_flag:
                t = Tactic("simplify")
            else:
                t = Then(Tactic("solve-eqs"),Tactic('simplify'))
            if type(conditions[1]) is z3.z3.ArithRef or type(conditions[0]) is z3.z3.ArithRef:
                conditions[0] = False
            else:
                conditions[0] = t(Not(And(Not(conditions[0]), Not(conditions[1])))).as_expr()
            conditions.pop(1)
        return conditions, bool_list, eq_flag
    def eq_exists(self, node):
        thing = type(node)
        if thing is ast.Eq:
            return True
        elif thing is ast.Name or thing is ast.Not or thing is ast.Subscript or thing is ast.Call or thing is ast.BoolOp:
            return False
        elif thing is ast.UnaryOp:
            return self.eq_exists(node.op) or self.eq_exists(node.operand)
        else:
            print("error:" + str(thing), file=sys.stderr)
        return False
def main():
    """
    main
    """
    # file_path = r'c:\Users\maru\Documents\Github\marui_novice_linter\tryz3.py'
    file_names_file = r'c:\Users\maru\Documents\Github\marui_novice_linter\file_names.txt'
    py_names = open("./file_names.csv", "r", encoding="ms932", errors="", newline="")
    # file_path = r'c:\Users\maru\Documents\Github\marui_novice_linter\pydat copy.py'
    f = csv.reader(py_names, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    error_count = 0
    with open("result.txt", "w") as result:
        result.close()
    count = 0
    # for py_file in f:
    #     count = count + 1
    py_file = ["pydat.py"]
    if py_file[0] != "filename":
        file_path = "./" + py_file[0]
        with open(file_path, 'r', encoding="utf-8_sig") as sourse_file:
            source = sourse_file.read()
            tree = ast.parse(source, file_path)
            # AST_Reader(tree)
            # try:
            global lineno_list
            with open("result.txt", "a") as result:
                FiveSixNodeVisitor().visit(tree)
                while len(lineno_list) != 0:
                    result.write(file_path + "\n\n")
                    result.write("pattern-5\n")
                    # pop してwrite
                    result.write(py_file[0])
                    result.write("\n")
                    a = lineno_list.pop(0)
                    b = lineno_list.pop(0) + 1
                    for i in range(a, b):
                        result.write(linecache.getline(file_path, i))
                    result.write("\n")
                TwoNodeVisitor().visit(tree)
                while len(lineno_list) != 0:
                    result.write(file_path + "\n\n")
                    result.write("pattern-2\n")
                    # pop してwrite
                    result.write(py_file[0])
                    result.write("\n")
                    a = lineno_list.pop(0)
                    b = lineno_list.pop(0) + 1
                    for i in range(a, b):
                        result.write(linecache.getline(file_path, i))
                    result.write("\n")
                OneNodeSearcher().one_search(tree)
                while len(lineno_list) != 0:
                    result.write("pattern-1\n")
                    # pop してwrite
                    result.write(py_file[0])
                    result.write("\n")
                    a = lineno_list.pop(0)
                    b = lineno_list.pop(0) + 1
                    for i in range(a, b):
                        result.write(linecache.getline(file_path, i))
                    result.write("\n")
                # break
            # except:
            #     error_count = error_count + 1
    # print(error_count)
    global pattern2
    global pattern5
    global pattern6
    global pattern1
    print(count)
    print(pattern5)
    print(pattern6)
    print(pattern2)
    print(pattern1)
if __name__ == '__main__':
    main()
