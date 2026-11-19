from collections.abc import Callable

import pytest

from data_structures_advanced import BinaryTree, Graph, TreeNode


SUCCESS_INDICATOR = True
FAILURE_INDICATOR = False
ABSENT = None
NEIGHBORS_FAILURE_INDICATOR = None

TREE_NODE_VALUE = 10
TREE_NODE_LEFT_INPUT = 20
TREE_NODE_RIGHT_INPUT = 30

TREE_EMPTY_SIZE = 0
TREE_ROOT_VALUE = 50
TREE_LOWER_VALUE = 30
TREE_HIGHER_VALUE = 70
TREE_LEFT_LEAF_VALUE = 20
TREE_RIGHT_LEAF_VALUE = 40
TREE_ABSENT_VALUE = 99
TREE_THREE_VALUES = (50, 30, 70)
TREE_FIVE_VALUES = (50, 30, 70, 20, 40)
TREE_DUPLICATE_INPUT = (50, 30, 70, 30)
TREE_ORDERED_INPUT = (20, 30, 40, 50, 70)

GRAPH_FIRST = 10
GRAPH_SECOND = 30
GRAPH_THIRD = 50
GRAPH_FOURTH = 70
GRAPH_MISSING = 99
GRAPH_MISSING_OTHER = 98

Check = tuple[str, object, object]
Scenario = Callable[[], tuple[Check, ...]]


def run_scenarios(subject_name: str, case_name: str, scenario: Scenario) -> None:
    for operation, actual, expected in scenario():
        assert actual == expected, (
            f"{subject_name} should return {expected!r} for {operation} "
            f"in {case_name}; got {actual!r}"
        )


def tree_with(values: tuple[int, ...]) -> tuple[BinaryTree, tuple[Check, ...]]:
    tree = BinaryTree()
    inserts = tuple((f"insert({value})", tree.insert(value), SUCCESS_INDICATOR) for value in values)
    return tree, inserts


def contains_checks(tree: BinaryTree, values: tuple[int, ...]) -> tuple[Check, ...]:
    return tuple((f"contains({value})", tree.contains(value), SUCCESS_INDICATOR) for value in values)


def graph_with(vertices: tuple[int, ...]) -> tuple[Graph, tuple[Check, ...]]:
    graph = Graph()
    adds = tuple((f"add_vertex({label})", graph.add_vertex(label), SUCCESS_INDICATOR) for label in vertices)
    return graph, adds


def edge_checks(graph: Graph, edges: tuple[tuple[int, int], ...]) -> tuple[Check, ...]:
    return tuple(
        (f"add_edge({u},{v})", graph.add_edge(u, v), SUCCESS_INDICATOR) for u, v in edges
    )


def counts(graph: Graph, vertices: int, edges: int) -> tuple[Check, ...]:
    return (
        ("vertex_count", graph.vertex_count(), vertices),
        ("edge_count", graph.edge_count(), edges),
    )


def value_of(node: TreeNode | None) -> int | None:
    return node.value if node is not None else None


def tree_node_create() -> tuple[Check, ...]:
    node = TreeNode(TREE_NODE_VALUE)
    return (("get_value", node.value, TREE_NODE_VALUE),)


def tree_node_absent_links() -> tuple[Check, ...]:
    node = TreeNode(TREE_NODE_VALUE)
    return (
        ("get_left", node.left, ABSENT),
        ("get_right", node.right, ABSENT),
    )


def tree_node_link_two_children() -> tuple[Check, ...]:
    parent = TreeNode(TREE_NODE_VALUE)
    parent.left = TreeNode(TREE_NODE_LEFT_INPUT)
    parent.right = TreeNode(TREE_NODE_RIGHT_INPUT)
    return (
        ("get_value(get_left)", value_of(parent.left), TREE_NODE_LEFT_INPUT),
        ("get_value(get_right)", value_of(parent.right), TREE_NODE_RIGHT_INPUT),
    )


