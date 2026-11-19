from __future__ import annotations

from .node import Node


class TreeNode(Node):
    def __init__(self, value: int) -> None:
        return None

    @property
    def left(self) -> TreeNode | None:
        return None

    @left.setter
    def left(self, node: TreeNode | None) -> None:
        return None

    @property
    def right(self) -> TreeNode | None:
        return None

    @right.setter
    def right(self, node: TreeNode | None) -> None:
        return None
