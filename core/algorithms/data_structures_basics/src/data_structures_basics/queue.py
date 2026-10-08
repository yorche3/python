from __future__ import annotations

from .node import Node


class Queue:
    """Cola FIFO independiente sobre `Node`: no envuelve `LinkedList`.

    Esqueleto del contrato: el algoritmo es del paso 5. Mientras no lo haya, cada
    operación devuelve su indicador.

    Adecuaciones: `dequeue` y `peek` devuelven -1 con la cola vacía, `is_empty`
    devuelve un booleano y `size` devuelve 0; los enlaces ausentes son `None`.
    """

    __slots__ = ("_front", "_rear", "_count")

    def __init__(self) -> None:
        self._front: Node | None = None
        self._rear: Node | None = None
        self._count = 0

    def enqueue(self, value: int) -> None:
        """Añade el valor por el final de la cola (`enqueue`)."""
        return None

    def dequeue(self) -> int:
        """Extrae el frente, o -1 si la cola está vacía (`dequeue`)."""
        return -1

    def peek(self) -> int:
        """Observa el frente sin extraerlo, o -1 si la cola está vacía (`peek`)."""
        return -1

    def is_empty(self) -> bool:
        """Cierto exactamente cuando la cola no tiene nodos."""
        return False

    def size(self) -> int:
        """Número de nodos de la cola (`size`)."""
        return 0
