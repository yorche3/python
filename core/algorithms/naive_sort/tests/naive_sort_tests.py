# Casos de prueba de la especificación 05_Naive_Sort.md
#
# Caso nulo incluido: en Python una lista puede ser `None`, así que el
# indicador de fallo del contrato es `None`, distinguible del caso vacío. No se
# espera ninguna excepción.
#
# Aislamiento: las listas de Python son mutables y los tres algoritmos ordenan
# in-place, así que cada caso ordena una copia del fixture compartido.

from naive_sort import bubble_sort, insertion_sort, selection_sort

STANDARD_INPUT = [5, 2, 9, 1, 5, 6]
STANDARD_OUTPUT = [1, 2, 5, 5, 6, 9]

SORTED_INPUT = [1, 2, 3, 4, 5]
SORTED_OUTPUT = [1, 2, 3, 4, 5]

REVERSE_INPUT = [5, 4, 3, 2, 1]
REVERSE_OUTPUT = [1, 2, 3, 4, 5]

IDENTICAL_INPUT = [7, 7, 7, 7]
IDENTICAL_OUTPUT = [7, 7, 7, 7]

NEGATIVE_INPUT = [3, -1, 4, -5, 0]
NEGATIVE_OUTPUT = [-5, -1, 0, 3, 4]

SINGLE_INPUT = [42]
SINGLE_OUTPUT = [42]

EMPTY_INPUT = []
EMPTY_OUTPUT = []

NULL_INPUT = None
NULL_OUTPUT = None

CASES = [
    {
        "description": "an unsorted array",
        "input": STANDARD_INPUT,
        "expected": STANDARD_OUTPUT,
    },
    {
        "description": "an already sorted array",
        "input": SORTED_INPUT,
        "expected": SORTED_OUTPUT,
    },
    {
        "description": "a reverse ordered array",
        "input": REVERSE_INPUT,
        "expected": REVERSE_OUTPUT,
    },
    {
        "description": "an array of identical elements",
        "input": IDENTICAL_INPUT,
        "expected": IDENTICAL_OUTPUT,
    },
    {
        "description": "an array with negative numbers",
        "input": NEGATIVE_INPUT,
        "expected": NEGATIVE_OUTPUT,
    },
    {
        "description": "a single element array",
        "input": SINGLE_INPUT,
        "expected": SINGLE_OUTPUT,
    },
    {
        "description": "an empty array",
        "input": EMPTY_INPUT,
        "expected": EMPTY_OUTPUT,
    },
    {
        "description": "a null input",
        "input": NULL_INPUT,
        "expected": NULL_OUTPUT,
    },
]

# Helper compartido: recibe la función a probar y el nombre del algoritmo, y
# ejecuta todos los casos con un mensaje descriptivo cada uno.
def assert_sorts_all_cases(sort, algorithm):
    for case in CASES:
        source = case["input"]
        actual = sort(None if source is None else list(source))
        assert actual == case["expected"], (
            f"{algorithm} should sort {case['description']}"
        )

def test_selection_sort():
    assert_sorts_all_cases(selection_sort, "selection_sort")

def test_bubble_sort():
    assert_sorts_all_cases(bubble_sort, "bubble_sort")

def test_insertion_sort():
    assert_sorts_all_cases(insertion_sort, "insertion_sort")
