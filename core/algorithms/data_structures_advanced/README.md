# Data Structures Advanced — Python

Implementación de la especificación [07_Data_Structures_Advanced](https://yorche3.github.io/programming_languages/core/algorithms/07_Data_Structures_Advanced/) en **Python**, usando **pytest** como framework de pruebas unitarias y una **arquitectura de librería con src-layout**.

**ES:** Este módulo implementa estructuras que requieren múltiples enlaces por nodo: una base `Node` que almacena únicamente el valor, un `TreeNode` con enlaces mutables a izquierda y derecha, un `GraphNode` con secuencia de vecinos y registro enlazado canónico, un árbol binario de búsqueda (`BinaryTree`) y un grafo dirigido (`Graph`) con registro enlazado manual de vértices e inserción ordenada de adyacencias sin delegar en colecciones de biblioteca.

**EN:** This module implements structures requiring multiple links per node: a base `Node` holding value only, a `TreeNode` with mutable left and right links, a `GraphNode` with neighbour sequence and canonical linked registry, a binary search tree (`BinaryTree`), and a directed graph (`Graph`) with a manual linked vertex registry and sorted adjacency insertion without delegating to standard library collections.

---

## 📂 Archivos y estructura / Files & Structure

| Archivo / Directory | Propósito / Purpose |
|---|---|
| [`pyproject.toml`](pyproject.toml) | Metadatos de la librería (PEP 621) + configuración de pytest y dependencias de desarrollo. / Library metadata (PEP 621) + pytest configuration and dev dependencies. |
| [`conftest.py`](conftest.py) | Añade `src/` a `sys.path` dinámicamente para ejecutar las pruebas sin instalación previa. / Adds `src/` to `sys.path` dynamically to run tests without prior installation. |
| [`src/data_structures_advanced/__init__.py`](src/data_structures_advanced/__init__.py) | Exporta `Node`, `TreeNode`, `BinaryTree` y `Graph`. / Exports `Node`, `TreeNode`, `BinaryTree`, and `Graph`. |
| [`src/data_structures_advanced/node.py`](src/data_structures_advanced/node.py) | Clase base `Node` con valor, sin enlaces ni validaciones. / Base `Node` class with value, without links or validations. |
| [`src/data_structures_advanced/tree_node.py`](src/data_structures_advanced/tree_node.py) | Nodo derivado `TreeNode` con enlaces `left` y `right` mutables. / Derived `TreeNode` node with mutable `left` and `right` links. |
| [`src/data_structures_advanced/graph_node.py`](src/data_structures_advanced/graph_node.py) | Nodo derivado `GraphNode` con secuencia de vecinos y enlace al siguiente vértice. / Derived `GraphNode` node with neighbour sequence and next vertex link. |
| [`src/data_structures_advanced/binary_tree.py`](src/data_structures_advanced/binary_tree.py) | Árbol binario de búsqueda (BST) no acotado con inserción y búsqueda `O(h)`. / Unbounded binary search tree (BST) with `O(h)` insertion and lookup. |
| [`src/data_structures_advanced/graph.py`](src/data_structures_advanced/graph.py) | Grafo dirigido con registro enlazado manual de vértices y adyacencia ordenada. / Directed graph with manual linked vertex registry and sorted adjacency. |
| [`src/data_structures_advanced/py.typed`](src/data_structures_advanced/py.typed) | Marcador de soporte de tipado estático (PEP 561). / Static typing marker (PEP 561). |
| [`tests/data_structures_advanced_tests.py`](tests/data_structures_advanced_tests.py) | Suite de pruebas unitarias parametrizadas cubriendo todas las estructuras y escenarios del contrato. / Parameterized unit test suite covering all structures and contract scenarios. |

**Estructura de directorios / Directory structure:**

```text
data_structures_advanced/
├── pyproject.toml
├── conftest.py
├── src/
│   └── data_structures_advanced/
│       ├── __init__.py
│       ├── node.py
│       ├── tree_node.py
│       ├── graph_node.py
│       ├── binary_tree.py
│       ├── graph.py
│       └── py.typed
└── tests/
    └── data_structures_advanced_tests.py
```

---

## 🛠️ Enfoque y construcción / Approach & Build

**ES:** Este proyecto adopta la **arquitectura de paquete estándar de Python** (src-layout con paquete `data_structures_advanced`), tomando como referencias de diseño las bases del lenguaje:

1. **De `data_structures_basics`:** Se adopta la organización modular por responsabilidades (cada estructura en su módulo propio dentro de `src/data_structures_advanced/`), la fachada limpia en `__init__.py`, la convención de propiedades `@property` para accesores de lectura/escritura, la resolución dinámica de `sys.path` mediante `conftest.py`, y la representación de ausencia mediante `None`.
2. **De `numbers`:** Se adopta el formato de configuración de proyecto con `pyproject.toml` (PEP 621), dependencias de desarrollo agrupadas para `pytest`, y la estructura de suite parametrizada exhaustiva.
3. **Desviación de ubicación:** La especificación sugiere `src/data_structures_advanced.ext` y `test/run_tests.ext`. En Python es idiomático modularizar las abstracciones en módulos separados (`node.py`, `tree_node.py`, `graph_node.py`, `binary_tree.py`, `graph.py`) agrupados bajo un paquete importable, y emplear `pytest` para descubrimiento y ejecución de pruebas en `tests/`.

**EN:** This project adopts Python's **standard package architecture** (src-layout with package `data_structures_advanced`), drawing from language references:

1. **From `data_structures_basics`:** Modular separation of concerns (each structure in its own module under `src/data_structures_advanced/`), a clean facade in `__init__.py`, `@property` accessor conventions, dynamic `sys.path` handling in `conftest.py`, and absence representation via `None`.
2. **From `numbers`:** Project configuration layout via `pyproject.toml` (PEP 621), grouped development dependencies for `pytest`, and a comprehensive parameterized test suite structure.
3. **Location deviation:** The specification suggests `src/data_structures_advanced.ext` and `test/run_tests.ext`. In Python, it is idiomatic to separate abstractions into individual modules (`node.py`, `tree_node.py`, `graph_node.py`, `binary_tree.py`, `graph.py`) grouped under an importable package, using `pytest` for discovery and test execution in `tests/`.

---

## 📄 Configuración clave / Key Configuration

### `pyproject.toml`

```toml
[project]
name = "data-structures-advanced"
version = "0.1.0"
description = "Node, TreeNode, GraphNode, BinaryTree and Graph, with pytest."
readme = "README.md"
authors = [
    { name = "yorche3", email = "hyaoki123@gmail.com" }
]
requires-python = ">=3.12"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[dependency-groups]
dev = [
    "pytest>=9.2.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["*_tests.py"]
```

---

## 🚀 Compilación y ejecución / Build & Run

```bash
# Verificación estática / Static check
python3 -W error -m py_compile src/data_structures_advanced/*.py tests/*.py conftest.py

# Ejecución de pruebas / Run tests
pytest -v
```

**Salida real / Actual output:**

```text
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: ~/programming_languages/python/core/algorithms/data_structures_advanced
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.15.1
collecting ... collected 23 items

tests/data_structures_advanced_tests.py::test_tree_node[create a tree node] PASSED [  4%]
tests/data_structures_advanced_tests.py::test_tree_node[absent initial links] PASSED [  8%]
tests/data_structures_advanced_tests.py::test_tree_node[link two children] PASSED [ 13%]
tests/data_structures_advanced_tests.py::test_tree_node[traverse each link] PASSED [ 17%]
tests/data_structures_advanced_tests.py::test_tree_node[unlink children] PASSED [ 21%]
tests/data_structures_advanced_tests.py::test_binary_tree[create empty] PASSED [ 26%]
tests/data_structures_advanced_tests.py::test_binary_tree[insert the root] PASSED [ 30%]
tests/data_structures_advanced_tests.py::test_binary_tree[insert lower and higher] PASSED [ 34%]
tests/data_structures_advanced_tests.py::test_binary_tree[multilevel branches] PASSED [ 39%]
tests/data_structures_advanced_tests.py::test_binary_tree[missing value in nonempty tree] PASSED [ 43%]
tests/data_structures_advanced_tests.py::test_binary_tree[idempotent duplicate] PASSED [ 47%]
tests/data_structures_advanced_tests.py::test_binary_tree[ordered insertions] PASSED [ 52%]
tests/data_structures_advanced_tests.py::test_graph[create empty] PASSED [ 56%]
tests/data_structures_advanced_tests.py::test_graph[isolated vertex] PASSED [ 60%]
tests/data_structures_advanced_tests.py::test_graph[nonconsecutive labels and directed edge] PASSED [ 65%]
tests/data_structures_advanced_tests.py::test_graph[duplicate vertex preserves adjacency] PASSED [ 69%]
tests/data_structures_advanced_tests.py::test_graph[duplicate edge] PASSED [ 73%]
tests/data_structures_advanced_tests.py::test_graph[missing endpoint without mutation] PASSED [ 78%]
tests/data_structures_advanced_tests.py::test_graph[sorted neighbours and counts] PASSED [ 82%]
tests/data_structures_advanced_tests.py::test_graph[missing-edge query] PASSED [ 86%]
tests/data_structures_advanced_tests.py::test_graph[neighbours of missing vertex] PASSED [ 91%]
tests/data_structures_advanced_tests.py::test_graph[self-loop and duplicate] PASSED [ 95%]
tests/data_structures_advanced_tests.py::test_graph[neighbour-result isolation] PASSED [100%]

============================== 23 passed in 0.02s ==============================
```

---

## 🧠 Algoritmos y operaciones / Algorithms & Operations

### `Node`

| Operación / Operation | Entrada → salida / Input → output | Complejidad / Complexity | Notas / Notes |
|---|---|---|---|
| `Node(value)` | `int → Node` | $O(1)$ | Constructor (`__init__`); almacena valor base sin enlaces ni validaciones. / Constructor (`__init__`); stores base value without links or validations. |
| `node.value` | `→ int` | $O(1)$ | Propiedad observadora (`get_value`). / Observer property (`get_value`). |

### `TreeNode`

| Operación / Operation | Entrada → salida / Input → output | Complejidad / Complexity | Notas / Notes |
|---|---|---|---|
| `TreeNode(value)` | `int → TreeNode` | $O(1)$ | Constructor (`__init__`); invoca `super()`, inicializa enlaces izquierdo y derecho a `None`. / Constructor (`__init__`); calls `super()`, initializes left and right links to `None`. |
| `node.value` | `→ int` | $O(1)$ | Propiedad observadora heredada de `Node`. / Observer property inherited from `Node`. |
| `node.left` | `→ TreeNode \| None` | $O(1)$ | Propiedad observadora (`get_left`); `None` si ausente. / Observer property (`get_left`); `None` when absent. |
| `node.left = other` | `TreeNode \| None → None` | $O(1)$ | Mutador de enlace izquierdo (`set_left`). / Mutator for left link (`set_left`). |
| `node.right` | `→ TreeNode \| None` | $O(1)$ | Propiedad observadora (`get_right`); `None` si ausente. / Observer property (`get_right`); `None` when absent. |
| `node.right = other` | `TreeNode \| None → None` | $O(1)$ | Mutador de enlace derecho (`set_right`). / Mutator for right link (`set_right`). |

### `BinaryTree`

| Operación / Operation | Entrada → salida / Input → output | Complejidad / Complexity | Notas / Notes |
|---|---|---|---|
| `BinaryTree()` | `→ BinaryTree` | $O(1)$ | Constructor (`__init__`); raíz `None`, contador `0`. / Constructor (`__init__`); root `None`, count `0`. |
| `tree.insert(value)` | `int → bool` | $O(h)$ | Inserta valor preservando invariante ABB. Los duplicados retornan `True` sin incrementar tamaño. / Inserts value preserving BST invariant. Duplicates return `True` without increasing size. |
| `tree.contains(value)` | `int → bool` | $O(h)$ | Búsqueda binaria por invariante ABB; `True` si existe, `False` si ausente. / Binary search following BST invariant; `True` if present, `False` if absent. |
| `tree.is_empty()` | `→ bool` | $O(1)$ | Comprueba si el árbol no tiene nodos (`count == 0`). / Checks whether tree has no nodes (`count == 0`). |
| `tree.size()` | `→ int` | $O(1)$ | Retorna el número de nodos únicos. / Returns count of unique nodes. |

### `GraphNode`

| Operación / Operation | Entrada → salida / Input → output | Complejidad / Complexity | Notas / Notes |
|---|---|---|---|
| `GraphNode(label)` | `int → GraphNode` | $O(1)$ | Constructor interno a `Graph`; inicializa etiqueta, secuencia de vecinos vacía y `next_vertex = None`. / Internal constructor for `Graph`; initializes label, empty neighbour sequence, and `next_vertex = None`. |
| `node.value` | `→ int` | $O(1)$ | Etiqueta del vértice heredada de `Node`. / Vertex label inherited from `Node`. |
| `node.neighbors` | `→ list[int]` | $O(1)$ | Secuencia de etiquetas de vecinos ordenados. / Sequence of sorted neighbour labels. |
| `node.next_vertex` | `→ GraphNode \| None` | $O(1)$ | Enlace al siguiente vértice en el registro canónico. / Link to next vertex in canonical registry. |
| `node.next_vertex = other` | `GraphNode \| None → None` | $O(1)$ | Mutador de enlace en registro de vértices. / Mutator for link in vertex registry. |

### `Graph`

| Operación / Operation | Entrada → salida / Input → output | Complejidad / Complexity | Notas / Notes |
|---|---|---|---|
| `Graph()` | `→ Graph` | $O(1)$ | Constructor (`__init__`); 0 vértices, 0 aristas, registro enlazado vacío. / Constructor (`__init__`); 0 vertices, 0 edges, empty linked registry. |
| `graph.add_vertex(label)` | `int → bool` | $O(V)$ | Registra un vértice si no existía; duplicado retorna `True` sin reiniciar vecinos. / Registers vertex if not present; duplicate returns `True` without resetting neighbours. |
| `graph.add_edge(u, v)` | `int, int → bool` | $O(V + d(u))$ | Añade arista dirigida de `u` a `v` en orden ascendente; falla (`False`) si falta `u` o `v`. Bucles permitidos; duplicados idempotentes. / Adds directed edge from `u` to `v` in sorted order; fails (`False`) if `u` or `v` is missing. Self-loops allowed; duplicates idempotent. |
| `graph.has_edge(u, v)` | `int, int → bool` | $O(V + d(u))$ | Comprueba existencia de arista; `False` si ausente o falta algún extremo. / Checks edge existence; `False` if absent or either endpoint missing. |
| `graph.get_neighbors(u)` | `int → list[int] \| None` | $O(V + d(u))$ | Retorna copia independiente de vecinos ordenados de `u`; `None` si `u` no existe, `[]` si está aislado. / Returns independent copy of sorted neighbours of `u`; `None` if `u` missing, `[]` if isolated. |
| `graph.is_empty()` | `→ bool` | $O(1)$ | Comprueba si el grafo no tiene vértices (`vertex_count == 0`). / Checks whether graph has no vertices (`vertex_count == 0`). |
| `graph.vertex_count()` | `→ int` | $O(1)$ | Retorna el número de vértices registrados. / Returns count of registered vertices. |
| `graph.edge_count()` | `→ int` | $O(1)$ | Retorna el número total de aristas dirigidas. / Returns count of directed edges. |

---

## 🧩 Decisiones de diseño / Design decisions

| Decisión / Decision | Alternativa considerada / Alternative | Razón / Reason |
|---|---|---|
| Herencia explícita de `Node` en `TreeNode` y `GraphNode` | Composición con valor embebido | Python ofrece soporte nativo de herencia de clases; modela limpiamente la relación "es un nodo con valor" compartiendo la propiedad `value` sin sobrecarga de indirección. / Python offers native class inheritance; cleanly models the "is a node with value" relationship sharing the `value` property without indirection overhead. |
| Registro de vértices como lista enlazada simple interna | Diccionario `dict[int, GraphNode]` o conjunto | Cumple estrictamente el contrato educativo de búsqueda $O(V)$ manual sin delegar el registro en estructuras indexadas de la biblioteca estándar. / Strictly adheres to the educational contract of manual $O(V)$ lookup without delegating the registry to standard-library indexed structures. |
| Inserción ordenada manual en adyacencia de vecinos | Uso de `bisect.insort` o re-ordenación con `.sort()` | La especificación autoriza almacenamiento nativo pero exige implementar búsqueda, deduplicación e inserción ordenada manualmente para preservar la complejidad $O(d(u))$ y determinismo. / The specification authorizes native storage but requires implementing search, deduplication, and sorted insertion manually to preserve $O(d(u))$ complexity and determinism. |
| Copia defensiva en `get_neighbors(u)` | Retornar referencia a lista interna | Garantiza el aislamiento frente a mutaciones externas en la lista devuelta, satisfaciendo el requerimiento de que consultas no alteren el grafo ni viceversa. / Guarantees isolation from external mutations on the returned list, fulfilling the requirement that queries do not alter the graph nor vice versa. |

---

## 🔀 Adaptaciones idiomáticas / Idiomatic adaptations

| Especificación / Specification | Adaptación / Adaptation | Justificación / Justification |
|---|---|---|
| `Node.init(value)` y `TreeNode.init(value)` | Constructores `__init__` | En Python los objetos se inicializan idiomáticamente al crearse mediante `__init__`. / In Python objects are idiomatically initialized upon creation via `__init__`. |
| `get_value()`, `get_left()`, `get_right()`, `set_left()`, `set_right()` | `@property` y `@setter` | Interfaz pythónica idiomática para lectura y mutación de atributos preservando encapsulamiento. / Idiomatic Pythonic interface for attribute access and mutation preserving encapsulation. |
| `Graph.get_neighbors(u)` en fallo | Retorna `None` | Representación idiomática y no ambigua de ausencia en Python frente a `[]` (vértice existente aislado). / Idiomatic and unambiguous representation of absence in Python distinct from `[]` (existing isolated vertex). |
| Caso inmutable de `TreeNode` | Omitido | Python implementa clases mutables estándar; la especificación declara este caso como condicional («si aplica»). / Python implements standard mutable classes; the specification designates this case as conditional ("if applicable"). |
| Ubicación esperada `src/data_structures_advanced.ext` | `src/data_structures_advanced/*.py` | Separación por responsabilidades (un archivo por ADT) con re-exportación centralizada en `__init__.py`. / Separation of concerns (one file per ADT) with centralized re-exports in `__init__.py`. |
| Ubicación esperada `test/run_tests.ext` | `tests/data_structures_advanced_tests.py` con `pytest` | pytest proporciona descubrimiento automático y runner integrado estándar en el ecosistema. / pytest provides automated discovery and standard integrated runner in the ecosystem. |

---

## 🚨 Indicadores de fallo / Failure indicators

| Operación / Operation | Situación de fallo / Failure situation | Indicador / Indicator | Ejemplo / Example |
|---|---|---|---|
| `node.left` / `node.right` | Enlace ausente | `None` | `TreeNode(10).left` → `None` |
| `binary_tree.contains(value)` | Valor ausente en el árbol | `False` | `BinaryTree().contains(50)` → `False` |
| `graph.add_edge(u, v)` | Extremo `u` o `v` inexistente | `False` | `Graph().add_edge(10, 99)` → `False` |
| `graph.has_edge(u, v)` | Arista ausente o extremos inexistentes | `False` | `Graph().has_edge(10, 30)` → `False` |
| `graph.get_neighbors(u)` | Vértice `u` inexistente en el grafo | `None` | `Graph().get_neighbors(99)` → `None` |

---

## ✅ Cobertura de pruebas / Test coverage

**ES:** Mapeo de casos: `unidad/variante → casos aplicables → grupo lógico → archivo/suite → runner`:
- `TreeNode` → 5 casos aplicables (1 omitido por mutabilidad nativa) → grupo lógico `test_tree_node` → `tests/data_structures_advanced_tests.py` → `pytest`.
- `BinaryTree` → 7 casos aplicables → grupo lógico `test_binary_tree` → `tests/data_structures_advanced_tests.py` → `pytest`.
- `Graph` → 11 casos aplicables → grupo lógico `test_graph` → `tests/data_structures_advanced_tests.py` → `pytest`.

### `TreeNode`

| Caso de la especificación / Specification case | Cubierto / Covered | Prueba / Test | Notas / Notes |
|---|---|:--:|---|
| Crear un nodo de árbol / Create a tree node | Sí | `tests/data_structures_advanced_tests.py:78-80` | Verifica `value == 10`. / Verifies `value == 10`. |
| Enlaces iniciales ausentes / Absent initial links | Sí | `tests/data_structures_advanced_tests.py:83-88` | Verifica `left is None` y `right is None`. / Verifies `left is None` and `right is None`. |
| Enlazar dos hijos / Link two children | Sí | `tests/data_structures_advanced_tests.py:91-98` | Enlaza hijos 20 y 30; verifica sus valores desde el padre. / Links children 20 and 30; checks their values from parent. |
| Recorrer cada enlace / Traverse each link | Sí | `tests/data_structures_advanced_tests.py:101-114` | Sigue enlaces y verifica hojas con enlaces ausentes. / Traverses links and verifies leaf nodes have absent links. |
| Desenlazar hijos / Unlink children | Sí | `tests/data_structures_advanced_tests.py:117-133` | Desasigna enlaces izquierdo y derecho individualmente preservando valores. / Unlinks left and right links individually preserving values. |
| Adaptación inmutable (si aplica) / Immutable adaptation (if applicable) | Omitido | N/A | No aplica en Python: `TreeNode` es mutable. / Not applicable in Python: `TreeNode` is mutable. |

### `BinaryTree`

| Caso de la especificación / Specification case | Cubierto / Covered | Prueba / Test | Notas / Notes |
|---|---|:--:|---|
| Crear vacío / Create empty | Sí | `tests/data_structures_advanced_tests.py:145-151` | Verifica `is_empty() == True`, `size() == 0`, `contains(50) == False`. / Checks `is_empty() == True`, `size() == 0`, `contains(50) == False`. |
| Insertar la raíz / Insert the root | Sí | `tests/data_structures_advanced_tests.py:154-161` | Inserta 50; verifica tamaño 1, no vacío y pertenencia. / Inserts 50; checks size 1, not empty, and membership. |
| Insertar menor y mayor / Insert lower and higher | Sí | `tests/data_structures_advanced_tests.py:164-167` | Inserta 50, 30, 70; verifica tamaño 3 y pertenencia de todos. / Inserts 50, 30, 70; checks size 3 and membership of all. |
| Ramas de varios niveles / Multilevel branches | Sí | `tests/data_structures_advanced_tests.py:170-173` | Inserta 50, 30, 70, 20, 40; verifica tamaño 5 y pertenencia. / Inserts 50, 30, 70, 20, 40; checks size 5 and membership. |
| Valor ausente en árbol no vacío / Missing value in nonempty tree | Sí | `tests/data_structures_advanced_tests.py:176-183` | Verifica que `contains(99)` falla sin alterar tamaño ni pertenencia de 50. / Checks `contains(99)` fails without altering size or 50 presence. |
| Duplicado idempotente / Idempotent duplicate | Sí | `tests/data_structures_advanced_tests.py:186-189` | Inserta 50, 30, 70, 30; verifica tamaño 3 y preservación de valores. / Inserts 50, 30, 70, 30; checks size 3 and preservation of values. |
| Inserciones ordenadas / Ordered insertions | Sí | `tests/data_structures_advanced_tests.py:192-198` | Inserta 20, 30, 40, 50, 70; verifica tamaño 5, presencia y fallo de 99. / Inserts 20, 30, 40, 50, 70; checks size 5, presence, and 99 failure. |

### `Graph`

| Caso de la especificación / Specification case | Cubierto / Covered | Prueba / Test | Notas / Notes |
|---|---|:--:|---|
| Crear vacío / Create empty | Sí | `tests/data_structures_advanced_tests.py:212-220` | Verifica `is_empty() == True`, contadores 0, fallos en `has_edge` y `get_neighbors`. / Checks `is_empty() == True`, 0 counts, failures on `has_edge` and `get_neighbors`. |
| Vértice aislado / Isolated vertex | Sí | `tests/data_structures_advanced_tests.py:223-229` | Registra 10; verifica 1 vértice, 0 aristas y vecinos `[]`. / Registers 10; checks 1 vertex, 0 edges, and neighbours `[]`. |
| Etiquetas no consecutivas y arista dirigida / Nonconsecutive labels and directed edge | Sí | `tests/data_structures_advanced_tests.py:232-237` | Registra 10 y 70, arista (10, 70); verifica dirección de arista y contadores. / Registers 10 and 70, edge (10, 70); checks edge direction and counts. |
| Vértice duplicado conserva adyacencia / Duplicate vertex preserves adjacency | Sí | `tests/data_structures_advanced_tests.py:240-246` | Re-añade vértice 10 tras arista (10, 30); preserva vecinos `[30]`. / Re-adds vertex 10 after edge (10, 30); preserves neighbours `[30]`. |
| Arista duplicada / Duplicate edge | Sí | `tests/data_structures_advanced_tests.py:249-253` | Añade arista (10, 30) dos veces; verifica contadores 2 vértices y 1 arista. / Adds edge (10, 30) twice; checks counts 2 vertices and 1 edge. |
| Extremo inexistente sin mutación / Missing endpoint without mutation | Sí | `tests/data_structures_advanced_tests.py:256-277` | Intenta aristas con vértices inexistentes (98, 99); verifica fallos y no mutación. / Attempts edges with missing vertices (98, 99); checks failure and no mutation. |
| Vecinos ordenados y contadores / Sorted neighbours and counts | Sí | `tests/data_structures_advanced_tests.py:280-290` | Añade aristas desordenadas a 10; verifica vecinos ordenados `[30, 50, 70]`. / Adds unordered edges to 10; checks sorted neighbours `[30, 50, 70]`. |
| Consulta de arista ausente / Missing-edge query | Sí | `tests/data_structures_advanced_tests.py:293-297` | Verifica `has_edge(10, 30) == False` en vértices sin arista. / Checks `has_edge(10, 30) == False` on vertices without edge. |
| Vecinos de vértice inexistente / Neighbours of missing vertex | Sí | `tests/data_structures_advanced_tests.py:300-305` | Verifica que `get_neighbors(99)` retorna `None`, distinguiéndose de `[]`. / Checks `get_neighbors(99)` returns `None`, distinct from `[]`. |
| Bucle y duplicado / Self-loop and duplicate | Sí | `tests/data_structures_advanced_tests.py:308-313` | Añade bucle (10, 10) dos veces; verifica `has_edge`, vecinos `[10]` y 1 arista. / Adds self-loop (10, 10) twice; checks `has_edge`, neighbours `[10]`, and 1 edge. |
| Aislamiento del resultado de vecinos / Neighbour-result isolation | Sí | `tests/data_structures_advanced_tests.py:316-330` | Modifica copia devuelta y añade arista posterior; verifica aislamiento. / Modifies returned copy and adds later edge; checks isolation. |

---

## ⚠️ Limitaciones conocidas / Known limitations

Ninguna / None

**ES:** Las estructuras no imponen límites artificiales de capacidad ni cotas de vértices o aristas preasignadas. Operan dentro de la memoria disponible respetando todas las cotas de complejidad $O(1)$, $O(h)$ y $O(V + d(u))$ del contrato.

**EN:** The structures impose no artificial capacity limits or preallocated vertex/edge bounds. They operate within available memory while respecting all contract complexity bounds $O(1)$, $O(h)$, and $O(V + d(u))$.

---

## 📝 Notas de implementación / Implementation Notes

**ES:**

- **Herencia del valor base:** `Node` encapsula exclusivamente `_value` y la propiedad `value`. `TreeNode` y `GraphNode` llaman a `super().__init__(...)` sin duplicar la gestión del valor.
- **Invariante de búsqueda en el ABB:** Las operaciones de inserción y búsqueda se implementan de forma iterativa, garantizando que el árbol no sufra desbordamiento de pila en estructuras profundas.
- **Registro canónico de vértices:** El grafo mantiene una lista enlazada simple interna cuyos nodos son las propias instancias de `GraphNode`, enlazadas mediante `next_vertex`. `_find_vertex` recorre este registro en $O(V)$ sin recurrir a diccionarios o tablas hash.
- **Invariante de adyacencia ordenada:** En `add_edge(u, v)`, se determina la posición de inserción de forma lineal en la secuencia interna de vecinos, garantizando orden ascendente y deduplicación con complejidad $O(d(u))$ sin invocar funciones de ordenamiento de la biblioteca estándar.
- **Distinción entre ausencia y vacío:** `get_neighbors(u)` retorna `None` como indicador de que el vértice `u` no existe en el grafo, mientras que retorna `[]` cuando `u` existe y es un vértice aislado sin aristas salientes.
- **Aislamiento defensivo:** `get_neighbors(u)` devuelve una copia independiente (`list(...)`), impidiendo que manipulaciones sobre la lista devuelta afecten el estado interno del grafo.

**EN:**

- **Base value inheritance:** `Node` exclusively encapsulates `_value` and the `value` property. `TreeNode` and `GraphNode` invoke `super().__init__(...)` without duplicating value handling.
- **BST search invariant:** Insertion and lookup operations are implemented iteratively, ensuring the tree does not encounter recursion stack overflows on deep trees.
- **Canonical vertex registry:** The graph maintains an internal singly linked list whose nodes are the `GraphNode` instances themselves, linked via `next_vertex`. `_find_vertex` traverses this registry in $O(V)$ without relying on dictionaries or hash tables.
- **Sorted adjacency invariant:** In `add_edge(u, v)`, the insertion position is determined linearly within the internal neighbour sequence, ensuring ascending order and deduplication in $O(d(u))$ complexity without calling standard-library sorting functions.
- **Distinction between absence and empty:** `get_neighbors(u)` returns `None` to indicate that vertex `u` does not exist in the graph, whereas it returns `[]` when `u` exists as an isolated vertex without outgoing edges.
- **Defensive isolation:** `get_neighbors(u)` returns an independent copy (`list(...)`), preventing modifications on the returned list from affecting the graph's internal state.

**ES:** Este proyecto también está implementado en otros lenguajes. Explora el repositorio principal para consultar las demás versiones.

**EN:** This project is also implemented in other languages. Explore the main repository to see the other versions.

---

## 🔍 Checklist de validación / Validation checklist

- [x] La suite nativa se ejecutó y su salida real está copiada en este README.
- [x] Cada caso de la especificación tiene su fila en _Cobertura de pruebas_ (o `Omitido` con razón).
- [x] Cada desviación del pseudocódigo o de la ubicación esperada está en _Adaptaciones idiomáticas_.
- [x] Cada operación con fallo posible está en _Indicadores de fallo_.
- [x] No hay rutas absolutas del autor, credenciales ni salidas inventadas.
- [x] Los enlaces relativos resuelven dentro del repositorio y el documento es bilingüe.
- [x] Ninguna sección repite lo que ya dice la especificación.

---

## 📚 Referencias / References

| Tipo / Kind | Referencia / Reference |
|---|---|
| Especificación / Specification | [`07_Data_Structures_Advanced.md`](https://yorche3.github.io/programming_languages/core/algorithms/07_Data_Structures_Advanced/) |
| Primera base del lenguaje / First language reference | `data_structures_basics` — [`../data_structures_basics/`](../data_structures_basics/) |
| Segunda base del lenguaje / Second language reference | `numbers` — [`../../foundations/numbers/`](../../foundations/numbers/) |
| Guía de inicialización / Initialisation guide | [`core/00_Project_Initialization_Guide.md`](https://yorche3.github.io/programming_languages/core/00_Project_Initialization_Guide/) |
| Adaptaciones idiomáticas / Idiomatic adaptations | [`AGENT_Template.md`](https://yorche3.github.io/programming_languages/docs/AGENT_Template/) |
| Validación de la documentación / Documentation validation | [`WORKFLOW.md`](https://yorche3.github.io/programming_languages/docs/WORKFLOW/) |
| Documentación oficial del lenguaje / Language official docs | [Python Documentation — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) |

---

*[← Volver a 06_Data_Structures_Basics](../data_structures_basics/) | [↑ Volver a inicio / Back to home](https://yorche3.github.io/programming_languages/)*
