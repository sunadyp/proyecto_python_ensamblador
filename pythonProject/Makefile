PYTHON = python

ANTLR_JAR = lib/antlr-4.13.1-complete.jar

SRC_DIR = src
TEST_DIR = tests
EXAMPLES_DIR = examples

all: grammar test

grammar:
	@echo "Generando archivos de ANTLR en src..."
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor -no-listener -o src $(SRC_DIR)/PythonSubset.g4

test:
	@echo "Ejecutando suite de pruebas..."
	$(PYTHON) $(TEST_DIR)/run_tests.py

expected:
	@echo "Generando salidas esperadas (.asm)..."
	$(PYTHON) $(EXAMPLES_DIR)/expected/generate_expected.py

install:
	pip install antlr4-python3-runtime

clean:
	@echo "Limpiando archivos generados..."
	rm -f $(SRC_DIR)/*Lexer.py $(SRC_DIR)/*Parser.py $(SRC_DIR)/*Visitor.py $(SRC_DIR)/*.tokens $(SRC_DIR)/*.interp

help:
	@echo "Comandos disponibles:"
	@echo "  make grammar   - Compila la gramatica .g4 a Python"
	@echo "  make test      - Ejecuta los tests validos e invalidos"
	@echo "  make expected  - Regenera los .asm en examples/expected"
	@echo "  make clean     - Borra los archivos generados por ANTLR"
	@echo "  make install   - Instala librerias de Python necesarias"