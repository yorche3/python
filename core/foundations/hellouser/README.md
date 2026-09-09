# Hello, User! — Python

Implementación de la especificación [02_Hello_User](https://yorche3.github.io/programming_languages/core/foundations/02_Hello_User/) en **Python**, con un enfoque manual y minimalista.

Lee un nombre desde la entrada estándar y saluda al usuario.

---

## 📂 Archivos y estructura / Files & Structure

| Archivo | Propósito |
|---------|-----------|
| [`hellouser.py`](hellouser.py) | Código fuente: solicita un nombre al usuario y saluda. |

**Estructura de directorios esperada:**

```text
hellouser/
├── hellouser.py    # Código fuente
└── README.md       # Este archivo
```

---

## 🛠️ Enfoque y construcción / Approach & Build

**ES:** Este programa introduce tres conceptos nuevos respecto a `helloworld`:

1. **Entrada de usuario** — `input` imprime el prompt (sin salto de línea) y lee una línea desde la entrada estándar.
2. **Variables** — `name = ...` asigna la línea leída a la variable `name`.
3. **Concatenación** — `+` une cadenas; `str(name)` garantiza la conversión a cadena.

**EN:** This program introduces three new concepts compared to `helloworld`:

1. **User input** — `input` prints the prompt (no newline) and reads a line from standard input.
2. **Variables** — `name = ...` assigns the read line to the variable `name`.
3. **Concatenation** — `+` joins strings; `str(name)` guarantees conversion to string.

### Inicialización / Initialization

1. Crear la estructura de directorios:

   ```bash
   mkdir -p python/core/foundations/hellouser
   ```

2. Escribir el archivo `hellouser.py` con el código fuente.

3. No se necesita ningún paso adicional de construcción o vinculación de dependencias.

---

## 📄 Archivos de configuración clave / Key Configuration Files

No se requieren archivos de configuración de build. El programa se ejecuta directamente con el intérprete `python3`.

**ES:** El flujo del programa es:

1. Imprimir `"Enter your name: "` y leer la línea con `input` (el prompt no lleva salto de línea).
2. Imprimir `"Hello, <nombre>!"` concatenando con `+`.

**EN:** Program flow:

1. Print `"Enter your name: "` and read the line with `input` (the prompt has no newline).
2. Print `"Hello, <name>!"` concatenating with `+`.

```python
name = input("Enter your name: ")
print("Hello, "+ str(name) +"!")
```

| Elemento | Propósito |
|----------|-----------|
| `input("Enter your name: ")` | Imprime el prompt **sin** salto de línea y devuelve la línea leída desde la entrada estándar (sin el `\n` final). |
| `name = ...` | Asigna la cadena leída a la variable `name`. |
| `str(name)` | Convierte el valor a cadena (redundante aquí, porque `input` ya devuelve `str`). |
| `+` | Operador de concatenación de cadenas. |
| `print(...)` | Imprime con salto de línea al final. |

> **ES:** `input` siempre devuelve `str`; la conversión `str(name)` es innecesaria pero inofensiva. Una alternativa más idiomática es un f-string: `print(f"Hello, {name}!")`.
> **EN:** `input` always returns `str`; the `str(name)` conversion is unnecessary but harmless. A more idiomatic alternative is an f-string: `print(f"Hello, {name}!")`.

---

## 🚀 Compilación y ejecución / Build & Run

### Requisito: Tener Python instalado

```bash
# Verificar instalación
python3 --version
```

### Ejecutar con el intérprete / Run with the interpreter

```bash
cd python/core/foundations/hellouser
python3 hellouser.py
```

### Verificar sintaxis sin ejecutar / Check syntax without running

```bash
python3 -m py_compile hellouser.py
```

### Salida esperada / Expected output

```text
Enter your name: Ada
Hello, Ada!
```

> **ES:** El programa espera a que el usuario escriba su nombre y presione Enter antes de mostrar el saludo.

---

## 📝 Notas de implementación / Implementation Notes

- **ES:** Python no requiere una función `main`: el script se ejecuta de arriba a abajo.
- **EN:** Python does not require a `main` function: the script executes top to bottom.
- **ES:** El prompt de `input` se escribe en `stdout` sin salto de línea, de modo que el cursor permanece junto a él.
- **EN:** `input`'s prompt is written to `stdout` without a newline, so the cursor stays next to it.

---

## 🌐 Otras implementaciones / Other implementations

Este proyecto también está implementado en otros lenguajes. Explora el [repositorio principal](https://github.com/yorche3/programming_languages) para ver todas las versiones.

---

*🌐 [github.com/yorche3/programming_languages](https://github.com/yorche3/programming_languages) · [GitHub Pages](https://yorche3.github.io/programming_languages/)*