def tree_node_traverse_each_link() -> tuple[Check, ...]:
    parent = TreeNode(TREE_NODE_VALUE)
    parent.left = TreeNode(TREE_NODE_LEFT_INPUT)
    parent.right = TreeNode(TREE_NODE_RIGHT_INPUT)
    left, right = parent.left, parent.right
    return (
        ("get_left value", value_of(left), TREE_NODE_LEFT_INPUT),
        ("get_right value", value_of(right), TREE_NODE_RIGHT_INPUT),
        ("get_left(left)", left.left if left else ABSENT, ABSENT),
        ("get_right(left)", left.right if left else TREE_ABSENT_VALUE, ABSENT),
        ("get_left(right)", right.left if right else TREE_ABSENT_VALUE, ABSENT),
        ("get_right(right)", right.right if right else TREE_ABSENT_VALUE, ABSENT),
    )


def tree_node_unlink_children() -> tuple[Check, ...]:
    parent = TreeNode(TREE_NODE_VALUE)
    parent.left = TreeNode(TREE_NODE_LEFT_INPUT)
    parent.right = TreeNode(TREE_NODE_RIGHT_INPUT)
    parent.left = None
    after_left = (
        ("value after clearing left", parent.value, TREE_NODE_VALUE),
        ("get_left after clearing left", parent.left, ABSENT),
        ("get_value(get_right) after clearing left", value_of(parent.right), TREE_NODE_RIGHT_INPUT),
    )
    parent.right = None
    return after_left + (
        ("value after clearing right", parent.value, TREE_NODE_VALUE),
        ("get_left after clearing right", parent.left, ABSENT),
        ("get_right after clearing right", parent.right, ABSENT),
    )


TREE_NODE_CASES: tuple[tuple[str, Scenario], ...] = (
    ("create a tree node", tree_node_create),
    ("absent initial links", tree_node_absent_links),
    ("link two children", tree_node_link_two_children),
    ("traverse each link", tree_node_traverse_each_link),
    ("unlink children", tree_node_unlink_children),
)


def tree_create_empty() -> tuple[Check, ...]:
    tree = BinaryTree()
    return (
        ("is_empty", tree.is_empty(), True),
        ("size", tree.size(), TREE_EMPTY_SIZE),
        ("contains(50)", tree.contains(TREE_ROOT_VALUE), FAILURE_INDICATOR),
    )


def tree_insert_root() -> tuple[Check, ...]:
    tree, inserts = tree_with((TREE_ROOT_VALUE,))
    return inserts + (
        ("size", tree.size(), 1),
        ("is_empty", tree.is_empty(), False),
        ("contains(50)", tree.contains(TREE_ROOT_VALUE), SUCCESS_INDICATOR),
    )


def tree_insert_lower_and_higher() -> tuple[Check, ...]:
    tree, inserts = tree_with(TREE_THREE_VALUES)
    return inserts + (("size", tree.size(), 3),) + contains_checks(tree, TREE_THREE_VALUES)


def tree_multilevel_branches() -> tuple[Check, ...]:
    tree, inserts = tree_with(TREE_FIVE_VALUES)
    return inserts + contains_checks(tree, TREE_FIVE_VALUES) + (("size", tree.size(), 5),)


def tree_missing_value_in_nonempty_tree() -> tuple[Check, ...]:
    tree, inserts = tree_with((TREE_ROOT_VALUE,))
    return inserts + (
        ("contains(99)", tree.contains(TREE_ABSENT_VALUE), FAILURE_INDICATOR),
        ("size", tree.size(), 1),
        ("contains(50)", tree.contains(TREE_ROOT_VALUE), SUCCESS_INDICATOR),
    )


def tree_idempotent_duplicate() -> tuple[Check, ...]:
    tree, inserts = tree_with(TREE_DUPLICATE_INPUT)
    return inserts + (("size", tree.size(), 3),) + contains_checks(tree, TREE_THREE_VALUES)


def tree_ordered_insertions() -> tuple[Check, ...]:
    tree, inserts = tree_with(TREE_ORDERED_INPUT)
    return inserts + (
        ("size", tree.size(), 5),
    ) + contains_checks(tree, TREE_ORDERED_INPUT) + (
        ("contains(99)", tree.contains(TREE_ABSENT_VALUE), FAILURE_INDICATOR),
    )


BINARY_TREE_CASES: tuple[tuple[str, Scenario], ...] = (
    ("create empty", tree_create_empty),
    ("insert the root", tree_insert_root),
    ("insert lower and higher", tree_insert_lower_and_higher),
    ("multilevel branches", tree_multilevel_branches),
    ("missing value in nonempty tree", tree_missing_value_in_nonempty_tree),
    ("idempotent duplicate", tree_idempotent_duplicate),
    ("ordered insertions", tree_ordered_insertions),
)


