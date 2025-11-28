class Optimizador:
    def __init__(self):
        self.constantes = {}

    def es_numero(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def es_temporal(self, s):
        return s and s.startswith('T') and s[1:].isdigit()

    def optimizar(self, lista_cuadruplos):
        cuadruplos_optimizados = []

        for cuad in lista_cuadruplos:
            # 1. PROPAGACIÓN DE CONSTANTES
            if cuad.arg1 in self.constantes:
                cuad.arg1 = self.constantes[cuad.arg1]

            if cuad.arg2 in self.constantes:
                cuad.arg2 = self.constantes[cuad.arg2]

            # 2. PLEGADO DE CONSTANTES
            if cuad.op in ['+', '-', '*', '/'] and self.es_numero(cuad.arg1) and self.es_numero(cuad.arg2):

                resultado = 0
                val1 = float(cuad.arg1)
                val2 = float(cuad.arg2)

                if cuad.op == '+':
                    resultado = val1 + val2
                elif cuad.op == '-':
                    resultado = val1 - val2
                elif cuad.op == '*':
                    resultado = val1 * val2
                elif cuad.op == '/':
                    resultado = val1 / val2

                if resultado.is_integer():
                    resultado = int(resultado)

                cuad.op = '='
                cuad.arg1 = str(resultado)
                cuad.arg2 = None

                if self.es_temporal(cuad.res):
                    self.constantes[cuad.res] = str(resultado)

            elif cuad.op == '=' and self.es_numero(cuad.arg1):
                if self.es_temporal(cuad.res):
                    self.constantes[cuad.res] = cuad.arg1

            cuadruplos_optimizados.append(cuad)

        return cuadruplos_optimizados