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
        return -1

    @property
    def head_node(self) -> Node | None:
        """Nodo de la cabeza, o `None` con la lista vacía.

        Es el punto de partida del recorrido del contrato (`get_next`).
        """
        return None

    def insert_head(self, value: int) -> None:
        """Inserta el valor al principio de la lista (`insert_head`)."""
        return None

    def insert_tail(self, value: int) -> None:
        """Inserta el valor al final de la lista (`insert_tail`)."""
        return None

    def delete(self, value: int) -> bool:
        """Elimina la primera aparición: `True` si estaba, `False` si no."""
        return False

    def is_empty(self) -> bool:
        """Cierto exactamente cuando la lista no tiene nodos."""
        return False

    def size(self) -> int:
        """Número de nodos de la lista (`size`)."""
        return 0
