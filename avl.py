from node import Node
from rotations import left_rotate, right_rotate


class AVL:
    def get_height(self, root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def insert(self, root, key):

        # BST insert
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # update height
        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right)
        )

        balance = self.get_balance(root)

        # -------------------------
        # ROTATIONS (SAFE VERSION)
        # -------------------------

        # LL
        if balance > 1 and root.left and key < root.left.key:
            return right_rotate(root)

        # RR
        if balance < -1 and root.right and key > root.right.key:
            return left_rotate(root)

        # LR
        if balance > 1 and root.left and key > root.left.key:
            root.left = left_rotate(root.left)
            return right_rotate(root)

        # RL
        if balance < -1 and root.right and key < root.right.key:
            root.right = right_rotate(root.right)
            return left_rotate(root)

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