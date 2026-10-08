from __future__ import annotations


class Node:
    """Nodo compartido por `LinkedList`, `Stack` y `Queue`.

    Es el tipo de celda enlazada del módulo: guarda el valor y el enlace al
    siguiente nodo, o `None` cuando no hay enlace. El `init` del contrato es
    `__init__` y sus accesores son propiedades.
    """

    __slots__ = ("_value", "_next")

    def __init__(self, value: int = 0, next_node: Node | None = None) -> None:
        self._value = value
        self._next = next_node

    @property
    def value(self) -> int:
        """Valor del nodo (`get_value`)."""
        return self._value

    @property
    def next(self) -> Node | None:
        """Enlace al siguiente nodo, o `None` si no hay (`get_next`)."""
        return self._next

    @next.setter
    def next(self, node: Node | None) -> None:
        """Enlaza otro nodo (`set_next`)."""
        self._next = node

    def __repr__(self) -> str:
        return f"Node(value={self._value}, next={'...' if self._next else 'None'})"
