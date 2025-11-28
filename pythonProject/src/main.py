import sys
from antlr4 import *
from PythonSubsetLexer import PythonSubsetLexer
from PythonSubsetParser import PythonSubsetParser

from VisitanteSemantico import VisitanteSemantico
from CodigoIntermedio import VisitanteIntermedio
from Optimizador import Optimizador
from GeneradorMIPS import GeneradorMIPS


def main(argv):
    codigo_fuente = """
    x = 0
    y = (10 + 20) / 2  # Esto se optimizará a 15

    print("Iniciando ciclo")

    while x < y : {
        x = x + 5
        if x == 15 : {
            print("El valor objetivo es:")
            print(x)
        }
    }
    print("Fin del programa")
    """

    print("=== COMPILADOR PYTHON -> MIPS ===")

    # ANTLR (Lexer y Parser)
    input_stream = InputStream(codigo_fuente)
    lexer = PythonSubsetLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PythonSubsetParser(stream)
    tree = parser.program()

    # Análisis Semántico
    print("\n[1] Verificando Semántica...")
    try:
        semantico = VisitanteSemantico()
        semantico.visit(tree)
        print("Semántica Correcta.")
    except Exception as e:
        print(f"Error Semántico: {e}")
        return

    # 2. Código Intermedio
    print("\n[2] Generando Cuádruplos...")
    intermedio = VisitanteIntermedio()
    intermedio.visit(tree)
    # NOTA: La variable interna ahora se llama 'cuadruplos'
    lista_cuadruplos = intermedio.cuadruplos

    # Imprimir para debug visual
    for i, c in enumerate(lista_cuadruplos):
        print(f"    {i}: {c}")

    # 3. Optimización
    print("\n[3] Optimizando...")
    optimizador = Optimizador()
    cuadruplos_optimizados = optimizador.optimizar(lista_cuadruplos)

    # Imprimir optimizados
    print("    --- Cuádruplos Optimizados ---")
    for i, c in enumerate(cuadruplos_optimizados):
        print(f"    {i}: {c}")

    # 4. Generación de MIPS
    print("\n[4] Generando MIPS (.asm)...")
    generador = GeneradorMIPS()
    generador.generar(cuadruplos_optimizados, "resultado.asm")

    print("\nÉxito! Archivo 'resultado.asm' generado.")


if __name__ == '__main__':
    main(sys.argv)