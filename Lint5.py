import ast
import astor

class FiveSixNodeVisitor(ast.NodeVisitor):

    def visit_FunctionDef(self, node):
        pattern_num = 0
        node.body.append("")
        for i in range(len(node.body) - 1):
            if type(node.body[i]) is ast.If and type(node.body[i].body[0]) is ast.Return and 'value' in vars(node.body[i].body[0].value):
                if type(node.body[i].body[0].value.value) is bool and node.body[i].body[0].value.value:                    
                    linenum = -1

                    if  type(node.body[i + 1]) is ast.Return and 'value' in vars(node.body[i + 1].value):
                        if type(node.body[i + 1].value.value) is bool and not node.body[i + 1].value.value:
                            linenum = node.body[i + 1].lineno
                    elif node.body[i].orelse:
                        if type(node.body[i].orelse[0]) is ast.Return and 'value' in vars(node.body[i].orelse[0].value):
                            if type(node.body[i].orelse[0].value.value) is bool and not node.body[i].orelse[0].value.value:
                                linenum = node.body[i].orelse[0].lineno
                            
                    if linenum != -1:
                        source = astor.to_source(node.body[i].test).replace("\n","")

                        if type(node.body[i].test) is ast.Compare:
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
                    print("line {0} ~ {1} :These conjoining conditions{2} using nested if statements can be simplified by using and operator.(pattern-2)".format(node.lineno, lineno, conditions))
                    print("I suggest this code should be written")
                    # print("elif_check={}".format(self.elif_check))
                    if self.elif_check == 1:
                        print("     elif ", end = "")
                    else:
                        print("     if ", end = "")
                    i = 0
                    for i in range(len(conditions) - 1):
                        print(conditions[i],end = "")
                        print(" and ",end = "")
                    print(conditions[i + 1],end = "")
                    print(":")
                conditions.clear()
        if node.orelse:
            # print("行きます")
            print(node.orelse)
            self.elif_check = 1
            self.visit(node.orelse[0])
            # print("完了です")
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

def main():
    FILENAME = r'c:\Users\maru\Documents\Github\marui_novice_linter\pydat.py'

    with open(FILENAME, 'r') as f:
        source = f.read()

    tree = ast.parse(source, FILENAME)
    AST_Reader(tree)

    #FiveSixNodeVisitor().visit(tree)
    print()
    TwoNodeVisitor().visit(tree)

if __name__ == '__main__':
    main()