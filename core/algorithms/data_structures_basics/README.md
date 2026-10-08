# Data Structures Basics — Python

Implementación de la especificación [06_Data_Structures_Basics](https://yorche3.github.io/programming_languages/core/algorithms/06_Data_Structures_Basics/) en **Python**, usando **pytest** como framework de pruebas unitarias y una **arquitectura de librería con src-layout**.

**ES:** Cuatro estructuras construidas a mano sobre un único tipo `Node`: `Node`, `LinkedList`, `Stack` y `Queue`. Cada ADT gestiona directamente sus punteros y contador; `Stack` y `Queue` no delegan en `LinkedList` ni en tipos de colección de la biblioteca estándar.

**EN:** Four structures built by hand over a single `Node` type: `Node`, `LinkedList`, `Stack` and `Queue`. Each ADT directly manages its pointers and count; `Stack` and `Queue` do not delegate to `LinkedList` or standard-library collection types.

---

## 📂 Archivos y estructura / Files & Structure

| Archivo / Directory | Propósito / Purpose |
|---|---|
| [`pyproject.toml`](pyproject.toml) | Metadatos de la librería (PEP 621) + configuración de pytest. / Library metadata (PEP 621) + pytest configuration. |
| [`conftest.py`](conftest.py) | Añade `src/` a `sys.path` para importar sin instalación previa. / Adds `src/` to `sys.path` to import without prior installation. |
| [`src/data_structures_basics/__init__.py`](src/data_structures_basics/__init__.py) | Exporta `Node`, `LinkedList`, `Stack` y `Queue`. / Exports `Node`, `LinkedList`, `Stack`, and `Queue`. |
| [`src/data_structures_basics/node.py`](src/data_structures_basics/node.py) | Celda enlazada compartida — valor y puntero al siguiente. / Shared linked cell — value and pointer to next. |
| [`src/data_structures_basics/linked_list.py`](src/data_structures_basics/linked_list.py) | Lista simplemente enlazada con `head`, `tail` y contador. / Singly linked list with `head`, `tail`, and count. |
| [`src/data_structures_basics/stack.py`](src/data_structures_basics/stack.py) | Pila LIFO independiente sobre `Node` con `top` y contador. / Independent LIFO stack over `Node` with `top` and count. |
| [`src/data_structures_basics/queue.py`](src/data_structures_basics/queue.py) | Cola FIFO independiente sobre `Node` con `front`, `rear` y contador. / Independent FIFO queue over `Node` with `front`, `rear`, and count. |
| [`src/data_structures_basics/py.typed`](src/data_structures_basics/py.typed) | Marcador de soporte de tipado estático (PEP 561). / Static typing marker (PEP 561). |
| [`tests/data_structures_basics_tests.py`](tests/data_structures_basics_tests.py) | Suite de pruebas unitarias sobre las cuatro estructuras. / Unit test suite covering all four data structures. |

**Estructura de directorios / Directory structure:**

```text
data_structures_basics/
├── pyproject.toml
├── conftest.py
├── src/
│   └── data_structures_basics/
│       ├── __init__.py
│       ├── node.py
│       ├── linked_list.py
│       ├── stack.py
│       ├── queue.py
│       └── py.typed
└── tests/
    └── data_structures_basics_tests.py
```

---

## 🛠️ Enfoque y construcción / Approach & Build

**ES:** Este proyecto usa una **arquitectura de paquete estándar de Python** (src-layout con paquete `data_structures_basics`):

1. **`pyproject.toml`** (PEP 621) declara el paquete `data-structures-basics` con backend de construcción `hatchling`.
2. **pytest** se configura en el mismo `pyproject.toml` (`testpaths = ["tests"]`, `python_files = ["*_tests.py"]`).
3. **`conftest.py`** añade `src/` a `sys.path` dinámicamente para ejecutar las pruebas directamente sin requerir instalación previa.
4. Cada estructura se implementa como una clase autónoma en su propio módulo, agrupadas bajo el paquete `data_structures_basics`.

**EN:** This project uses a **standard Python package architecture** (src-layout with package `data_structures_basics`):

1. **`pyproject.toml`** (PEP 621) declares the `data-structures-basics` package using the `hatchling` build backend.
2. **pytest** is configured in the same `pyproject.toml` (`testpaths = ["tests"]`, `python_files = ["*_tests.py"]`).
3. **`conftest.py`** dynamically adds `src/` to `sys.path` to execute tests directly without requiring prior installation.
4. Each structure is implemented as an autonomous class in its own module, grouped under the `data_structures_basics` package.

---

## 📄 Configuración clave / Key Configuration

### `pyproject.toml`

```toml
[project]
name = "data-structures-basics"
version = "0.1.0"
description = "Node, LinkedList, Stack and Queue over a shared linked node, with pytest."
readme = "README.md"
authors = [
    { name = "yorche3", email = "hyaoki123@gmail.com" }
]
requires-python = ">=3.12"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["*_tests.py"]
```

---

## 🚀 Compilación y ejecución / Build & Run

```bash
# Verificación estática / Static check
python3 -W error -m py_compile src/data_structures_basics/*.py tests/*.py conftest.py

# Ejecución de pruebas / Run tests
pytest -v
```

**Salida real / Actual output:**

```text
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: ~/programming_languages/python/core/algorithms/data_structures_basics
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.15.1
collecting ... collected 4 items

tests/data_structures_basics_tests.py::test_node PASSED                  [ 25%]
tests/data_structures_basics_tests.py::test_linked_list PASSED           [ 50%]
tests/data_structures_basics_tests.py::test_stack PASSED                 [ 75%]
tests/data_structures_basics_tests.py::test_queue PASSED                 [100%]

============================== 4 passed in 0.01s ===============================
```

---

## 🧠 Algoritmos y operaciones / Algorithms & Operations

### `Node`

| Operación / Operation | Entrada → salida / Input → output | Complejidad / Complexity | Notas / Notes |
|---|---|---|---|
| `Node(value, next_node=None)` | `int, Node \| None → Node` | $O(1)$ | Constructor (`init`); asigna valor y enlace siguiente. / Constructor (`init`); assigns value and next link. |
| `node.value` | `→ int` | $O(1)$ | Propiedad observadora (`get_value`). / Observer property (`get_value`). |
| `node.next` | `→ Node \| None` | $O(1)$ | Propiedad observadora (`get_next`); `None` si ausente. / Observer property (`get_next`); `None` when absent. |
| `node.next = other` | `Node \| None → None` | $O(1)$ | Setter del enlace (`set_next`). / Setter for next link (`set_next`). |

### `LinkedList`

| Operación / Operation | Entrada → salida / Input → output | Complejidad / Complexity | Notas / Notes |
|---|---|---|---|
| `LinkedList()` | `→ LinkedList` | $O(1)$ | Constructor (`init`); cabeza/cola `None`, contador `0`. / Constructor (`init`); head/tail `None`, count `0`. |
| `list.head` | `→ int` | $O(1)$ | Propiedad observadora (`get_head`); `-1` si vacía. / Observer property (`get_head`); `-1` if empty. |
| `list.head_node` | `→ Node \| None` | $O(1)$ | Propiedad para recorrido (`get_next`); `None` si vacía. / Property for traversal (`get_next`); `None` if empty. |
| `list.insert_head(value)` | `int → None` | $O(1)$ | Inserta nodo al inicio; actualiza cabeza y cola. / Inserts node at head; updates head and tail. |
| `list.insert_tail(value)` | `int → None` | $O(1)$ | Inserta nodo al final; actualiza cola y cabeza. / Inserts node at tail; updates tail and head. |
| `list.delete(value)` | `int → bool` | $O(n)$ | Elimina primera aparición; `True` en éxito, `False` si ausente. / Deletes first occurrence; `True` on success, `False` if absent. |
| `list.is_empty()` | `→ bool` | $O(1)$ | Comprueba si el tamaño es `0`. / Checks if size is `0`. |
| `list.size()` | `→ int` | $O(1)$ | Retorna el número de nodos. / Returns node count. |

### `Stack`

| Operación / Operation | Entrada → salida / Input → output | Complejidad / Complexity | Notas / Notes |
|---|---|---|---|
| `Stack()` | `→ Stack` | $O(1)$ | Constructor (`init`); tope `None`, contador `0`. / Constructor (`init`); top `None`, count `0`. |
| `stack.push(value)` | `int → None` | $O(1)$ | Apila un nuevo nodo sobre el tope. / Pushes new node onto top. |
| `stack.pop()` | `→ int` | $O(1)$ | Desapila y retorna tope; `-1` si vacía. / Pops and returns top; `-1` if empty. |
| `stack.peek()` | `→ int` | $O(1)$ | Observa el tope sin desapilar; `-1` si vacía. / Observes top without popping; `-1` if empty. |
| `stack.is_empty()` | `→ bool` | $O(1)$ | Comprueba si la pila está vacía. / Checks if stack is empty. |
| `stack.size()` | `→ int` | $O(1)$ | Retorna el número de elementos. / Returns element count. |

### `Queue`

| Operación / Operation | Entrada → salida / Input → output | Complejidad / Complexity | Notas / Notes |
|---|---|---|---|
| `Queue()` | `→ Queue` | $O(1)$ | Constructor (`init`); frente/final `None`, contador `0`. / Constructor (`init`); front/rear `None`, count `0`. |
| `queue.enqueue(value)` | `int → None` | $O(1)$ | Encola nuevo nodo por el final. / Enqueues new node at rear. |
| `queue.dequeue()` | `→ int` | $O(1)$ | Desencola y retorna el frente; `-1` si vacía. / Dequeues and returns front; `-1` if empty. |
| `queue.peek()` | `→ int` | $O(1)$ | Observa el frente sin desencolar; `-1` si vacía. / Observes front without dequeueing; `-1` if empty. |
| `queue.is_empty()` | `→ bool` | $O(1)$ | Comprueba si la cola está vacía. / Checks if queue is empty. |
| `queue.size()` | `→ int` | $O(1)$ | Retorna el número de elementos. / Returns element count. |

---

## 🧩 Decisiones de diseño / Design decisions

| Decisión / Decision | Alternativa considerada / Alternative | Razón / Reason |
|---|---|---|
| Clases independientes con `__slots__` | Diccionarios dinámicos o tuplas con nombre | Reducción de huella en memoria, acceso rápido a atributos e integridad estructural estricta. / Reduced memory footprint, fast attribute access, and strict structural integrity. |
| Módulos separados en paquete `data_structures_basics` | Todo el código en un único fichero plano | Mayor modularidad, claridad arquitectónica y reusabilidad limpia mediante re-exportaciones en `__init__.py`. / Higher modularity, architectural clarity, and clean reusability via `__init__.py` re-exports. |
| Constructores `__init__` como `init` | Métodos explícitos `init()` adicionales | Mecanismo idiomático estándar de instanciación e inicialización en Python sin redundancia de estado no inicializado. / Standard idiomatic mechanism for instantiation and initialization in Python without uninitialized state redundancy. |
| Propiedades `@property` en `Node` y `LinkedList` | Métodos `get_value()`, `get_next()`, etc. | Sintaxis pythónica idiomática de acceso a atributos de lectura preservando el encapsulamiento. / Idiomatic Pythonic syntax for read attribute access while preserving encapsulation. |

---

## 🔀 Adaptaciones idiomáticas / Idiomatic adaptations

| Especificación / Specification | Adaptación / Adaptation | Justificación / Justification |
|---|---|---|
| `Node.init(value)` y estructuras `init()` | Constructores `__init__` | En Python los objetos se inicializan idiomáticamente al crearse mediante `__init__`. / In Python objects are idiomatically initialized upon creation via `__init__`. |
| `get_value()`, `get_next()`, `set_next(next)` | `@property value`, `@property next`, `@next.setter` | Interfaz orientada a propiedades idiomática en Python para accesores y mutadores de nodos. / Idiomatic Python property interface for node accessors and mutators. |
| `LinkedList.get_head()` | Propiedad `head` (valor) y `head_node` (nodo) | Permite retornar el valor entero con centinela (`head`) o el nodo para permitir el recorrido encadenado de la prueba (`head_node`). / Enables returning integer value with sentinel (`head`) or node for chained traversal in tests (`head_node`). |
| `LinkedList.delete(value)` retorno booleano | Retorna `True` (éxito) o `False` (fallo) | Python expresa idiomáticamente el éxito/fallo de mutación condicional mediante valores booleanos nativos. / Python idiomatically expresses conditional mutation success/failure using native booleans. |
| Ubicación esperada: `src/data_structures_basics.ext` | `src/data_structures_basics/*.py` | Separación por responsabilidades (un archivo por ADT) con re-exportación en `__init__.py`. / Separation of concerns (one file per ADT) with re-exports in `__init__.py`. |
| Ubicación esperada: `test/run_tests.ext` | `tests/data_structures_basics_tests.py` con `pytest` | pytest incluye su propio test runner automático y configuración en `pyproject.toml`. / pytest provides its own automated test runner and configuration in `pyproject.toml`. |

---

## 🚨 Indicadores de fallo / Failure indicators

| Operación / Operation | Situación de fallo / Failure situation | Indicador / Indicator | Ejemplo / Example |
|---|---|---|---|
| `node.next` | Enlace ausente | `None` | `Node(10).next` → `None` |
| `list.head` | Lista vacía | `-1` | `LinkedList().head` → `-1` |
| `list.delete(value)` | Valor ausente en la lista | `False` | `LinkedList().delete(99)` → `False` |
| `stack.peek()` | Pila vacía | `-1` | `Stack().peek()` → `-1` |
| `stack.pop()` | Pila vacía | `-1` | `Stack().pop()` → `-1` |
| `queue.peek()` | Cola vacía | `-1` | `Queue().peek()` → `-1` |
| `queue.dequeue()` | Cola vacía | `-1` | `Queue().dequeue()` → `-1` |

---

## ✅ Cobertura de pruebas / Test coverage

### `Node`

| Caso de la especificación / Specification case | Cubierto / Covered | Prueba / Test | Notas / Notes |
|---|---|:--:|---|
| Inicializar y observar valor/enlace | Sí | `tests/data_structures_basics_tests.py:59-92` | Verifica `value == 10` y `next is None`. / Verifies `value == 10` and `next is None`. |
| Inicializar otro nodo, enlazar y recorrer | Sí | `tests/data_structures_basics_tests.py:59-92` | Verifica encadenamiento de nodos y lectura de valor. / Verifies chained nodes and value reading. |

### `LinkedList`

| Caso de la especificación / Specification case | Cubierto / Covered | Prueba / Test | Notas / Notes |
|---|---|:--:|---|
| Estado vacío | Sí | `tests/data_structures_basics_tests.py:94-157` | Verifica `is_empty() == True`, `size() == 0` y `head == -1`. / Verifies `is_empty() == True`, `size() == 0`, and `head == -1`. |
| Insertar por ambos extremos | Sí | `tests/data_structures_basics_tests.py:94-157` | Inserta 10, 20 (cola), 5 (cabeza), 10 (cola); verifica recorrido `(5, 10, 20, 10)`. / Inserts 10, 20 (tail), 5 (head), 10 (tail); checks traversal `(5, 10, 20, 10)`. |
| Eliminar primera aparición | Sí | `tests/data_structures_basics_tests.py:94-157` | Elimina primera aparición de 10; verifica recorrido `(5, 20, 10)` y `size == 3`. / Deletes first occurrence of 10; checks traversal `(5, 20, 10)` and `size == 3`. |
| Valor ausente | Sí | `tests/data_structures_basics_tests.py:94-157` | Intenta eliminar 99; verifica retorno `False` y estado inalterado. / Attempts deleting 99; checks `False` return and unchanged state. |
| Vaciar | Sí | `tests/data_structures_basics_tests.py:94-157` | Elimina 5, 20, 10; verifica `is_empty() == True`, `size() == 0` y `head == -1`. / Deletes 5, 20, 10; checks `is_empty() == True`, `size() == 0`, and `head == -1`. |

### `Stack`

| Caso de la especificación / Specification case | Cubierto / Covered | Prueba / Test | Notas / Notes |
|---|---|:--:|---|
| Estado vacío y extracción fallida | Sí | `tests/data_structures_basics_tests.py:159-212` | Verifica `is_empty() == True`, `size() == 0`, `peek() == -1` y `pop() == -1`. / Verifies `is_empty() == True`, `size() == 0`, `peek() == -1`, and `pop() == -1`. |
| LIFO y `peek` no mutante | Sí | `tests/data_structures_basics_tests.py:159-212` | Apila 10, 20, 30; verifica `peek() == 30` y `size() == 3`. / Pushes 10, 20, 30; checks `peek() == 30` and `size() == 3`. |
| Extracción y reutilización | Sí | `tests/data_structures_basics_tests.py:159-212` | Desapila 30, apila 40, desapila 40, 20, 10; verifica vacío final. / Pops 30, pushes 40, pops 40, 20, 10; checks final empty state. |
| Vacío tras extracción | Sí | `tests/data_structures_basics_tests.py:159-212` | Verifica fallo al desapilar de nuevo y preservación de `is_empty() == True`. / Verifies failure on further pop and preserved `is_empty() == True`. |

### `Queue`

| Caso de la especificación / Specification case | Cubierto / Covered | Prueba / Test | Notas / Notes |
|---|---|:--:|---|
| Estado vacío y extracción fallida | Sí | `tests/data_structures_basics_tests.py:214-266` | Verifica `is_empty() == True`, `size() == 0`, `peek() == -1` y `dequeue() == -1`. / Verifies `is_empty() == True`, `size() == 0`, `peek() == -1`, and `dequeue() == -1`. |
| FIFO y `peek` no mutante | Sí | `tests/data_structures_basics_tests.py:214-266` | Encola 10, 20, 30; verifica `peek() == 10` y `size() == 3`. / Enqueues 10, 20, 30; checks `peek() == 10` and `size() == 3`. |
| Extracción y reutilización | Sí | `tests/data_structures_basics_tests.py:214-266` | Desencola 10, encola 40, desencola 20, 30, 40; verifica vacío final. / Dequeues 10, enqueues 40, dequeues 20, 30, 40; checks final empty state. |
| Vacío tras extracción | Sí | `tests/data_structures_basics_tests.py:214-266` | Verifica fallo al desencolar de nuevo y preservación de `is_empty() == True`. / Verifies failure on further dequeue and preserved `is_empty() == True`. |

---

## ⚠️ Limitaciones conocidas / Known limitations

Ninguna / None

**ES:** Las estructuras no imponen límites artificiales de capacidad y operan dentro de los límites de memoria disponible, preservando todas las cotas de complejidad $O(1)$ y $O(n)$ del contrato.

**EN:** The structures impose no artificial capacity limits and operate within available memory boundaries, preserving all $O(1)$ and $O(n)$ complexity bounds from the contract.

---

## 📝 Notas de implementación / Implementation Notes

**ES:**

- **Estructura compartida:** `Node` es el único tipo de celda enlazada compartido por `LinkedList`, `Stack` y `Queue`.
- **Independencia de ADTs:** `Stack` gestiona directamente `top` y `Queue` gestiona directamente `front` y `rear`. Ninguna envuelve `LinkedList`.
- **Valores centinela:** `-1` se utiliza como indicador natural de fallo para valores enteros cuando las estructuras están vacías; enlaces ausentes se representan con `None`.
- **Manejo de memoria:** Python gestiona la recolección de basura mediante conteo de referencias y recolector de ciclos; al desacoplar nodos huérfanos se liberan automáticamente.

**EN:**

- **Shared structure:** `Node` is the single linked cell type shared across `LinkedList`, `Stack`, and `Queue`.
- **ADT independence:** `Stack` directly manages `top` and `Queue` directly manages `front` and `rear`. Neither wraps `LinkedList`.
- **Sentinel values:** `-1` is used as the natural integer failure indicator when structures are empty; absent links are represented as `None`.
- **Memory management:** Python handles garbage collection via reference counting and cyclic GC; unlinked orphan nodes are reclaimed automatically.

**ES:** Este proyecto también está implementado en otros lenguajes. Explora el repositorio principal para consultar las demás versiones.

**EN:** This project is also implemented in other languages. Explore the main repository to see the other versions.

---

## 🔍 Checklist de validación / Validation checklist

- [x] La suite nativa se ejecutó y su salida real está copiada en este README.
- [x] Cada caso de la especificación tiene su fila en _Cobertura de pruebas_.
- [x] Cada desviación del pseudocódigo o de la ubicación esperada está en _Adaptaciones idiomáticas_.
- [x] Cada operación con fallo posible está en _Indicadores de fallo_.
- [x] No hay rutas absolutas del autor, credenciales ni salidas inventadas.
- [x] Los enlaces relativos resuelven dentro del repositorio y el documento es bilingüe.
- [x] Ninguna sección repite lo que ya dice la especificación.

---

## 📚 Referencias / References

| Tipo / Kind | Referencia / Reference |
|---|---|
| Especificación / Specification | [`06_Data_Structures_Basics.md`](https://yorche3.github.io/programming_languages/core/algorithms/06_Data_Structures_Basics/) |
| Módulo homologado del lenguaje / Homologated module | [`python/core/foundations/numbers/`](../../foundations/numbers/) |
| Guía de inicialización / Initialisation guide | [`core/00_Project_Initialization_Guide.md`](https://yorche3.github.io/programming_languages/core/00_Project_Initialization_Guide/) |
| Adaptaciones idiomáticas / Idiomatic adaptations | [`AGENT_Template.md`](https://yorche3.github.io/programming_languages/docs/AGENT_Template/) |
| Validación de la documentación / Documentation validation | [`WORKFLOW.md`](https://yorche3.github.io/programming_languages/docs/WORKFLOW/) |
| Documentación oficial del lenguaje / Language official docs | [Python Documentation — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) |

---

*[← Volver a 05_Naive_Sort](../naive_sort/) | [↑ Volver a inicio / Back to home](https://yorche3.github.io/programming_languages/)*
