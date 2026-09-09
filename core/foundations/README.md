# 🚀 Fundamentos / Foundations — Python

Implementación de los ejercicios de la sección [Fundamentos / Foundations](https://yorche3.github.io/programming_languages/core/foundations/) del repositorio principal en **Python**.

---

## 📖 Descripción / Description

**ES:** Esta sección reúne los conceptos esenciales para empezar a trabajar con **Python**. Cubre desde los programas más básicos (`Hello, World!` y `Hello, User!`) hasta la implementación de una calculadora con pruebas unitarias y algoritmos numéricos en tres enfoques progresivos (recursivo directo, recursivo con acumulador e iterativo).

**EN:** This section brings together the essential concepts to start working with **Python**. It covers everything from the most basic programs (`Hello, World!` and `Hello, User!`) to the implementation of a calculator with unit tests and numerical algorithms in three progressive approaches (direct recursion, accumulator recursion, and iterative).

---

## 📁 Estructura / Structure

```text
python/
└── core/
    └── foundations/
        ├── README.md              # Este archivo / This file
        ├── helloworld/            # 01_Hello_World — Primer programa
        │   ├── helloworld.py
        │   └── README.md
        ├── hellouser/             # 02_Hello_User — Entrada y salida
        │   ├── hellouser.py
        │   └── README.md
        ├── unit_test/
        │   └── calculator/        # 03_Unit_Test_Calculator — Pruebas unitarias
        │       ├── src/
        │       │   ├── __init__.py
        │       │   └── calculator.py
        │       ├── test/
        │       │   ├── __init__.py
        │       │   └── calculator_test.py
        │       ├── .gitignore
        │       └── README.md
        └── numbers/               # 04_Numbers — Algoritmos numéricos
            ├── pyproject.toml
            ├── conftest.py
            ├── src/
            │   └── numbers.py
            ├── tests/
            │   ├── recursive_tests.py
            │   └── iterative_tests.py
            ├── .gitignore
            └── README.md
```

---

## 🔢 Progresión / Progression

| Especificación | Proyecto | Conceptos | Tests | Dependencias externas |
| -------------- | -------- | --------- | :---: | :-------------------: |
| [`01_Hello_World`](https://yorche3.github.io/programming_languages/core/foundations/01_Hello_World/) | [`helloworld/`](helloworld/) | `print`, ejecución interpretada, `py_compile` | — | ❌ Solo stdlib |
| [`02_Hello_User`](https://yorche3.github.io/programming_languages/core/foundations/02_Hello_User/) | [`hellouser/`](hellouser/) | `input` (prompt), variables, concatenación `+` | — | ❌ Solo stdlib |
| [`03_Unit_Test_Calculator`](https://yorche3.github.io/programming_languages/core/foundations/03_Unit_Test_Calculator/) | [`unit_test/calculator/`](unit_test/calculator/) | pytest, `def test_*`, `assert`, `sys.path` idiom | 5 | ✅ pytest (solo test) |
| [`04_Numbers`](https://yorche3.github.io/programming_languages/core/foundations/04_Numbers/) | [`numbers/`](numbers/) | Recursión, iteración, acumuladores, src-layout, TCO | 10 | ✅ pytest (solo test) |

---

## 🛠️ Enfoque general / General Approach

**ES:** Los proyectos en esta sección siguen un patrón progresivo:

1. **Hello World** y **Hello User**: Programas de un solo archivo, ejecutados directamente con `python3`. Usan exclusivamente la biblioteca estándar.
2. **Calculator**: Primer proyecto con framework de pruebas (**pytest**, el más recomendado de Python). Introduce la separación `src/` + `test/` y el runner de pytest.
3. **Numbers**: Expande el patrón a dos suites y adopta la **arquitectura de librería moderna** (src-layout con `pyproject.toml` PEP 621). Python **no garantiza TCO**, por lo que `_acc` se conserva como puente didáctico sin pruebas propias: `_rec` + `_ite` = 10 tests (22 casos).

**EN:** The projects in this section follow a progressive pattern:

1. **Hello World** and **Hello User**: Single-file programs, run directly with `python3`. Use only the standard library.
2. **Calculator**: First project with a test framework (**pytest**, Python's most recommended). Introduces the `src/` + `test/` separation and pytest's runner.
3. **Numbers**: Expands the pattern to two suites and adopts the **modern library architecture** (src-layout with a PEP 621 `pyproject.toml`). Python **does not guarantee TCO**, so `_acc` is kept as an educational bridge without dedicated tests: `_rec` + `_ite` = 10 tests (22 cases).

---

## 🚀 Ejecución rápida / Quick Start

### Hello World

```bash
cd python/core/foundations/helloworld
python3 helloworld.py
```

### Hello User

```bash
cd python/core/foundations/hellouser
python3 hellouser.py
```

### Calculator (pruebas)

```bash
cd python/core/foundations/unit_test/calculator
pytest test/
```

### Numbers (pruebas)

```bash
cd python/core/foundations/numbers
pytest
```

---

*🌐 [github.com/yorche3/programming_languages](https://github.com/yorche3/programming_languages) · [GitHub Pages](https://yorche3.github.io/programming_languages/)*
