class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DLL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.d = {}

    def insert(self, name):
        if name in self.d:
            self.removeInsert(name)
            return 
        node = Node(name)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.d[name] = node

    def removeInsert(self, name): #asuming node nil values
        node = self.d[name]
        if node != self.head:
            node.prev.next = node.next
            if node == self.tail:
                self.tail = node.prev
            else:
                node.next.prev = node.prev

            del node
            newnode = Node(name)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            self.d[name] = newnode

n = int(input())
dll = DLL()
for i in range(n):
    dll.insert(input())
p = dll.head
while p != None:
    print(p.val)
    p  = p.next