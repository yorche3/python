# Algorithms Pure — Python

Implementaciones de la [Fase 1 — Algoritmos Puros](https://yorche3.github.io/programming_languages/ROADMAP/#fase-1--algoritmos-puros--algorithms-pure-) en **Python**: ordenamientos elementales, estructuras de datos propias, ordenamientos óptimos y distribuidos, y búsqueda.

Los módulos de esta fase trabajan sobre **listas mutables**, que se ordenan **in-place** y devuelven la misma referencia, y no necesitan ningún tipo opcional para el indicador de fallo: una entrada `None` devuelve `None`.

---

## 📂 Módulos / Modules

| Módulo | Especificación | Enfoque | Tests | Estado |
|--------|---------------|---------|:-----:|:------:|
| [`naive_sort/`](naive_sort/) | [05_Naive_Sort](https://yorche3.github.io/programming_languages/core/algorithms/05_Naive_Sort/) | `pytest` | 3 | ✅ |

---

## 📁 Estructura / Structure

```text
algorithms/
└── naive_sort/                      # 05_Naive_Sort
    ├── pyproject.toml               # Librería (PEP 621) + configuración de pytest
    ├── conftest.py                  # sys.path para tests
    ├── .gitignore                   # Ignora artefactos
    ├── src/
    │   └── naive_sort.py            # 3 funciones del contrato
    ├── tests/
    │   └── naive_sort_tests.py      # 3 tests × 8 casos
    └── README.md
```

---

## 🛠️ Patrón común / Common Pattern

| Característica | Descripción |
|---------------|-------------|
| **Runtime** | CPython 3.8+ (intérprete, sin paso de compilación a un artefacto) |
| **CLI** | `pytest` |
| **Andamiaje** | ✍️ Estructura manual (`mkdir -p src tests` + `pyproject.toml` + `conftest.py`), la que ya usa [`foundations/numbers/`](../foundations/numbers/); la guía también marca 🔧 `uv init --lib`, que no está instalado en este entorno |
| **Framework de tests** | pytest, configurado en `pyproject.toml` (`testpaths = ["tests"]`, `python_files = ["*_tests.py"]`) |
| **Runner** | El propio pytest: descubre las funciones `test_*`; no hay archivo `run_tests` |
| **Separación** | `src/` (módulo) ↔ `tests/` (suites) |
| **Import** | `conftest.py` añade `src/` a `sys.path`, así no hace falta instalar la librería |
| **Nombre del paquete** | Sufijo `-algorithms` (`naive-sort-algorithms`), como `numbers-algorithms` |
| **Iteración** | Bucles `for` sobre `range` y `while` con índices; Python no tiene recursión de cola garantizada |
| **Indexación** | Directa (`arr[i]`) y sin estructuras auxiliares; las cotas las decide el algoritmo |
| **API** | Una función por algoritmo, con `arr` como nombre del parámetro (el de la documentación) |
| **Mutabilidad** | Las listas son mutables → los algoritmos ordenan *in-place* y devuelven la misma lista; los tests pasan una copia por caso |
| **Naming** | `snake_case` idéntico al de la especificación (`selection_sort`), con el nombre como nombre del test |
| **Nulabilidad** | `None` es representable: el caso nulo se incluye y devuelve `None` sin lanzar excepciones |
| **Verificación estática** | `python3 -W error -m py_compile …`; el entorno del repositorio no tiene linters (`ruff`, `flake8`, `pylint`, `mypy`) |
| **Artefactos** | `__pycache__/`, `*.py[cod]`, `.pytest_cache/`, `*.egg-info/`, `build/`, `dist/` — ignorados por el `.gitignore` del módulo |

---

## 🚀 Compilación rápida / Quick Build

```bash
# Naive Sort Tests
cd naive_sort
pytest
```

---

## ▶️ Siguiente / Next

👉 Continúa con los módulos pendientes de esta fase en el [Roadmap](https://yorche3.github.io/programming_languages/ROADMAP/).
👉 Continue with the pending modules of this phase in the [Roadmap](https://yorche3.github.io/programming_languages/ROADMAP/).

---

*[← Volver a Core](../README.md)*

*🌐 [github.com/yorche3/programming_languages](https://github.com/yorche3/programming_languages) · [GitHub Pages](https://yorche3.github.io/programming_languages/)*
