import sys
import os
import glob

# 1. AJUSTE DE IMPORTACIÓN:
# Como estamos en 'examples/expected', debemos subir 2 niveles (..)
# para llegar a la raíz y luego entrar a 'src'.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from antlr4 import *
from src.PythonSubsetLexer import PythonSubsetLexer
from src.PythonSubsetParser import PythonSubsetParser
from SemanticVisitor import SemanticVisitor
from IntermediateCode import IntermediateVisitor
from Optimizer import Optimizer
from MIPSGenerator import MIPSGenerator


def compile_file(input_path, output_path):
    # (Esta función se queda IGUAL, no cambian rutas internas)
    print(f"Compilando {os.path.basename(input_path)} -> {os.path.basename(output_path)}...")

    try:
        input_stream = FileStream(input_path, encoding='utf-8')
        lexer = PythonSubsetLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PythonSubsetParser(stream)
        tree = parser.program()

        semantic = SemanticVisitor()
        semantic.visit(tree)

        intermediate = IntermediateVisitor()
        intermediate.visit(tree)

        optimizer = Optimizer()
        quads = optimizer.optimize(intermediate.quadruples)

        mips = MIPSGenerator()
        mips.generate(quads, output_path)

        print("✅ Generado con éxito.")

    except Exception as e:
        print(f"❌ Error al compilar: {e}")


def main():
    # base_dir ahora es: .../proyecto/examples/expected
    base_dir = os.path.dirname(__file__)

    # 2. AJUSTE DE RUTAS DE ENTRADA/SALIDA:

    # La carpeta 'valid' está en el directorio hermano (subir uno y entrar a valid)
    valid_dir = os.path.join(base_dir, '..', 'valid')

    # La carpeta 'expected' es DONDE ESTAMOS AHORA MISMO
    expected_dir = base_dir

    # Buscar todos los .txt en valid
    # (os.path.abspath ayuda a limpiar la ruta visualmente si hay muchos "..")
    input_files = glob.glob(os.path.abspath(os.path.join(valid_dir, '*.txt')))

    if not input_files:
        print(f"No se encontraron archivos en: {os.path.abspath(valid_dir)}")
        return

    print(f"=== Generando {len(input_files)} archivos ASM en carpeta actual ===\n")

    for input_file in input_files:
        filename = os.path.basename(input_file)
        name_without_ext = os.path.splitext(filename)[0]

        # Guardamos directamente en la carpeta actual (expected_dir)
        output_file = os.path.join(expected_dir, name_without_ext + ".asm")

        compile_file(input_file, output_file)

    print("\n=== ¡Listo! Archivos generados en esta carpeta. ===")


if __name__ == '__main__':
    main()