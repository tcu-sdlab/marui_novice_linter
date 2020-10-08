import ast
import astor

class FiveNodeVisitor(ast.NodeVisitor):

    def visit_FunctionDef(self, node):
        for i in range(len(node.body) - 1):
            if type(node.body[i]) is ast.If and type(node.body[i].body[0]) is ast.Return and 'value' in vars(node.body[i].body[0].value):
                if node.body[i].body[0].value.value and type(node.body[i + 1]) is ast.Return and 'value' in vars(node.body[i + 1].value):
                    if  not node.body[i + 1].value.value:
                        source = astor.to_source(node.body[i].test).replace("\n","")
                        print("line " + str(node.body[i].lineno) + " ~ " + str(node.body[i + 1].lineno) + ": " + source+ " returns Boolean,so you may not need if-statement.")
                        print("I suggest this code should be written")
                        print("     return " + source)
                
        return node
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
    FILENAME = r'c:\Users\maru\Documents\pyAST_ex\pydat.py'

    with open(FILENAME, 'r') as f:
        source = f.read()

    tree = ast.parse(source, FILENAME)
    AST_Reader(tree)

    FiveNodeVisitor().visit(tree)

if __name__ == '__main__':
    main()