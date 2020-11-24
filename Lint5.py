import ast
import astor
from z3 import *
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
            and 'value' in vars(node.body[i].body[0].value):
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
                            source = source.rstrip(")").lstrip("(")
                        elif type(node.body[i].test) is ast.Call:
                            pattern_num = 6
                        else:
                            pattern_num = "undefined"

                        print("line {0} ~ {1}: {2} returns Boolean,so you may not need if-statement.(pattern-{3})".format(node.body[i].lineno, linenum, source, pattern_num))
                        print("I suggest this code should be written")
                        print("     return " + source)

        del(node.body[-1])
        return node
class TwoNodeVisitor(ast.NodeVisitor):
    except_list = []
    elif_check = 0
    def visit_If(self, node):

        if node not in self.except_list:

            conditions, lineno = self.search_childIf(node)
            if conditions:
                if len(conditions) > 1:
                    print("line {0} ~ {1} :These conjoining conditions{2} using nested if statements can be simplified by using and operator.(pattern-2)"\
                        .format(node.lineno, lineno, conditions))
                    print("I suggest this code should be written")
                    if self.elif_check == 1:
                        sentence = "     elif "
                        # print("     elif ", end = "")
                    else:
                        sentence = "     if "
                        # print("     if ", end = "")
                    i = 0
                    count = 1
                    for i in range(len(conditions) - 1):

                        sentence = sentence + conditions[i]
                        if len(sentence) > 80 * count:
                            sentence = sentence + " \\\n     and "
                            count = count + 1
                        else:
                            sentence = sentence + " and "
                        # print(conditions[i],end = "")
                        # print(" and ",end = "")
                    sentence = sentence + conditions[i + 1] + ":"
                    # print(conditions[i + 1],end = "")
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
class OneNodeVisitor(ast.NodeVisitor):
    convert_list = {ast.Eq: ast.NotEq, ast.NotEq: ast.Eq}
    def visit_If(self, node):
        """
        docstring
        """
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
    mode = 0
    def one_search(self, node, count = 0, previous = {}, conditions = []):
        if type(node) is ast.If:
            if count - 1 in previous:
                if previous[count - 1] not in conditions:
                    conditions.append(previous[count - 1])
                conditions.append(node.test)
                self.mode = 1
            else:
                if self.mode:
                    print(conditions)
                    self.mode = 0
                conditions = []
            previous[count] = node.test
            print(vars(node))
            print("count = {}".format(count))
        else:
            if self.mode:
                print(conditions)

                for i in conditions:
                    self.test_val_search(i)
                print("val ={}".format(self.valiables))
                previous = []
                for i in conditions:
                    self.gen_code(i, self.valiables)
                    f = open('test.txt','r')
                    string = f.read()
                    print(string)
                    if string.startswith("And"):
                        string = string.lstrip("And(").rstrip(")")
                    zero_flag = True
                    result_flag = False
                    for k in string.split(", "):
                        if not zero_flag:
                            if k.startswith("Not"):
                                k = k.lstrip("Not(").rstrip(")")
                            else:
                                k = "Not({})".format(k)
                        else:
                            zero_flag = 0
                        if k in previous:
                            print("succeed")
                            result_flag = True
                        else:
                            previous.append(k)
                    print("line {0} :These if statements can be simlified by elif statements.(pattern-1)"\
                    .format(node.lineno))
                    print("I suggest this code should be written")
                    print("elif ",end = "")
                    for j in previous:
                        print(j,end = " ")
                    print()
                    print("previous = {}".format(previous))
                    f.close()
                    self.mode = 0
            conditions = []
        cnt = 0
        for child in ast.iter_child_nodes(node):
            cnt = cnt + 1
            self.one_search(child, cnt, previous, conditions)
    valiables = []
    def gen_code(self, i, valiables):
        if type(i) is not ast.Call:
            constant1 = """
from z3 import *
f = open('test.txt','w')
g  = Goal()
t = Then(Tactic("solve-eqs"),Tactic("simplify"))
val_list = {}
"""
            constant2 ="valiables = {val}\n".format(val = valiables)
            for j in range(len(valiables)):
                constant2 = constant2 + "{} = Int(valiables[j])\n".format(valiables[j])
            constant2 = constant2 + """
for i in range(len(valiables)):
    val_list[i] = Int(valiables[i])
    """
            constant3 = """
f.write(str(s))
f.close()
                    """
            if type(i) is ast.BoolOp:
                if type(i.op) is ast.And:
                    i = ast.Call(func = ast.Name(id = 'And', ctx = ast.Store()), args = i.values, keywords = [])
            source = astor.to_source(ast.Assign(targets = [ast.Name(id = 's',ctx = ast.Store())],value = ast.Call(func = ast.Name(id = 't', ctx = ast.Load()), args = [i], keywords = [])))
            tmp = constant1 + constant2 + source.rstrip() + ".as_expr()" + constant3
            print(tmp)
            exec(compile(tmp,"","exec"))
    def test_val_search(self, node):
        if type(node) is ast.BoolOp:
            for i in node.values:
                self.test_val_search(i)
        elif type(node) is ast.Compare:
            self.test_val_search(node.left)
            for j in node.comparators:
                self.test_val_search(j)
        elif type(node) is ast.BinOp:
            self.test_val_search(node.left)
            self.test_val_search(node.right)
        elif type(node) is ast.Name :
            if node.id not in self.valiables:
                self.valiables.append(node.id)

        elif type(node) is ast.Constant:
            print("Constant class")
        else:
            print("unknown class")
def main():
    """
    main
    """
    # file_name = r'c:\Users\maru\Documents\Github\marui_novice_linter\tryz3.py'
    file_name = r'c:\Users\maru\Documents\Github\marui_novice_linter\pydat.py'
    with open(file_name, 'r', encoding="utf-8_sig") as sourse_file:
        source = sourse_file.read()

    tree = ast.parse(source, file_name)

    AST_Reader(tree)
    # FiveSixNodeVisitor().visit(tree)
    # TwoNodeVisitor().visit(tree)
    OneNodeSearcher().one_search(tree)
if __name__ == '__main__':
    main()