def graph_create_empty() -> tuple[Check, ...]:
    graph = Graph()
    return (
        ("is_empty", graph.is_empty(), True),
        ("vertex_count", graph.vertex_count(), 0),
        ("edge_count", graph.edge_count(), 0),
        ("has_edge(10,30)", graph.has_edge(GRAPH_FIRST, GRAPH_SECOND), FAILURE_INDICATOR),
        ("get_neighbors(10)", graph.get_neighbors(GRAPH_FIRST), NEIGHBORS_FAILURE_INDICATOR),
    )


def graph_isolated_vertex() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST,))
    return adds + (
        ("is_empty", graph.is_empty(), False),
    ) + counts(graph, 1, 0) + (
        ("get_neighbors(10)", graph.get_neighbors(GRAPH_FIRST), []),
    )


def graph_nonconsecutive_labels_and_directed_edge() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST, GRAPH_FOURTH))
    return adds + edge_checks(graph, ((GRAPH_FIRST, GRAPH_FOURTH),)) + (
        ("has_edge(10,70)", graph.has_edge(GRAPH_FIRST, GRAPH_FOURTH), SUCCESS_INDICATOR),
        ("has_edge(70,10)", graph.has_edge(GRAPH_FOURTH, GRAPH_FIRST), FAILURE_INDICATOR),
    ) + counts(graph, 2, 1)


def graph_duplicate_vertex_preserves_adjacency() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST, GRAPH_SECOND))
    return adds + edge_checks(graph, ((GRAPH_FIRST, GRAPH_SECOND),)) + (
        ("add_vertex(10) again", graph.add_vertex(GRAPH_FIRST), SUCCESS_INDICATOR),
    ) + counts(graph, 2, 1) + (
        ("get_neighbors(10)", graph.get_neighbors(GRAPH_FIRST), [GRAPH_SECOND]),
    )


def graph_duplicate_edge() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST, GRAPH_SECOND))
    return adds + edge_checks(graph, ((GRAPH_FIRST, GRAPH_SECOND),) * 2) + counts(graph, 2, 1) + (
        ("get_neighbors(10)", graph.get_neighbors(GRAPH_FIRST), [GRAPH_SECOND]),
    )


def graph_missing_endpoint_without_mutation() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST, GRAPH_SECOND))
    valid_edge = edge_checks(graph, ((GRAPH_FIRST, GRAPH_SECOND),))
    attempts = (
        (GRAPH_FIRST, GRAPH_MISSING),
        (GRAPH_MISSING, GRAPH_FIRST),
        (GRAPH_MISSING_OTHER, GRAPH_MISSING),
        (GRAPH_MISSING, GRAPH_MISSING),
    )
    failures = tuple(
        (f"add_edge({u},{v})", graph.add_edge(u, v), FAILURE_INDICATOR) for u, v in attempts
    )
    absent_edges = tuple(
        (f"has_edge({u},{v})", graph.has_edge(u, v), FAILURE_INDICATOR) for u, v in attempts
    )
    return adds + valid_edge + failures + counts(graph, 2, 1) + (
        ("get_neighbors(10)", graph.get_neighbors(GRAPH_FIRST), [GRAPH_SECOND]),
        ("get_neighbors(30)", graph.get_neighbors(GRAPH_SECOND), []),
    ) + absent_edges + (
        ("get_neighbors(98)", graph.get_neighbors(GRAPH_MISSING_OTHER), NEIGHBORS_FAILURE_INDICATOR),
        ("get_neighbors(99)", graph.get_neighbors(GRAPH_MISSING), NEIGHBORS_FAILURE_INDICATOR),
    )


def graph_sorted_neighbors_and_counts() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST, GRAPH_SECOND, GRAPH_THIRD, GRAPH_FOURTH))
    edges = ((GRAPH_FIRST, GRAPH_FOURTH), (GRAPH_FIRST, GRAPH_SECOND),
             (GRAPH_FIRST, GRAPH_THIRD), (GRAPH_SECOND, GRAPH_THIRD))
    return adds + edge_checks(graph, edges) + (
        ("get_neighbors(10)", graph.get_neighbors(GRAPH_FIRST), [30, 50, 70]),
        ("get_neighbors(30)", graph.get_neighbors(GRAPH_SECOND), [50]),
        ("get_neighbors(50)", graph.get_neighbors(GRAPH_THIRD), []),
        ("get_neighbors(70)", graph.get_neighbors(GRAPH_FOURTH), []),
    ) + counts(graph, 4, 4)


