from .graph_node import GraphNode


class Graph:
    def __init__(self) -> None:
        self._vertices: GraphNode | None = None
        self._vertex_count: int = 0
        self._edge_count: int = 0

    def _find_vertex(self, label: int) -> GraphNode | None:
        current = self._vertices
        while current is not None:
            if current.value == label:
                return current
            current = current.next_vertex
        return None

    @staticmethod
    def _insert_neighbor(neighbors: list[int], label: int) -> None:
        position = 0
        while position < len(neighbors) and neighbors[position] < label:
            position += 1
        neighbors.insert(position, label)

    def add_vertex(self, label: int) -> bool | None:
        if self._find_vertex(label) is not None:
            return True
        new_vertex = GraphNode(label)
        new_vertex.next_vertex = self._vertices
        self._vertices = new_vertex
        self._vertex_count += 1
        return True

    def add_edge(self, u: int, v: int) -> bool | None:
        u_vertex = self._find_vertex(u)
        if u_vertex is None or self._find_vertex(v) is None:
            return False
        if v in u_vertex.neighbors:
            return True
        self._insert_neighbor(u_vertex.neighbors, v)
        self._edge_count += 1
        return True

    def has_edge(self, u: int, v: int) -> bool | None:
        u_vertex = self._find_vertex(u)
        if u_vertex is None:
            return False
        return v in u_vertex.neighbors

    def get_neighbors(self, u: int) -> list[int] | None:
        u_vertex = self._find_vertex(u)
        if u_vertex is None:
            return None
        return list(u_vertex.neighbors)

    def is_empty(self) -> bool | None:
        return self._vertex_count == 0

    def vertex_count(self) -> int | None:
        return self._vertex_count

    def edge_count(self) -> int | None:
        return self._edge_count
