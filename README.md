# Python

Proyectos en **Python (3.8+)**, con programas simples ejecutados con el intérprete
`python3` y proyectos con pruebas unitarias gestionados con **pytest**, el framework
de pruebas más recomendado del ecosistema Python.

---

## 📂 Módulos / Modules

| Módulo | Descripción |
| ------ | ----------- |
| [`core/foundations/`](core/foundations/) | **Fase 0 — Fundamentos**: `helloworld`, `hellouser`, `unit_test/calculator`, `numbers` |

---

## ▶️ Comenzar / Getting Started

```bash
# Hello, World!
cd core/foundations/helloworld
python3 helloworld.py

# Hello, User!
cd core/foundations/hellouser
python3 hellouser.py

# Calculator Tests
cd core/foundations/unit_test/calculator
pytest test/

# Numbers Tests
cd core/foundations/numbers
pytest
```

---

## 📦 Requisitos / Requirements

| Herramienta | Instalación |
| ----------- | ----------- |
| [Python 3.8+](https://www.python.org/downloads/) | `sudo apt install python3` (Linux) / [Descargar](https://www.python.org/downloads/) |
| [pytest](https://docs.pytest.org/) | `sudo apt install python3-pytest` (Linux) / `pip install pytest` |

```bash
# Verificar instalación
python3 --version
pytest --version
```

---

## 🏗️ Tipos de proyecto / Project Types

### 1. Programa simple (interpretado con `python3`)

**ES:** Un único archivo fuente, sin dependencias externas, ejecutado directamente
con el intérprete. Ideal para `helloworld` y `hellouser`. Solo requiere la
biblioteca estándar. Opcionalmente se puede compilar a bytecode con `py_compile`.

**EN:** A single source file, no external dependencies, run directly with the
interpreter. Ideal for `helloworld` and `hellouser`. Only the standard library is
required. Optionally, it can be compiled to bytecode with `py_compile`.

```bash
python3 <File>.py
```

### 2. Proyecto con pruebas unitarias (pytest)

**ES:** Para proyectos que requieren pruebas unitarias, se usa **pytest** como
framework de test. El código fuente se organiza en `src/` y las pruebas en `test/`
(o `tests/`, la convención de pytest), con descubrimiento automático mediante
`pyproject.toml` y `conftest.py` para resolver las importaciones.

**EN:** For projects that require unit tests, **pytest** is used as the test
framework. Source code goes in `src/` and tests in `test/` (or `tests/`, pytest's
convention), with automatic discovery via `pyproject.toml` and `conftest.py` to
resolve imports.

```bash
pytest                    # desde la raíz del proyecto (lee pyproject.toml)
pytest <dir>/             # suite específica
python3 -m pytest         # alternativa equivalente
```

---

## 🌐 Otras implementaciones / Other implementations

Este proyecto también está implementado en otros lenguajes. Explora el [repositorio
principal](https://github.com/yorche3/programming_languages) para ver todas las
versiones.

---

*🌐 [github.com/yorche3/programming_languages](https://github.com/yorche3/programming_languages) · [GitHub Pages](https://yorche3.github.io/programming_languages/)*
