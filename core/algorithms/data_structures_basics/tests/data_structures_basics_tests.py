from collections.abc import Callable

from data_structures_basics import LinkedList, Node, Queue, Stack


FAILURE_INDICATOR = -1

NODE_INITIAL_INPUT = 10
NODE_INITIAL_VALUE = 10
NODE_LINKED_INPUT = 20
NODE_LINKED_VALUE = 20

LIST_EMPTY_SIZE = 0
LIST_INSERT_TAIL_FIRST = 10
LIST_INSERT_TAIL_SECOND = 20
LIST_INSERT_HEAD = 5
LIST_INSERT_TAIL_THIRD = 10
LIST_INSERT_OUTPUT = (5, 10, 20, 10)
LIST_DELETE_FIRST_VALUE = 10
LIST_DELETE_FIRST_OUTPUT = (5, 20, 10)
LIST_DELETE_FIRST_SIZE = 3
LIST_ABSENT_VALUE = 99
LIST_EMPTY_VALUES = (5, 20, 10)

STACK_VALUES = (10, 20, 30)
STACK_PEEK_VALUE = 30
STACK_SIZE_AFTER_PUSH = 3
STACK_REUSED_VALUE = 40
STACK_POP_OUTPUT = (30, 40, 20, 10)

QUEUE_VALUES = (10, 20, 30)
QUEUE_PEEK_VALUE = 10
QUEUE_SIZE_AFTER_ENQUEUE = 3
QUEUE_REUSED_VALUE = 40
QUEUE_DEQUEUE_OUTPUT = (10, 20, 30, 40)

Check = tuple[str, object, object]
Scenario = Callable[[object], tuple[Check, ...]]


def run_scenario(subject_name: str, subject: object, cases: tuple[tuple[str, Scenario], ...]) -> None:
    for case_name, case in cases:
        for operation, actual, expected in case(subject):
            assert actual == expected, (
                f"{subject_name} should return {expected!r} for {operation} "
                f"in {case_name}; got {actual!r}"
            )


def linked_list_values(linked_list: LinkedList) -> tuple[int, ...]:
    values: list[int] = []
    node = linked_list.head_node
    while node is not None:
        values.append(node.value)
        node = node.next
    return tuple(values)


def test_node() -> None:
    def initialize_and_observe_value_and_link(subject: object) -> tuple[Check, ...]:
        node = subject
        assert isinstance(node, Node)
        return (
            ("get_value", node.value, NODE_INITIAL_VALUE),
            ("get_next", node.next, None),
        )

    def initialize_link_and_traverse(subject: object) -> tuple[Check, ...]:
        node = subject
        assert isinstance(node, Node)
        linked_node = Node(NODE_LINKED_INPUT)
        node.next = linked_node
        return (
            ("get_value(get_next)", node.next.value if node.next is not None else None, NODE_LINKED_VALUE),
            ("get_next(linked node)", linked_node.next, None),
        )

    run_scenario(
        "Node",
        Node(NODE_INITIAL_INPUT),
        (
            (
                "initialize and observe value/link",
                initialize_and_observe_value_and_link,
            ),
            (
                "initialize another node, link and traverse",
                initialize_link_and_traverse,
            ),
        ),
    )


def test_linked_list() -> None:
    def empty_state(subject: object) -> tuple[Check, ...]:
        linked_list = subject
        assert isinstance(linked_list, LinkedList)
        return (
            ("is_empty", linked_list.is_empty(), True),
            ("size", linked_list.size(), LIST_EMPTY_SIZE),
            ("get_head", linked_list.head, FAILURE_INDICATOR),
        )

    def insert_at_both_ends(subject: object) -> tuple[Check, ...]:
        linked_list = subject
        assert isinstance(linked_list, LinkedList)
        linked_list.insert_tail(LIST_INSERT_TAIL_FIRST)
        linked_list.insert_tail(LIST_INSERT_TAIL_SECOND)
        linked_list.insert_head(LIST_INSERT_HEAD)
        linked_list.insert_tail(LIST_INSERT_TAIL_THIRD)
        return (
            ("size", linked_list.size(), len(LIST_INSERT_OUTPUT)),
            ("traversal from get_head", linked_list_values(linked_list), LIST_INSERT_OUTPUT),
        )

    def delete_first_occurrence(subject: object) -> tuple[Check, ...]:
        linked_list = subject
        assert isinstance(linked_list, LinkedList)
        return (
            ("delete", linked_list.delete(LIST_DELETE_FIRST_VALUE), True),
            ("traversal from get_head", linked_list_values(linked_list), LIST_DELETE_FIRST_OUTPUT),
            ("size", linked_list.size(), LIST_DELETE_FIRST_SIZE),
        )

    def absent_value(subject: object) -> tuple[Check, ...]:
        linked_list = subject
        assert isinstance(linked_list, LinkedList)
        return (
            ("delete", linked_list.delete(LIST_ABSENT_VALUE), False),
            ("traversal from get_head", linked_list_values(linked_list), LIST_DELETE_FIRST_OUTPUT),
            ("size", linked_list.size(), LIST_DELETE_FIRST_SIZE),
        )

    def empty_the_list(subject: object) -> tuple[Check, ...]:
        linked_list = subject
        assert isinstance(linked_list, LinkedList)
        return (
            ("delete(5)", linked_list.delete(LIST_EMPTY_VALUES[0]), True),
            ("delete(20)", linked_list.delete(LIST_EMPTY_VALUES[1]), True),
            ("delete(10)", linked_list.delete(LIST_EMPTY_VALUES[2]), True),
            ("is_empty", linked_list.is_empty(), True),
            ("size", linked_list.size(), LIST_EMPTY_SIZE),
            ("get_head", linked_list.head, FAILURE_INDICATOR),
        )

    run_scenario(
        "LinkedList",
        LinkedList(),
        (
            ("empty state", empty_state),
            ("insert at both ends", insert_at_both_ends),
            ("delete first occurrence", delete_first_occurrence),
            ("absent value", absent_value),
            ("empty the list", empty_the_list),
        ),
    )


