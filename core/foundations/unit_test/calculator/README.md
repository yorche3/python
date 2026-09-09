# Calculator — Python

Implementación de la especificación [03_Unit_Test_Calculator](https://yorche3.github.io/programming_languages/core/foundations/03_Unit_Test_Calculator/) en **Python**, usando **pytest** como framework de pruebas unitarias.

---

## 📂 Archivos y estructura / Files & Structure

| Archivo | Propósito |
|---------|-----------|
| [`src/calculator.py`](src/calculator.py) | Módulo `calculator` con las 5 operaciones aritméticas. |
| [`src/__init__.py`](src/__init__.py) | Marca `src/` como paquete (permite `from src import calculator`). |
| [`test/calculator_test.py`](test/calculator_test.py) | 5 pruebas con `def test_*` y `assert`. |
| [`test/__init__.py`](test/__init__.py) | Marca `test/` como paquete. |
| [`.gitignore`](.gitignore) | Ignora `__pycache__/` y `.pytest_cache/`. |

**Estructura de directorios esperada:**

```text
calculator/
├── .gitignore                 # Ignora __pycache__/ y .pytest_cache/
├── src/
│   ├── __init__.py            # Paquete src
│   └── calculator.py          # 5 operaciones aritméticas
└── test/
    ├── __init__.py            # Paquete test
    └── calculator_test.py     # 5 tests con pytest
```

---

## 🛠️ Enfoque y construcción / Approach & Build

**ES:** Este proyecto usa **pytest** (el framework de pruebas más popular de Python) con el layout `src/` + `test/`:

1. `calculator` es un módulo con funciones simples.
2. Cada prueba es una función `test_*` con `assert` plano (sin clases, sin `unittest`).
3. El archivo de test añade el directorio del proyecto a `sys.path` para resolver `from src import calculator`.
4. `multiplication`, `division` y `modulus` se implementan con las estrategias educativas de la especificación (sin usar los operadores `*`, `/` ni `%` respectivamente).

**EN:** This project uses **pytest** (Python's most popular test framework) with the `src/` + `test/` layout:

1. `calculator` is a module with plain functions.
2. Each test is a `test_*` function with a plain `assert` (no classes, no `unittest`).
3. The test file adds the project directory to `sys.path` to resolve `from src import calculator`.
4. `multiplication`, `division` and `modulus` are implemented with the educational strategies from the specification (without using the `*`, `/` or `%` operators respectively).

---

## 📄 Archivos de configuración clave / Key Configuration Files

No se requieren archivos de configuración de build: `pytest` descubre y ejecuta las pruebas automáticamente.

### `src/calculator.py` — Módulo principal

| Operación | Implementación educativa |
| --------- | ------------------------ |
| `addition(a, b)` | Suma directa (`a + b`). |
| `subtraction(a, b)` | Resta directa (`a - b`). |
| `multiplication(a, b)` | Suma repetitiva: acumula `a`, `b` veces con `range` (no usa `*`). |
| `division(a, b)` | Resta repetitiva: resta `b` de `a` mientras `a >= b` (no usa `/`). |
| `modulus(a, b)` | Construida sobre `division` y `multiplication` (no usa `%`). |

```python
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    result = 0
    for _ in range(b):
        result = addition(result, a)
    return result

def division(a, b):
    remaining = a
    quotient = 0
    while remaining >= b:
        remaining = subtraction(remaining, b)
        quotient = addition(quotient, 1)
    return quotient

def modulus(a, b):
    q = division(a, b)
    p = multiplication(q, b)
    return subtraction(a, p)
```

### `test/calculator_test.py` — Pruebas unitarias (pytest)

**ES:** Una función `test_*` por operación, con los mismos casos del pseudocódigo de la especificación.

**EN:** One `test_*` function per operation, with the same cases as the specification pseudocode.

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import calculator

def test_addition():
    assert calculator.addition(2, 3) == 5

def test_subtraction():
    assert calculator.subtraction(5, 2) == 3

def test_multiplication():
    assert calculator.multiplication(3, 4) == 12

def test_division():
    assert calculator.division(10, 3) == 3

def test_modulus():
    assert calculator.modulus(10, 3) == 1
```

---

## 🚀 Compilación y ejecución / Build & Run

### Requisitos / Requirements

- **Python 3** (`python3`).
- **pytest** (`pytest`).

```bash
python3 --version
pytest --version

# Instalar pytest (si no está instalado)
sudo apt install python3-pytest
```

### Ejecutar las pruebas unitarias / Run tests

```bash
cd python/core/foundations/unit_test/calculator
pytest test/
```

### Salida esperada / Expected output

```text
============================= test session starts ==============================
collected 5 items

test/calculator_test.py .....                                            [100%]

5 passed in 0.01s
```

---

## 📝 Notas de implementación / Implementation Notes

- **ES:** El proyecto no usa un `main`: el "punto de entrada" es el propio runner de pytest, que descubre y ejecuta las funciones `test_*` automáticamente. Por eso no se necesita el `run_tests` del pseudocódigo (la especificación lo pide solo si el framework no lo incluye).
- **EN:** The project has no `main`: the "entry point" is pytest's runner itself, which discovers and runs the `test_*` functions automatically. That's why the pseudocode's `run_tests` is not needed (the specification asks for it only if the framework doesn't include one).
- **ES:** Solo se usa la biblioteca estándar en el módulo; pytest es una dependencia **solo para pruebas** (instalada vía apt/pip).
- **EN:** Only the standard library is used in the module; pytest is a **test-only** dependency (installed via apt/pip).
- **ES:** `division` no valida `b == 0` (fuera del alcance de este ejemplo, como indica la especificación).
- **EN:** `division` does not validate `b == 0` (out of scope for this example, as the specification states).

---

## 🌐 Otras implementaciones / Other implementations

Este proyecto también está implementado en otros lenguajes. Explora el [repositorio principal](https://github.com/yorche3/programming_languages) para ver todas las versiones.

---

*🌐 [github.com/yorche3/programming_languages](https://github.com/yorche3/programming_languages) · [GitHub Pages](https://yorche3.github.io/programming_languages/)*
