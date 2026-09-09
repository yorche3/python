# Numbers — Python

Implementación de la especificación [04_Numbers](https://yorche3.github.io/programming_languages/core/foundations/04_Numbers/) en **Python**, usando **pytest** como framework de pruebas unitarias y una **arquitectura de librería con src-layout**.

Tres enfoques de implementación para los mismos 5 algoritmos: **recursivo directo** (`_rec`), **recursivo con acumulador** (`_acc`) e **iterativo** (`_ite`).

---

## 📂 Archivos y estructura / Files & Structure

| Archivo | Propósito |
|---------|-----------|
| [`pyproject.toml`](pyproject.toml) | Metadatos de la librería (PEP 621) + configuración de pytest. |
| [`src/numbers.py`](src/numbers.py) | Módulo `numbers` — 15 funciones (3 enfoques × 5 algoritmos) + 4 helpers `_help`. |
| [`conftest.py`](conftest.py) | Añade `src/` a `sys.path` y evita la colisión con el módulo stdlib `numbers`. |
| [`tests/recursive_tests.py`](tests/recursive_tests.py) | Suite recursiva: 5 tests (11 casos). |
| [`tests/iterative_tests.py`](tests/iterative_tests.py) | Suite iterativa: 5 tests (11 casos). |
| [`.gitignore`](.gitignore) | Ignora `__pycache__/`, `.pytest_cache/`, artefactos de build. |

**Estructura de directorios esperada:**

```text
numbers/
├── pyproject.toml               # Librería + configuración de pytest
├── conftest.py                  # sys.path para tests
├── .gitignore                   # Ignora artefactos
├── src/
│   └── numbers.py               # 15 funciones + 4 helpers _help
└── tests/
    ├── recursive_tests.py       # Tests recursivos (5 tests, 11 casos)
    └── iterative_tests.py       # Tests iterativos (5 tests, 11 casos)
```

---

## 🛠️ Enfoque y construcción / Approach & Build

**ES:** Este proyecto usa la **arquitectura de librería moderna de Python** (src-layout):

1. **`pyproject.toml`** (PEP 621) declara la librería `numbers-algorithms` con el módulo `numbers` en `src/`.
2. **pytest** se configura en el mismo `pyproject.toml` (`testpaths`, `python_files = ["*_tests.py"]`).
3. **`conftest.py`** añade `src/` a `sys.path` para que los tests importen `numbers` sin instalarlo.
4. Las 15 funciones se organizan en 3 grupos por enfoque:

| Enfoque | Sufijo | Ejemplo | ¿Tiene tests directos? |
| ------- | ------ | ------- | :---------------------: |
| Recursivo directo | `_rec` | `fibonacci_rec(n)` | ✅ Sí |
| Recursivo con acumulador | `_acc` | `fibonacci_acc(n)` | ❌ No (ver nota TCO) |
| Iterativo | `_ite` | `fibonacci_ite(n)` | ✅ Sí |

**EN:** This project uses Python's **modern library architecture** (src-layout):

1. **`pyproject.toml`** (PEP 621) declares the `numbers-algorithms` library with the `numbers` module under `src/`.
2. **pytest** is configured in the same `pyproject.toml` (`testpaths`, `python_files = ["*_tests.py"]`).
3. **`conftest.py`** adds `src/` to `sys.path` so tests import `numbers` without installing it.
4. The 15 functions are organized into 3 groups by approach:

| Approach | Suffix | Example | Direct tests? |
| -------- | ------ | ------- | :-----------: |
| Direct recursion | `_rec` | `fibonacci_rec(n)` | ✅ Yes |
| Accumulator recursion | `_acc` | `fibonacci_acc(n)` | ❌ No (see TCO note) |
| Iterative | `_ite` | `fibonacci_ite(n)` | ✅ Yes |

**Combinación aplicada:** TCO ❌ + iteración ✅ → `_rec` + `_ite` = **2 suites × 5 tests = 10 tests (22 casos)**.

**Applied combination:** No TCO + iteration ✅ → `_rec` + `_ite` = **2 suites × 5 tests = 10 tests (22 cases)**.

---

## 📄 Archivos de configuración clave / Key Configuration Files

### `pyproject.toml` — Librería + pytest

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "numbers-algorithms"
version = "1.0.0"
description = "Numerical algorithms in three approaches (recursive, accumulator, iterative)."
requires-python = ">=3.8"

[tool.setuptools]
py-modules = ["numbers"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["*_tests.py"]
```

### `conftest.py` — Import sin instalación

**ES:** Añade `src/` al inicio de `sys.path`. Además purga el módulo stdlib `numbers` de `sys.modules`: como Python ya trae un módulo `numbers` (PEP 3141), sin esta línea el `import numbers` de los tests resolvería el módulo de la biblioteca estándar.

**EN:** Adds `src/` to the start of `sys.path`. It also purges the stdlib `numbers` module from `sys.modules`: since Python ships a `numbers` module (PEP 3141), without this line the tests' `import numbers` would resolve the standard-library module.

```python
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.modules.pop('numbers', None)
```

### `src/numbers.py` — Implementación

**ES:** Cada algoritmo tiene 3 implementaciones en un único archivo. Los helpers `_help` son privados por convención (prefijo `_`). El estilo sigue el patrón `if/elif/else` con asignación por tuplas. Por ejemplo, `fibonacci`:

**EN:** Each algorithm has 3 implementations in a single file. The `_help` helpers are private by convention (`_` prefix). The style follows the `if/elif/else` pattern with tuple assignment. For example, `fibonacci`:

```python
# Enfoque recursivo directo / Direct recursion
def fibonacci_rec(n):
  if n <= 1:
    return n
  else:
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

# Enfoque con acumulador / Accumulator recursion
def fibonacci_acc(n):
  return fibonacci_acc_help(n, 0, 1)

def fibonacci_acc_help(n, acc2, acc1):
  if n <= 0:
    return acc2
  elif n <= 2:
    return acc1 + acc2
  else:
    return fibonacci_acc_help(n - 1, acc1, acc1 + acc2)

# Enfoque iterativo / Iterative
def fibonacci_ite(n):
  if n <= 1:
    return n
  else:
    acc2 = 0
    acc1 = 1
    for _ in range(2, n):
      acc2, acc1 = acc1, acc1 + acc2
    return acc1 + acc2
```

| Algoritmo | `_rec` | `_acc` | `_ite` |
| --------- | ------ | ------ | ------ |
| `sum_of_first_n` | `n + sum_rec(n-1)` | helper con `acc + n` | bucle `1..n` |
| `factorial` | `n * fact_rec(n-1)` | helper con `acc * n` | bucle `2..n` |
| `fibonacci` | `fib_rec(n-1) + fib_rec(n-2)` | helper con `acc2, acc1` | bucle de intercambio por tuplas |
| `greatest_common_divisor` | Euclides recursivo | helper (Euclides) | `while b: a, b = b, a % b` |
| `least_common_multiple` | `(a // gcd) * b` | `(a // gcd) * b` | `(a // gcd) * b` |

### Suites de pruebas — pytest

**ES:** Dos suites, una por enfoque probado. Cada suite agrupa una función `test_*` por función (5 por suite); los 11 casos del pseudocódigo viven como `assert` dentro de ellas (22 en total).

**EN:** Two suites, one per tested approach. Each suite groups one `test_*` function per function (5 per suite); the specification pseudocode's 11 cases live as `assert`s within them (22 in total).

```python
from numbers import fibonacci_rec

def test_fibonacci_rec():
    assert fibonacci_rec(0) == 0
    assert fibonacci_rec(1) == 1
    assert fibonacci_rec(6) == 8
```

---

## 🚀 Compilación y ejecución / Build & Run

### Requisitos / Requirements

- **Python 3.8+** (`python3`).
- **pytest** (`pytest`).

```bash
python3 --version
pytest --version

# Instalar pytest (si no está instalado)
sudo apt install python3-pytest
```

### Ejecutar las pruebas unitarias / Run tests

```bash
cd python/core/foundations/numbers
pytest
```

### Usar el módulo como librería / Use the module as a library

```bash
# Opción A — import directo con PYTHONPATH
PYTHONPATH=src python3 -c "from numbers import fibonacci_rec; print(fibonacci_rec(6))"

# Opción B — instalación editable (PEP 660)
python3 -m pip install -e .
```

### Salida esperada / Expected output

```text
============================= test session starts ==============================
collected 10 items

tests/iterative_tests.py .....                                           [ 50%]
tests/recursive_tests.py .....                                           [100%]

10 passed in 0.01s
```

> **ES:** 10 tests en total (5 por suite); los 22 casos viven como `assert` dentro de ellos, todos pasando.
> **EN:** 10 tests in total (5 per suite); the 22 cases live as `assert`s within them, all passing.

---

## 🔁 Sobre recursión con acumulador y Tail Call Optimization (TCO)

**ES:**
Tail recursion ocurre cuando la llamada recursiva es la última acción que ejecuta una función; después de la llamada no hay más instrucciones. La recursión con acumulador consigue esto pasando el estado previo como parámetro, sin dejar trabajo pendiente en la pila.

En Python, **no se garantiza TCO**: el intérprete no optimiza las llamadas de cola y el límite de recursión (~1000 frames) termina en `RecursionError`. La versión con acumulador se conserva únicamente con fines educativos, como puente conceptual entre la recursión directa (`_rec`) y la versión iterativa (`_ite`). Como no hay un beneficio práctico de rendimiento, **no se desarrollan pruebas unitarias específicas para las funciones `_acc`**. Su comportamiento queda validado a través de las suites recursiva e iterativa, que ejercitan los mismos resultados.

**EN:**
Tail recursion occurs when the recursive call is the last action executed by a function; after the call there are no more instructions. Accumulator recursion achieves this by passing the previous state as a parameter, leaving no pending work on the stack.

In Python, **TCO is not guaranteed**: the interpreter does not optimize tail calls and the recursion limit (~1000 frames) ends in `RecursionError`. The accumulator version is kept purely for educational purposes, as a conceptual bridge between direct recursion (`_rec`) and the iterative version (`_ite`). Since there is no practical performance benefit, **no dedicated unit tests are written for the `_acc` functions**. Their behavior is validated through the recursive and iterative suites, which exercise the same results.

---

## 📝 Notas de implementación / Implementation Notes

- **ES:** El proyecto no usa un `main`: el "punto de entrada" es el propio runner de pytest, que descubre y ejecuta las funciones `test_*` automáticamente. Por eso no se necesita el `run_tests` del pseudocódigo (la especificación lo pide solo si el framework no lo incluye).
- **EN:** The project has no `main`: the "entry point" is pytest's runner itself, which discovers and runs the `test_*` functions automatically. That's why the pseudocode's `run_tests` is not needed (the specification asks for it only if the framework doesn't include one).
- **ES:** El nombre `numbers` colisiona con el módulo stdlib `numbers` (PEP 3141); el `conftest.py` lo resuelve para las pruebas purgando `sys.modules`. En un entorno real se instalaría la librería (`pip install -e .`), donde el paquete instalado precede a la stdlib.
- **EN:** The name `numbers` collides with the stdlib `numbers` module (PEP 3141); `conftest.py` solves it for tests by purging `sys.modules`. In a real environment the library would be installed (`pip install -e .`), where the installed package precedes the stdlib.
- **ES:** El MCM usa `(a // gcd) * b` para evitar desbordes y mantener resultados enteros exactos.
- **EN:** LCM uses `(a // gcd) * b` to avoid overflow and keep exact integer results.
- **ES:** Los helpers `_help` son privados por convención (prefijo `_`).
- **EN:** The `_help` helpers are private by convention (`_` prefix).

---

## 🌐 Otras implementaciones / Other implementations

Este proyecto también está implementado en otros lenguajes. Explora el [repositorio principal](https://github.com/yorche3/programming_languages) para ver todas las versiones.

---

*🌐 [github.com/yorche3/programming_languages](https://github.com/yorche3/programming_languages) · [GitHub Pages](https://yorche3.github.io/programming_languages/)*