def graph_missing_edge_query() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST, GRAPH_SECOND))
    return adds + (
        ("has_edge(10,30)", graph.has_edge(GRAPH_FIRST, GRAPH_SECOND), FAILURE_INDICATOR),
    ) + counts(graph, 2, 0) + (("is_empty", graph.is_empty(), False),)


def graph_neighbors_of_missing_vertex() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST,))
    return adds + (
        ("get_neighbors(99)", graph.get_neighbors(GRAPH_MISSING), NEIGHBORS_FAILURE_INDICATOR),
        ("get_neighbors(10)", graph.get_neighbors(GRAPH_FIRST), []),
    ) + counts(graph, 1, 0)


def graph_self_loop_and_duplicate() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST,))
    return adds + edge_checks(graph, ((GRAPH_FIRST, GRAPH_FIRST),) * 2) + (
        ("has_edge(10,10)", graph.has_edge(GRAPH_FIRST, GRAPH_FIRST), SUCCESS_INDICATOR),
        ("get_neighbors(10)", graph.get_neighbors(GRAPH_FIRST), [GRAPH_FIRST]),
    ) + counts(graph, 1, 1)


def graph_neighbor_result_isolation() -> tuple[Check, ...]:
    graph, adds = graph_with((GRAPH_FIRST, GRAPH_SECOND, GRAPH_THIRD))
    first_edge = edge_checks(graph, ((GRAPH_FIRST, GRAPH_SECOND),))
    saved = graph.get_neighbors(GRAPH_FIRST)
    copy = graph.get_neighbors(GRAPH_FIRST)
    if isinstance(copy, list):
        copy.append(GRAPH_MISSING)
        copy.clear()
    after_copy = (
        ("get_neighbors(10) after changing copy", graph.get_neighbors(GRAPH_FIRST), [GRAPH_SECOND]),
    )
    second_edge = edge_checks(graph, ((GRAPH_FIRST, GRAPH_THIRD),))
    return adds + first_edge + after_copy + second_edge + (
        ("saved neighbours of 10", saved, [GRAPH_SECOND]),
        ("fresh neighbours of 10", graph.get_neighbors(GRAPH_FIRST), [GRAPH_SECOND, GRAPH_THIRD]),
    ) + counts(graph, 3, 2)


GRAPH_CASES: tuple[tuple[str, Scenario], ...] = (
    ("create empty", graph_create_empty),
    ("isolated vertex", graph_isolated_vertex),
    ("nonconsecutive labels and directed edge", graph_nonconsecutive_labels_and_directed_edge),
    ("duplicate vertex preserves adjacency", graph_duplicate_vertex_preserves_adjacency),
    ("duplicate edge", graph_duplicate_edge),
    ("missing endpoint without mutation", graph_missing_endpoint_without_mutation),
    ("sorted neighbours and counts", graph_sorted_neighbors_and_counts),
    ("missing-edge query", graph_missing_edge_query),
    ("neighbours of missing vertex", graph_neighbors_of_missing_vertex),
    ("self-loop and duplicate", graph_self_loop_and_duplicate),
    ("neighbour-result isolation", graph_neighbor_result_isolation),
)


@pytest.mark.parametrize(("case_name", "scenario"), TREE_NODE_CASES, ids=[name for name, _ in TREE_NODE_CASES])
def test_tree_node(case_name: str, scenario: Scenario) -> None:
    run_scenarios("TreeNode", case_name, scenario)


@pytest.mark.parametrize(("case_name", "scenario"), BINARY_TREE_CASES, ids=[name for name, _ in BINARY_TREE_CASES])
def test_binary_tree(case_name: str, scenario: Scenario) -> None:
    run_scenarios("BinaryTree", case_name, scenario)


@pytest.mark.parametrize(("case_name", "scenario"), GRAPH_CASES, ids=[name for name, _ in GRAPH_CASES])
def test_graph(case_name: str, scenario: Scenario) -> None:
    run_scenarios("Graph", case_name, scenario)