def test_stack() -> None:
    def empty_state_and_failed_removal(subject: object) -> tuple[Check, ...]:
        stack = subject
        assert isinstance(stack, Stack)
        return (
            ("is_empty", stack.is_empty(), True),
            ("size", stack.size(), LIST_EMPTY_SIZE),
            ("peek", stack.peek(), FAILURE_INDICATOR),
            ("pop", stack.pop(), FAILURE_INDICATOR),
        )

    def lifo_and_non_mutating_peek(subject: object) -> tuple[Check, ...]:
        stack = subject
        assert isinstance(stack, Stack)
        for value in STACK_VALUES:
            stack.push(value)
        return (
            ("peek", stack.peek(), STACK_PEEK_VALUE),
            ("size", stack.size(), STACK_SIZE_AFTER_PUSH),
        )

    def removal_and_reuse(subject: object) -> tuple[Check, ...]:
        stack = subject
        assert isinstance(stack, Stack)
        first_pop = stack.pop()
        stack.push(STACK_REUSED_VALUE)
        return (
            ("first pop", first_pop, STACK_POP_OUTPUT[0]),
            ("second pop", stack.pop(), STACK_POP_OUTPUT[1]),
            ("third pop", stack.pop(), STACK_POP_OUTPUT[2]),
            ("fourth pop", stack.pop(), STACK_POP_OUTPUT[3]),
            ("is_empty", stack.is_empty(), True),
            ("size", stack.size(), LIST_EMPTY_SIZE),
        )

    def empty_after_removal(subject: object) -> tuple[Check, ...]:
        stack = subject
        assert isinstance(stack, Stack)
        return (
            ("pop", stack.pop(), FAILURE_INDICATOR),
            ("is_empty", stack.is_empty(), True),
        )

    run_scenario(
        "Stack",
        Stack(),
        (
            ("empty state and failed removal", empty_state_and_failed_removal),
            ("LIFO and non-mutating peek", lifo_and_non_mutating_peek),
            ("removal and reuse", removal_and_reuse),
            ("empty after removal", empty_after_removal),
        ),
    )


def test_queue() -> None:
    def empty_state_and_failed_removal(subject: object) -> tuple[Check, ...]:
        queue = subject
        assert isinstance(queue, Queue)
        return (
            ("is_empty", queue.is_empty(), True),
            ("size", queue.size(), LIST_EMPTY_SIZE),
            ("peek", queue.peek(), FAILURE_INDICATOR),
            ("dequeue", queue.dequeue(), FAILURE_INDICATOR),
        )

    def fifo_and_non_mutating_peek(subject: object) -> tuple[Check, ...]:
        queue = subject
        assert isinstance(queue, Queue)
        for value in QUEUE_VALUES:
            queue.enqueue(value)
        return (
            ("peek", queue.peek(), QUEUE_PEEK_VALUE),
            ("size", queue.size(), QUEUE_SIZE_AFTER_ENQUEUE),
        )

    def removal_and_reuse(subject: object) -> tuple[Check, ...]:
        queue = subject
        assert isinstance(queue, Queue)
        first_dequeue = queue.dequeue()
        queue.enqueue(QUEUE_REUSED_VALUE)
        return (
            ("first dequeue", first_dequeue, QUEUE_DEQUEUE_OUTPUT[0]),
            ("second dequeue", queue.dequeue(), QUEUE_DEQUEUE_OUTPUT[1]),
            ("third dequeue", queue.dequeue(), QUEUE_DEQUEUE_OUTPUT[2]),
            ("fourth dequeue", queue.dequeue(), QUEUE_DEQUEUE_OUTPUT[3]),
            ("is_empty", queue.is_empty(), True),
            ("size", queue.size(), LIST_EMPTY_SIZE),
        )

    def empty_after_removal(subject: object) -> tuple[Check, ...]:
        queue = subject
        assert isinstance(queue, Queue)
        return (
            ("dequeue", queue.dequeue(), FAILURE_INDICATOR),
            ("is_empty", queue.is_empty(), True),
        )

    run_scenario(
        "Queue",
        Queue(),
        (
            ("empty state and failed removal", empty_state_and_failed_removal),
            ("FIFO and non-mutating peek", fifo_and_non_mutating_peek),
            ("removal and reuse", removal_and_reuse),
            ("empty after removal", empty_after_removal),
        ),
    )