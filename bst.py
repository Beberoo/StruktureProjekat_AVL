import sys
from node import Node

sys.setrecursionlimit(10000)


class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        
        current = root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    break
                else:
                    current = current.right
        
        return root

    def search(self, root, key):
        current = root
        while current is not None:
            if current.key == key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None