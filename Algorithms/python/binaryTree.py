class Node():
    """
    Um nó armazena um valor apenas.

    """
    def __init__(self,value : int):
        self.value = value
class Tree():
    def __init__(self,val,left = None,right = None):
        self.root = Node(val).value
        self.left = left
        self.right = right
    def addLeft(self,value):
        if self.left is None: # se sim, pode adicionar!
            self.left = Tree(value)
        else:
            print("Nó Left está ocupado!")
    def addRight(self, value):
        if self.right is None:
            self.right = Tree(value)
        else:
            print("Nó Right está ocupado!")
    def removeLeft(self):
        if self.left is not None:
            self.left = None
    def removeRight(self):
        if self.right is not None:
            self.right = None
    def showTree(self, depth=0, prefix=''):
        if self.right is not None:
            self.right.showTree(depth + 1, prefix + 'r:')
        print(' ' * 4 * depth + prefix + str(self.root))
        if self.left is not None:
            self.left.showTree(depth + 1, prefix + 'l:')

# - - - - - - - 

arvore = Tree(1)
arvore.addLeft(2)
arvore.addRight(3)
arvore.left.addLeft(4)
arvore.left.addRight(5)
arvore.right.addLeft(6)
arvore.right.addRight(7)

print(arvore.right.showTree())