from .tree_node import TreeNode

class BinaryTree:
    def __init__(self) -> None:
        self._root: TreeNode | None = None
        self._count: int = 0

    def insert(self, value: int) -> bool | None:
        if self._root is None:
            self._root = TreeNode(value)
            self._count += 1
            return True
        current = self._root
        while True:
            if value == current.value:
                return True
            elif value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    self._count += 1
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    self._count += 1
                    return True
                current = current.right

    def contains(self, value: int) -> bool | None:
        current = self._root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def is_empty(self) -> bool | None:
        return self._count == 0

    def size(self) -> int | None:
        return self._count
