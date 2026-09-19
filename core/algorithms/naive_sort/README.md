# Naive Sort — Python

Implementación de la especificación [05_Naive_Sort](https://yorche3.github.io/programming_languages/core/algorithms/05_Naive_Sort/) en **Python**, usando **pytest** como framework de pruebas unitarias y una **arquitectura de librería con src-layout**.

Tres algoritmos de ordenación con coste $O(n^2)$: **selection sort**, **bubble sort** e **insertion sort**, los tres *in-place* sobre la lista recibida, sin invocar bibliotecas de ordenamiento ni estructuras auxiliares.

---

## 📂 Archivos y estructura / Files & Structure

| Archivo | Propósito |
|---------|-----------|
| [`pyproject.toml`](pyproject.toml) | Metadatos de la librería (PEP 621) + configuración de pytest. |
| [`src/naive_sort.py`](src/naive_sort.py) | Módulo `naive_sort` — las 3 funciones del contrato. |
| [`conftest.py`](conftest.py) | Añade `src/` a `sys.path` para importar el módulo sin instalarlo. |
| [`tests/naive_sort_tests.py`](tests/naive_sort_tests.py) | Suite única: 3 tests (8 casos cada uno). |
| [`.gitignore`](.gitignore) | Ignora `__pycache__/`, `*.py[cod]`, `.pytest_cache/`, artefactos de build. |

**Estructura de directorios esperada:**

```text
naive_sort/
├── pyproject.toml               # Librería + configuración de pytest
├── conftest.py                  # sys.path para tests
├── .gitignore                   # Ignora artefactos
├── src/
│   └── naive_sort.py            # 3 funciones del contrato
└── tests/
    └── naive_sort_tests.py      # 3 tests, 8 casos cada uno
```

---

## 🛠️ Enfoque y construcción / Approach & Build

**ES:** Sigue la misma **arquitectura de librería** (src-layout) que [`numbers`](../../foundations/numbers/) y [`calculator`](../../foundations/unit_test/calculator/):

1. **`pyproject.toml`** (PEP 621) declara la librería `naive-sort-algorithms` con el módulo `naive_sort` en `src/`.
2. **pytest** se configura en el mismo `pyproject.toml` (`testpaths`, `python_files = ["*_tests.py"]`).
3. **`conftest.py`** añade `src/` a `sys.path` para que los tests importen `naive_sort` sin instalarlo.
4. Las **3 funciones** del contrato viven en un único módulo y son autónomas: no hay helpers compartidos ni estructuras auxiliares.

**EN:** Follows the same **library architecture** (src-layout) as [`numbers`](../../foundations/numbers/) and [`calculator`](../../foundations/unit_test/calculator/):

1. **`pyproject.toml`** (PEP 621) declares the `naive-sort-algorithms` library with the `naive_sort` module under `src/`.
2. **pytest** is configured in the same `pyproject.toml` (`testpaths`, `python_files = ["*_tests.py"]`).
3. **`conftest.py`** adds `src/` to `sys.path` so tests import `naive_sort` without installing it.
4. The contract's **3 functions** live in a single module and are self-contained: no shared helpers and no auxiliary structures.

**Combinación aplicada:** implementación iterativa + listas mutables → **1 suite × 3 tests = 3 tests (24 casos)**.

**Applied combination:** iterative implementation + mutable lists → **1 suite × 3 tests = 3 tests (24 cases)**.

---

## 📄 Archivos de configuración clave / Key Configuration Files

### `pyproject.toml` — Librería + pytest

**ES:** El paquete se llama `naive-sort-algorithms` (no `naive-sort`, por el mismo motivo que `numbers-algorithms`). `requires-python = ">=3.8"` reproduce el mínimo ya usado en `numbers/`.

**EN:** The package is named `naive-sort-algorithms` (not `naive-sort`, for the same reason as `numbers-algorithms`). `requires-python = ">=3.8"` mirrors the minimum already used in `numbers/`.

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "naive-sort-algorithms"
version = "1.0.0"
description = "Elementary O(n^2) sorting algorithms: selection, bubble and insertion sort."
requires-python = ">=3.8"

[tool.setuptools]
py-modules = ["naive_sort"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["*_tests.py"]
```

### `conftest.py` — Import sin instalación

**ES:** Añade `src/` al inicio de `sys.path`. También purga `naive_sort` de `sys.modules` por simetría con `numbers/`: aquí **no hay colisión** con la biblioteca estándar (no existe un módulo `naive_sort`), así que esa línea es inocua.

**EN:** Adds `src/` to the start of `sys.path`. It also purges `naive_sort` from `sys.modules` for symmetry with `numbers/`: here there is **no collision** with the standard library (there is no `naive_sort` module), so that line is harmless.

```python
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.modules.pop('naive_sort', None)
```

### `src/naive_sort.py` — Implementación

**ES:** Las tres funciones reciben una lista de enteros y ordenan **in-place**, devolviendo esa misma lista. Extracto de `bubble_sort`, que conserva la bandera `swapped` y la salida temprana del pseudocódigo:

**EN:** All three functions take a list of integers and sort **in-place**, returning that same list. Excerpt from `bubble_sort`, which keeps the pseudocode's `swapped` flag and early exit:

```python
def bubble_sort(arr):
    if arr is None:
        return None
    n = len(arr)
    if n < 2:
        return arr
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

### Suites de pruebas — pytest

**ES:** Una única suite con una función `test_*` por algoritmo. Los 8 casos viven en una lista de diccionarios compartida y un único helper los recorre para cualquier función; el helper recibe el nombre del algoritmo para componer el mensaje:

**EN:** A single suite with one `test_*` function per algorithm. The 8 cases live in a shared list of dictionaries and a single helper walks them for any function; the helper receives the algorithm name to compose the message:

```python
def assert_sorts_all_cases(sort, algorithm):
    for case in CASES:
        source = case["input"]
        actual = sort(None if source is None else list(source))
        assert actual == case["expected"], (
            f"{algorithm} should sort {case['description']}"
        )
```

---

## 🚀 Compilación y ejecución / Build & Run

### Requisitos / Requirements

- **Python 3.8+** (`python3`).
- **pytest** (`pytest`).

```bash
python3 --version
pytest --version
```

### Verificación estática / Static check

**ES:** Python no compila a un artefacto previo, así que la verificación estática es la compilación a *bytecode* con los avisos tratados como errores. El entorno del repositorio no tiene linters instalados (`ruff`, `flake8`, `pylint` y `mypy` no están disponibles), de modo que `py_compile` es el análisis ejecutado:

**EN:** Python does not compile to a prior artifact, so the static check is bytecode compilation with warnings treated as errors. The repository environment has no linters installed (`ruff`, `flake8`, `pylint` and `mypy` are unavailable), so `py_compile` is the analysis that was run:

```bash
cd python/core/algorithms/naive_sort
python3 -W error -m py_compile src/naive_sort.py tests/naive_sort_tests.py conftest.py
```

```text
py_compile sin errores ni warnings (exit 0)
```

### Ejecutar las pruebas unitarias / Run tests

```bash
cd python/core/algorithms/naive_sort
pytest
```

### Usar el módulo como librería / Use the module as a library

```bash
# Opción A — import directo con PYTHONPATH
PYTHONPATH=src python3 -c "from naive_sort import bubble_sort; print(bubble_sort([5, 2, 9, 1, 5, 6]))"

# Opción B — instalación editable (PEP 660)
python3 -m pip install -e .
```

### Salida esperada / Expected output

```text
collected 3 items

tests/naive_sort_tests.py::test_selection_sort PASSED                    [ 33%]
tests/naive_sort_tests.py::test_bubble_sort PASSED                       [ 66%]
tests/naive_sort_tests.py::test_insertion_sort PASSED                    [100%]

============================== 3 passed in 0.01s ==============================
```

> **ES:** 3 tests (uno por algoritmo); los 24 casos viven como `assert` dentro de ellos (8 por algoritmo), todos pasando.
> **EN:** 3 tests (one per algorithm); the 24 cases live as `assert`s within them (8 per algorithm), all passing.

---

## 🧠 Algoritmos y operaciones / Algorithms & Operations

| Algoritmo | Función | Estrategia | Entrada ordenada | Entrada invertida |
|-----------|---------|-----------|:----------------:|:-----------------:|
| Selection sort | `selection_sort` | Busca el mínimo del tramo no ordenado con `min_idx` y lo intercambia al inicio | $O(n^2)$ | $O(n^2)$ |
| Bubble sort | `bubble_sort` | Compara e intercambia adyacentes; bandera `swapped` con `break` (**salida temprana**) | $O(n)$ | $O(n^2)$ |
| Insertion sort | `insertion_sort` | Toma cada elemento como `key` y desplaza el sub-tramo ordenado | $O(n)$ | $O(n^2)$ |

**ES:** Las tres funciones son autónomas: no comparten helpers, y no hay ninguna estructura auxiliar más allá de los índices y la variable `key`.

**EN:** All three functions are self-contained: they share no helpers, and there is no auxiliary structure beyond the indices and the `key` variable.

### Casos cubiertos / Covered cases

| # | Caso | Entrada | Salida esperada |
|:-:|------|---------|-----------------|
| 1 | Array estándar desordenado | `[5, 2, 9, 1, 5, 6]` | `[1, 2, 5, 5, 6, 9]` |
| 2 | Array ya ordenado | `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` |
| 3 | Array en orden inverso | `[5, 4, 3, 2, 1]` | `[1, 2, 3, 4, 5]` |
| 4 | Elementos idénticos | `[7, 7, 7, 7]` | `[7, 7, 7, 7]` |
| 5 | Con números negativos | `[3, -1, 4, -5, 0]` | `[-5, -1, 0, 3, 4]` |
| 6 | Un solo elemento | `[42]` | `[42]` |
| 7 | Lista vacía | `[]` | `[]` |
| 8 | Entrada nula | `None` | `None` |

**ES:** Son los 7 casos obligatorios de la especificación más el caso nulo, que en Python sí es representable (ver la nota correspondiente).

**EN:** These are the 7 mandatory cases from the specification plus the null case, which is representable in Python (see the corresponding note).

---

## 📝 Notas de implementación / Implementation Notes

### 🧬 Ordenamiento *in-place* sobre la lista recibida / In-place sorting over the received list

**ES:** Las listas de Python son **mutables**, así que los tres algoritmos ordenan la propia lista que reciben (`arr[i], arr[min_idx] = arr[min_idx], arr[i]`) y devuelven **esa misma referencia**, que es la variante *in-place* que la especificación permite. Por eso los tests pasan a cada función una **copia** del fixture compartido (`list(source)`), de modo que un caso no puede contaminar los siguientes.

**EN:** Python lists are **mutable**, so all three algorithms sort the very list they receive (`arr[i], arr[min_idx] = arr[min_idx], arr[i]`) and return **that same reference**, which is the *in-place* variant the specification allows. That is why the tests pass each function a **copy** of the shared fixture (`list(source)`), so one case cannot contaminate the next.

### 🚫 Caso nulo incluido: `None` como indicador de fallo / Null case included: `None` as the failure indicator

**ES:** El contrato exige devolver el indicador de fallo del lenguaje cuando la entrada es nula o inválida, sin lanzar excepciones. En Python el indicador natural es **`None`**, que además es distinguible del caso vacío (`[]` devuelve la misma lista vacía), y las tres funciones lo comprueban con `if arr is None: return None` antes de leer `len(arr)`. Es un caso controlado del contrato, no una prueba de excepción: la suite lo cubre como caso 8.

**EN:** The contract requires returning the language's failure indicator when the input is null or invalid, without throwing exceptions. In Python the natural indicator is **`None`**, which is also distinguishable from the empty case (`[]` returns the same empty list), and all three functions check it with `if arr is None: return None` before reading `len(arr)`. It is a controlled contract case, not an exception test: the suite covers it as case 8.

### 🔁 `bubble_sort` y la bandera de intercambio / `bubble_sort` and the swap flag

**ES:** El criterio de aceptación exige la optimización de salida temprana. `bubble_sort` pone `swapped = False` al inicio de cada pasada, lo activa al intercambiar y ejecuta `if not swapped: break` al terminar, que es el `if not swapped then break` del pseudocódigo: una lista ya ordenada se resuelve en **una sola pasada** y el mejor caso es $O(n)$. El bucle exterior recorre `range(n)` en lugar del `0 to n - 2` del pseudocódigo; la pasada extra tiene el rango interno vacío (`n - i - 1 == 0`), deja `swapped` en `False` y sale por el `break`, así que el resultado observable es el mismo. La bandera **no es observable en la salida** (las tres funciones devuelven una lista ordenada), por lo que la suite no puede detectar su ausencia: su presencia se verifica comparando el código con el pseudocódigo, no con los tests.

**EN:** The acceptance criteria require the early-exit optimisation. `bubble_sort` sets `swapped = False` at the start of each pass, sets it when swapping and runs `if not swapped: break` at the end, which is the pseudocode's `if not swapped then break`: an already sorted list is solved in **a single pass** and the best case is $O(n)$. The outer loop walks `range(n)` instead of the pseudocode's `0 to n - 2`; the extra pass has an empty inner range (`n - i - 1 == 0`), leaves `swapped` as `False` and exits through the `break`, so the observable result is the same. The flag is **not observable in the output** (all three functions return a sorted list), so the suite cannot detect its absence: its presence is verified by comparing the code against the pseudocode, not by the tests.

### 🔀 Estabilidad de `insertion_sort` / `insertion_sort` stability

**ES:** El desplazamiento usa la comparación estricta `arr[j] > key`, así que `insertion_sort` es estable: los elementos iguales conservan su orden relativo. El caso 1 (`[5, 2, 9, 1, 5, 6]`, con dos cincos) se beneficia de ello, aunque los tests comparan valores y no identidad.

**EN:** The shifting uses the strict comparison `arr[j] > key`, so `insertion_sort` is stable: equal elements keep their relative order. Case 1 (`[5, 2, 9, 1, 5, 6]`, with two fives) benefits from it, although the tests compare values rather than identity.

### 🔀 `selection_sort` sin la guarda `min_idx != i` / `selection_sort` without the `min_idx != i` guard

**ES:** El pseudocódigo solo intercambia cuando `min_idx != i`; la implementación intercambia siempre `arr[i], arr[min_idx] = arr[min_idx], arr[i]`. Cuando `min_idx == i` el intercambio es una **operación nula sobre el mismo par de posiciones**, así que el resultado observable y la complejidad $O(n^2)$ no cambian: es una divergencia idiomática aceptada, no un defecto.

**EN:** The pseudocode only swaps when `min_idx != i`; the implementation always swaps `arr[i], arr[min_idx] = arr[min_idx], arr[i]`. When `min_idx == i` the swap is a **no-op on the same pair of positions**, so neither the observable result nor the $O(n^2)$ complexity changes: it is an accepted idiomatic divergence, not a defect.

### 🏷️ Naming y ausencia de `main` / Naming and missing `main`

**ES:** Las funciones usan `snake_case` (`selection_sort`), que coincide con el nombre de la especificación, y los parámetros conservan el nombre `arr` de la documentación. No hay `main`: el punto de entrada es el propio runner de pytest, que descubre las funciones `test_*`.

**EN:** Functions use `snake_case` (`selection_sort`), matching the specification's name, and parameters keep the documentation's `arr` name. There is no `main`: the entry point is pytest's own runner, which discovers the `test_*` functions.

### 📍 Desviaciones respecto a la ubicación esperada / Deviations from the expected location

| Especificación | Implementación | Motivo |
|----------------|----------------|--------|
| `src/naive_sort.ext` | `src/naive_sort.py` | Nombre exacto del módulo; solo cambia la extensión. |
| `test/naive_sort_test.ext` | `tests/naive_sort_tests.py` | El directorio va en plural y con el sufijo `_tests.py`, como en `numbers/` (`tests/recursive_tests.py`) y como exige `python_files = ["*_tests.py"]`. |
| `test/run_tests.ext` | — | pytest trae su propio runner: descubre y ejecuta las funciones `test_*`, así que la especificación no pide un archivo de ejecución aparte. |

**ES:** Este proyecto también está implementado en otros lenguajes. Explora el repositorio principal para consultar las demás versiones.

**EN:** This project is also implemented in other languages. Explore the main repository to see the other versions.

---

*[← Volver a Algoritmos Puros](../README.md) · [↑ Volver a Core](../../README.md)*

*🌐 [github.com/yorche3/programming_languages](https://github.com/yorche3/programming_languages) · [GitHub Pages](https://yorche3.github.io/programming_languages/)*
