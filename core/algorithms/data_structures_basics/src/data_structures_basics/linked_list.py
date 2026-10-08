from __future__ import annotations

from .node import Node


class LinkedList:
    """Lista simplemente enlazada con referencias a cabeza, cola y contador.

    Esqueleto del contrato: el algoritmo es del paso 5. Mientras no lo haya, cada
    operación devuelve su indicador.

    Adecuaciones: los enlaces ausentes son `None`, que solo se usa para nodos;
    `head` devuelve -1 y `head_node` devuelve `None` con la lista vacía; `delete`
    devuelve un booleano y `size` devuelve 0.
    """

    __slots__ = ("_head", "_tail", "_count")

    def __init__(self) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None
        self._count = 0

    @property
    def head(self) -> int:
        """Valor de la cabeza, o -1 con la lista vacía (`get_head`)."""
        return self._head.value if self._head is not None else -1

    @property
    def head_node(self) -> Node | None:
        """Nodo de la cabeza, o `None` con la lista vacía.

        Es el punto de partida del recorrido del contrato (`get_next`).
        """
        return self._head

    def insert_head(self, value: int) -> None:
        """Inserta el valor al principio de la lista (`insert_head`)."""
        new_head = Node(value)
        new_head.next = self._head
        self._head = new_head
        if self._tail is None:
            self._tail = new_head
        self._count += 1

    def insert_tail(self, value: int) -> None:
        """Inserta el valor al final de la lista (`insert_tail`)."""
        new_tail = Node(value)
        if self._tail is not None:
            self._tail.next = new_tail
        self._tail = new_tail
        if self._head is None:
            self._head = new_tail
        self._count += 1

    def delete(self, value: int) -> bool:
        """Elimina la primera aparición: `True` si estaba, `False` si no."""
        prev: Node | None = None
        current = self._head
        while current is not None:
            if current.value == value:
                if prev is None:
                    self._head = current.next
                else:
                    prev.next = current.next
                if current.next is None:
                    self._tail = prev
                self._count -= 1
                return True
            prev = current
            current = current.next
        return False

    def is_empty(self) -> bool:
        """Cierto exactamente cuando la lista no tiene nodos."""
        return self._count == 0

    def size(self) -> int:
        """Número de nodos de la lista (`size`)."""
        return self._count
