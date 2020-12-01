class OneNodeSearcher():
    def one_search(self, node, count = 0, previous = {}, conditions = []):
        if type(node) is ast.If:
            