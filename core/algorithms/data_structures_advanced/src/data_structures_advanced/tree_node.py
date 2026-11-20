from __future__ import annotations

from .node import Node


class TreeNode(Node):
    def __init__(self, value: int) -> None:
        super().__init__(value)
        self._left: TreeNode | None = None
        self._right: TreeNode | None = None

    @property
    def left(self) -> TreeNode | None:
        return self._left

    @left.setter
    def left(self, node: TreeNode | None) -> None:
        self._left = node

    @property
    def right(self) -> TreeNode | None:
        return self._right

    @right.setter
    def right(self, node: TreeNode | None) -> None:
        self._right = node
