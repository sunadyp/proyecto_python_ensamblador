import sys
import os
import glob



sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))


from antlr4 import *

from PythonSubsetLexer import PythonSubsetLexer
from PythonSubsetParser import PythonSubsetParser


from VisitanteSemantico import VisitanteSemantico
from CodigoIntermedio import VisitanteIntermedio
from Optimizador import Optimizador
from GeneradorMIPS import GeneradorMIPS


def compile_file(input_path, output_path):
    print(f"Compilando {os.path.basename(input_path)} -> {os.path.basename(output_path)}...")

    try:
        # A. ANTLR
        input_stream = FileStream(input_path, encoding='utf-8')
        lexer = PythonSubsetLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PythonSubsetParser(stream)
        tree = parser.program()


        semantico = VisitanteSemantico()
        semantico.visit(tree)


        intermedio = VisitanteIntermedio()
        intermedio.visit(tree)


        optimizador = Optimizador()

        cuadruplos = optimizador.optimizar(intermedio.cuadruplos)


        mips = GeneradorMIPS()

        mips.generar(cuadruplos, output_path)

        print(" Generado con éxito.")

    except Exception as e:
        print(f"❌ Error al compilar: {e}")


def main():
    # Directorio actual (examples/expected)
    base_dir = os.path.dirname(__file__)

    # Directorio de entrada (examples/valid)
    valid_dir = os.path.join(base_dir, '..', 'valid')

    # Directorio de salida (el actual)
    expected_dir = base_dir

    # Buscar archivos .txt
    input_files = glob.glob(os.path.abspath(os.path.join(valid_dir, '*.txt')))

    if not input_files:
        print(f"No se encontraron archivos en: {os.path.abspath(valid_dir)}")
        return

    print(f"=== Generando {len(input_files)} archivos ASM en carpeta actual ===\n")

    for input_file in input_files:
        # Calcular nombre de salida
        filename = os.path.basename(input_file)
        name_without_ext = os.path.splitext(filename)[0]
        output_file = os.path.join(expected_dir, name_without_ext + ".asm")

        compile_file(input_file, output_file)

    print("\n=== ¡Listo! Revisa los archivos .asm generados. ===")


if __name__ == '__main__':
    main()