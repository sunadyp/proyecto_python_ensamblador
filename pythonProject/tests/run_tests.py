import sys
import os
import glob


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))


from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

# Archivos generados por ANTLR
from PythonSubsetLexer import PythonSubsetLexer
from PythonSubsetParser import PythonSubsetParser


from VisitanteSemantico import VisitanteSemantico
from CodigoIntermedio import VisitanteIntermedio
from Optimizador import Optimizador
from GeneradorMIPS import GeneradorMIPS



class ThrowingErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error Sintáctico en línea {line}:{column} - {msg}")


def run_test(file_path, expect_failure=False):
    filename = os.path.basename(file_path)
    print(f"Testing {filename:<35} ...", end=" ")

    try:
        # 1. Leer el archivo .txt
        input_stream = FileStream(file_path, encoding='utf-8')

        # 2. Lexer
        lexer = PythonSubsetLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(ThrowingErrorListener())

        stream = CommonTokenStream(lexer)

        # 3. Parser
        parser = PythonSubsetParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ThrowingErrorListener())

        tree = parser.program()

        # 4. Semántico
        semantico = VisitanteSemantico()
        semantico.visit(tree)

        # 5. Intermedio
        intermedio = VisitanteIntermedio()
        intermedio.visit(tree)

        # 6. Optimización
        optimizador = Optimizador()
        cuadruplos = optimizador.optimizar(intermedio.cuadruplos)


        mips = GeneradorMIPS()

        mips.recolectar_variables(cuadruplos)

        if expect_failure:
            print(" FAIL (Se esperaba un error pero compiló con éxito)")
            return False
        else:
            print(" PASS")
            return True

    except Exception as e:
        if expect_failure:
            # Mostramos el error completo
            err_msg = str(e)
            print(f" (Error detectado: {err_msg})")
            return True
        else:
            print(f"FAIL - {e}")
            return False


# -----------------------------------------------------------
# FUNCIÓN PRINCIPAL
# -----------------------------------------------------------
def main():
    base_dir = os.path.dirname(__file__)

    # Rutas a las carpetas
    valid_path = os.path.join(base_dir, '..', 'examples', 'valid', '*.txt')
    invalid_path = os.path.join(base_dir, '..', 'examples', 'invalid', '*.txt')

    valid_files = glob.glob(valid_path)
    invalid_files = glob.glob(invalid_path)

    passed_count = 0
    total_files = len(valid_files) + len(invalid_files)

    if total_files == 0:
        print("⚠️ No se encontraron archivos en examples/valid/ ni examples/invalid/")
        return

    # 1. EJECUTAR CASOS VÁLIDOS
    if valid_files:
        print(f"\n=== PRUEBAS VÁLIDAS ({len(valid_files)}) ===")
        for f in valid_files:
            if run_test(f, expect_failure=False):
                passed_count += 1

    # 2. EJECUTAR CASOS INVÁLIDOS
    if invalid_files:
        print(f"\n=== PRUEBAS INVÁLIDAS ({len(invalid_files)}) ===")
        for f in invalid_files:
            if run_test(f, expect_failure=True):
                passed_count += 1

    # 3. RESUMEN
    print("-" * 50)
    print(f"RESUMEN FINAL: {passed_count}/{total_files} pruebas pasaron.")

    if passed_count == total_files:
        print("Pruebas Pasadas")
    else:
        print("Casos Con fallas.")


if __name__ == '__main__':
    main()