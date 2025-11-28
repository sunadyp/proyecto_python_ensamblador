# ==========================================
# VARIABLES
# ==========================================
# El intérprete de Python (en Windows suele ser 'python', en Linux 'python3')
PYTHON = python

# Ruta al JAR de ANTLR
ANTLR_JAR = lib/antlr-4.13.1-complete.jar

# Directorios
SRC_DIR = src
TEST_DIR = tests
EXAMPLES_DIR = examples

# ==========================================
# REGLAS (TARGETS)
# ==========================================

# Regla por defecto (si solo escribes 'make')
all: grammar test

# 1. Generar el Compilador (Lexer, Parser, Visitor) desde la gramática
grammar:
	@echo "Generando archivos de ANTLR en src..."
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor -no-listener -o src $(SRC_DIR)/PythonSubset.g4

# 2. Ejecutar las Pruebas Automatizadas
test:
	@echo "Ejecutando suite de pruebas..."
	$(PYTHON) $(TEST_DIR)/run_tests.py

# 3. Generar los archivos ASM esperados (Script nuevo)
expected:
	@echo "Generando salidas esperadas (.asm)..."
	$(PYTHON) $(EXAMPLES_DIR)/expected/generate_expected.py

# 4. Instalar dependencias necesarias
install:
	pip install antlr4-python3-runtime

# 5. Limpiar archivos generados (Para empezar de cero)
# NOTA: Este comando usa sintaxis de Linux/Git Bash (rm).
# Si usas CMD de Windows puro, ver nota abajo.
clean:
	@echo "Limpiando archivos generados..."
	rm -f $(SRC_DIR)/*Lexer.py $(SRC_DIR)/*Parser.py $(SRC_DIR)/*Visitor.py $(SRC_DIR)/*.tokens $(SRC_DIR)/*.interp

# Ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make grammar   - Compila la gramatica .g4 a Python"
	@echo "  make test      - Ejecuta los tests validos e invalidos"
	@echo "  make expected  - Regenera los .asm en examples/expected"
	@echo "  make clean     - Borra los archivos generados por ANTLR"
	@echo "  make install   - Instala librerias de Python necesarias"