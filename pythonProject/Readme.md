# Compilador: Python Subset a MIPS

Implementación de un compilador de cuatro fases (Análisis, Código Intermedio, Optimización y Generación) para un **subconjunto simplificado de Python**, con **MIPS** como arquitectura objetivo.

***

## Información del Curso

* **Materia:** Programación de Sistemas de Base 2
* **Institución:** Universidad Autónoma de Tamaulipas
* **Semestre:** 9
* **Profesor(es):** Dante Adolfo Muñoz Quintero

***

## Integrantes del Equipo

-   Aldama Trinidad Alfonso René - a2213332131
-   Domínguez Reyes Pavel Noel - a2213332155

***

## Estructura del Proyecto

El proyecto sigue una **arquitectura modular** que separa las fases de análisis, generación y pruebas:

| Directorio | Descripción |
| :--- | :--- |
| `src/` | Contiene el núcleo del compilador: los analizadores (Lexer, Parser), los visitantes (`VisitanteSemantico`, `VisitanteIntermedio`), el `Optimizador` y el `GeneradorMIPS`. |
| `tests/` | Archivos de prueba para la validación del compilador (códigos de entrada y sus salidas esperadas). |
| `docs/` | Documentación técnica, reporte final del proyecto y diagramas de la arquitectura. |
| `main.py` | El archivo controlador principal que orquesta todas las fases del **pipeline de compilación**. |

***

## Requisitos y Dependencias

Este proyecto requiere Python 3.8+ y las librerías de runtime necesarias para el análisis gramatical.

| Requisito | Instalación |
| :--- | :--- |
| **Python 3.8+** | (Debe estar instalado en el sistema) |
| **ANTLR Runtime** | `pip install antlr4-python3-runtime` |

***

## Instrucciones de Compilación y Ejecución

El compilador se ejecuta directamente a través del archivo `main.py`, que procesa el código fuente de prueba y genera la salida en ensamblador MIPS.

1.  **Clonar el repositorio:** (Reemplaza la URL con la dirección real de tu repositorio en GitHub)
    ```bash
    git clone [https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories](https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories)
    cd [nombre del repositorio]
    ```

2.  **Ejecutar el Compilador:**
    ```bash
    python main.py
    ```

3.  **Resultado:**
    La ejecución generará el archivo de salida **`resultado.asm`** en el directorio raíz. Este archivo puede ser cargado y ejecutado en el **simulador MIPS MARS**.

***

## Ejemplos de Uso

El siguiente código fuente, incluido en la variable `codigo_fuente` de `main.py`, demuestra las capacidades del compilador, incluyendo la **optimización de constantes** y el manejo de estructuras de control (`while` e `if`).

### Código Fuente de Prueba

```python
x = 0
y = (10 + 20) / 2  # Optimizado a y = 15

print("Iniciando ciclo")

while x < y : {
    x = x + 5
    if x == 15 : {
        print("El valor objetivo es:")
        print(x)
    }
}
print("Fin del programa")
