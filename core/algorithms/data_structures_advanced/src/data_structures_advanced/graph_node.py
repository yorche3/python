from __future__ import annotations

from .node import Node


class GraphNode(Node):
    def __init__(self, label: int) -> None:
        super().__init__(label)
        self._neighbors: list[int] = []
        self._next_vertex: GraphNode | None = None

    @property
    def neighbors(self) -> list[int]:
        return self._neighbors

    @property
    def next_vertex(self) -> GraphNode | None:
        return self._next_vertex

    @next_vertex.setter
    def next_vertex(self, node: GraphNode | None) -> None:
        self._next_vertex = node
