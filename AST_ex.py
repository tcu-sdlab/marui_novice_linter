import ast

class PrintNodeVisitor(ast.NodeVisitor):
    def visit(self, node):
        print(vars(node))
        return super().visit(node)


class VariableNodeVisitor(ast.NodeVisitor):
    vallist = {}
    def visit_Assign(self, node):
        self.vallist[node.targets[0].id] = node.value.value
        return node
    def get_list(self):
        print(self.vallist)
    
    def search_val(self,node):
        self.visit(node)
        self.get_list()


class FunctionNodeVisitor(ast.NodeVisitor):
    def visit_Call(self,node):
        print(node.func.id)
        return node

    def search_func(self,node):
        self.visit(node)


class IfNodeVisitor(ast.NodeVisitor):
    exceptlist =[]
    def visit_If(self, node):
        if not id(node)  in self.exceptlist:
            self.exceptlist.append(id(node))
            self.visit(node.test)
            if 'orelse' in vars(node):
                for i in node.orelse:
                    if type(i) is ast.If:
                        print("elif", end = " ")
                        self.visit(i)
        return node

    def put_value(self, dat):
        if type(dat) is ast.BinOp:
            self.put_value(dat.left)
            if type(dat.op) is ast.Add:
                print("+", end = " ")
            self.put_value(dat.right)
        elif 'id' in vars(dat):
            print(dat.id,end = " ")
        else:
            print(dat.value,end=' ')
    def visit_BoolOp(self, node):
        if type(node.op) is ast.And:
            print("and",end= " ")
        elif type(node.op) is ast.Or:
            print("or",end= " ")
        for i in node.values:
            # self.exceptlist.append(id(i))
            self.put_value(i.left)
            if type(i.ops[0]) is ast.Eq:
                print("==",end=' ')
            elif type(i.ops[0]) is ast.NotEq:
                print("!=",end=' ')
            elif type(i.ops[0]) is ast.Gt:
                print(">",end=' ')
            self.put_value(i.comparators[0])
        print()
        return node
    def visit_Compare(self, node):
        # if id(node) not in self.exceptlist:

        self.put_value(node.left)

        if type(node.ops[0]) is ast.Eq:
            print("==",end=' ')
        elif type(node.ops[0]) is ast.NotEq:
            print("!=",end=' ')
        elif type(node.ops[0]) is ast.Gt:
            print(">",end=' ')
        self.put_value(node.comparators[0])
        print()
def search_if(node,val, address = []):
    if type(node) is ast.If and not id(node) in address:
        address.append(id(node))
        print("条件文は")
        #ブール演算子かどうか
        if type(node.test) is ast.BoolOp:
            if type(node.test.op) is ast.And:
                print("and",end=' ')
        else:
            if 'id' in vars(node.test.left):
                print(node.test.left.id+"("+ str(val[node.test.left.id]) +")")
            else:
                print(node.test.left.value,end=' ')

            if type(node.test.ops[0]) is ast.Eq:
                print("==",end=' ')
            elif type(node.test.ops[0]) is ast.NotEq:
                print("!=",end=' ')
            elif type(node.test.ops[0]) is ast.Gt:
                print(">",end=' ')
            
            if 'id' in vars(node.test.comparators[0]):
                print(node.test.comparators[0].id+"("+ str(val[node.test.comparators[0].id]) +")")
            else:
                print(node.test.comparators[0].value)
        for ellist in node.orelse:
            search_if(ellist,val,address)
    for child in ast.iter_child_nodes(node):
        search_if(child,val,address)

def walk(node, indent=0):
    # 入れ子構造をインデントで表現する
    print(' ' * indent, end='')

    # クラス名を表示する
    print(node.__class__, end='')

    # 行数の情報があれば表示する
    if hasattr(node, 'lineno'):
        msg = ': {lineno}'.format(lineno=node.lineno)
        print(msg, end='')

    # 改行を入れる
    print()

    # 再帰的に実行する
    for child in ast.iter_child_nodes(node):
        walk(child, indent=indent+4)

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

def main():
    FILENAME = r'c:\Users\maru\Documents\pyAST_ex\pydat.py'

    with open(FILENAME, 'r') as f:
        source = f.read()
    print("Node")
    tree = ast.parse(source, FILENAME)
    walk(tree)

    print("view")
    AST_Reader(tree)

    print("\n\nsearch")
    FunctionNodeVisitor().search_func(tree)
    print("\nvariable")
    VariableNodeVisitor().search_val(tree)

    print("\nif")
    IfNodeVisitor().visit(tree)

    # print("search_if")
    # search_if(tree,val)

if __name__ == '__main__':
    main()