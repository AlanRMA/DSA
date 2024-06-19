class BinaryTree():
    class Node():
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self, value=None):
        self.root = self.Node(value) if value else None

    def add(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._add(value, node.left)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._add(value, node.right)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _delete(self, value, node):
        if node is None:
            return None
        elif value < node.value:
            node.left = self._delete(value, node.left)
            return node
        elif value > node.value:
            node.right = self._delete(value, node.right)
            return node
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete(min_node.value, node.right)

            return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def print(self):
        print(self._print(self.root).replace("\n", "\n    "))

    def _print(self, node):
        if node is None:
            return ""
        elif node.left is None and node.right is None:
            return str(node.value)
        else:
            left = self._print(node.left)
            right = self._print(node.right)
            return f"({left}\n {node.value} \n{right})"


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(4)
    tree.add(2)
    tree.add(6)
    tree.add(1)
    tree.add(3)
    tree.add(5)
    tree.add(7)
    tree.delete(2)
    tree.print()
