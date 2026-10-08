from __future__ import annotations

from .node import Node


class Stack:
    """Pila LIFO independiente sobre `Node`: no envuelve `LinkedList`.

    Esqueleto del contrato: el algoritmo es del paso 5. Mientras no lo haya, cada
    operación devuelve su indicador.

    Adecuaciones: `pop` y `peek` devuelven -1 con la pila vacía, `is_empty`
    devuelve un booleano y `size` devuelve 0; el enlace ausente es `None`.
    """

    __slots__ = ("_top", "_count")

    def __init__(self) -> None:
        self._top: Node | None = None
        self._count = 0

    def push(self, value: int) -> None:
        """Apila el valor sobre el tope (`push`)."""
        new_top = Node(value)
        new_top.next = self._top
        self._top = new_top
        self._count += 1
        return None

    def pop(self) -> int:
        """Extrae el tope, o -1 si la pila está vacía (`pop`)."""
        if self._top is None:
            return -1
        value = self._top.value
        self._top = self._top.next
        self._count -= 1
        return value

    def peek(self) -> int:
        """Observa el tope sin extraerlo, o -1 si la pila está vacía (`peek`)."""
        return self._top.value if self._top is not None else -1

    def is_empty(self) -> bool:
        """Cierto exactamente cuando la pila no tiene nodos."""
        return self._count == 0

    def size(self) -> int:
        """Número de nodos de la pila (`size`)."""
        return self._count
