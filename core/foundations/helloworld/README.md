# Hello, World! — Python

Implementación de la especificación [01_Hello_World](https://yorche3.github.io/programming_languages/core/foundations/01_Hello_World/) en **Python**, con un enfoque manual y minimalista.

---

## 📂 Archivos y estructura / Files & Structure

| Archivo | Propósito |
|---------|-----------|
| [`helloworld.py`](helloworld.py) | Código fuente: imprime `"Hello, World! from Python!"` en la salida estándar. |

**Estructura de directorios esperada:**

```text
helloworld/
├── helloworld.py   # Código fuente
└── README.md       # Este archivo
```

---

## 🛠️ Enfoque y construcción / Approach & Build

**ES:** El proyecto se creó manualmente, sin herramientas de scaffolding. Un único archivo `.py` es suficiente: Python es un lenguaje interpretado, por lo que no requiere compilación previa para ejecutarse.

**EN:** The project was created manually, without scaffolding tools. A single `.py` file is enough: Python is an interpreted language, so no prior compilation is required to run it.

### Inicialización / Initialization

1. Crear la estructura de directorios:

   ```bash
   mkdir -p python/core/foundations/helloworld
   ```

2. Escribir el archivo `helloworld.py` con el código fuente.

3. No se necesita ningún paso adicional de construcción o vinculación de dependencias.

---

## 📄 Archivos de configuración clave / Key Configuration Files

No se requieren archivos de configuración de build. El programa se ejecuta directamente con el intérprete `python3`.

```python
print("Hello, World! from Python!")
```

| Elemento | Propósito |
|----------|-----------|
| `print(...)` | Función integrada que imprime su argumento en la salida estándar y añade un salto de línea al final. |
| `"Hello, World! from Python!"` | Argumento: la cadena a imprimir. |

> **ES:** `print` acepta varios argumentos (separados por espacios), y el salto de línea final se puede suprimir con `end=""`.
> **EN:** `print` accepts multiple arguments (separated by spaces), and the trailing newline can be suppressed with `end=""`.

---

## 🚀 Compilación y ejecución / Build & Run

### Requisito: Tener Python instalado

```bash
# Verificar instalación
python3 --version
```

### Ejecutar con el intérprete / Run with the interpreter

```bash
cd python/core/foundations/helloworld
python3 helloworld.py
```

### Verificar sintaxis sin ejecutar / Check syntax without running

```bash
python3 -m py_compile helloworld.py
```

### Salida esperada / Expected output

```text
Hello, World! from Python!
```

---

## 📝 Notas de implementación / Implementation Notes

- **ES:** Python no requiere una función `main`: el script se ejecuta de arriba a abajo.
- **EN:** Python does not require a `main` function: the script executes top to bottom.
- **ES:** `print` escribe en `stdout` y añade automáticamente un salto de línea.
- **EN:** `print` writes to `stdout` and automatically appends a newline.

---

## 🌐 Otras implementaciones / Other implementations

Este proyecto también está implementado en otros lenguajes. Explora el [repositorio principal](https://github.com/yorche3/programming_languages) para ver todas las versiones.

---

*🌐 [github.com/yorche3/programming_languages](https://github.com/yorche3/programming_languages) · [GitHub Pages](https://yorche3.github.io/programming_languages/)*
