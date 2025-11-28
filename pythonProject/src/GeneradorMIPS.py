class GeneradorMIPS:
    def __init__(self):
        self.variables = set()
        self.cadenas = {}
        self.contador_cadenas = 0

    def es_numero(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def es_cadena(self, s):
        return s and s.startswith('"') and s.endswith('"')

    def recolectar_variables(self, lista_cuadruplos):

        for cuad in lista_cuadruplos:
            # --- 1. RECOLECCIÓN DE VARIABLES NUMÉRICAS ---
            for arg in [cuad.arg1, cuad.arg2, cuad.res]:
                # Debe existir, NO ser número, NO ser string
                if arg and not self.es_numero(arg) and not self.es_cadena(arg):
                    if cuad.op in ['LABEL', 'GOTO', 'IF_FALSE'] and arg == cuad.res:
                        continue  # Es una etiqueta, ignorar

                    self.variables.add(arg)

            # --- 2. RECOLECCIÓN DE CADENAS (STRINGS) ---
            if self.es_cadena(cuad.arg1) and cuad.arg1 not in self.cadenas:
                self.contador_cadenas += 1
                etiqueta = f"str_{self.contador_cadenas}"
                self.cadenas[cuad.arg1] = etiqueta

    def generar(self, lista_cuadruplos, nombre_archivo="resultado.asm"):
        self.recolectar_variables(lista_cuadruplos)

        with open(nombre_archivo, 'w') as f:
            # --- SECCIÓN DE DATOS (.data) ---
            f.write(".data\n")

            # 1. Declarar Variables Numéricas (.word)
            for var in self.variables:
                f.write(f"    {var}: .word 0\n")

            # 2. Declarar Cadenas (.asciiz)
            for contenido, etiqueta in self.cadenas.items():
                f.write(f"    {etiqueta}: .asciiz {contenido}\n")

            # --- SECCIÓN DE CÓDIGO (.text) ---
            f.write("\n.text\n")
            f.write("main:\n")

            for cuad in lista_cuadruplos:
                f.write(f"    # {cuad}\n")
                op = cuad.op

                # --- OPERACIONES ARITMÉTICAS ---
                if op in ['+', '-', '*', '/', '<', '>', '==']:
                    # Cargar Operando 1
                    if self.es_numero(cuad.arg1):
                        f.write(f"    li $t0, {cuad.arg1}\n")
                    else:
                        f.write(f"    lw $t0, {cuad.arg1}\n")

                    # Cargar Operando 2
                    if self.es_numero(cuad.arg2):
                        f.write(f"    li $t1, {cuad.arg2}\n")
                    else:
                        f.write(f"    lw $t1, {cuad.arg2}\n")

                    # Operar
                    if op == '+':
                        f.write("    add $t2, $t0, $t1\n")
                    elif op == '-':
                        f.write("    sub $t2, $t0, $t1\n")
                    elif op == '*':
                        f.write("    mul $t2, $t0, $t1\n")
                    elif op == '/':
                        f.write("    div $t0, $t1\n")
                        f.write("    mflo $t2\n")
                    elif op == '<':
                        f.write("    slt $t2, $t0, $t1\n")
                    elif op == '>':
                        f.write("    sgt $t2, $t0, $t1\n")
                    elif op == '==':
                        f.write("    seq $t2, $t0, $t1\n")

                    # Guardar resultado
                    f.write(f"    sw $t2, {cuad.res}\n")

                # --- ASIGNACIÓN (=) ---
                elif op == '=':
                    if self.es_numero(cuad.arg1):
                        f.write(f"    li $t0, {cuad.arg1}\n")
                    else:
                        f.write(f"    lw $t0, {cuad.arg1}\n")
                    f.write(f"    sw $t0, {cuad.res}\n")

                # --- PRINT (Manejo híbrido String/Int) ---
                elif op == 'PRINT':
                    # CASO A: Imprimir Texto
                    if self.es_cadena(cuad.arg1):
                        f.write("    li $v0, 4\n")  # Syscall 4: Print String
                        etiqueta = self.cadenas[cuad.arg1]  # Recuperar etiqueta (str_1)
                        f.write(f"    la $a0, {etiqueta}\n")  # Cargar dirección

                    # CASO B: Imprimir Número
                    else:
                        f.write("    li $v0, 1\n")
                        if self.es_numero(cuad.arg1):
                            f.write(f"    li $a0, {cuad.arg1}\n")
                        else:
                            f.write(f"    lw $a0, {cuad.arg1}\n")

                    f.write("    syscall\n")

                    f.write("    li $a0, 10\n")
                    f.write("    li $v0, 11\n")
                    f.write("    syscall\n")

                # --- SALTOS Y ETIQUETAS ---
                elif op == 'LABEL':
                    f.write(f"{cuad.res}:\n")

                elif op == 'GOTO':
                    f.write(f"    j {cuad.res}\n")

                elif op == 'IF_FALSE':
                    if self.es_numero(cuad.arg1):
                        f.write(f"    li $t0, {cuad.arg1}\n")
                    else:
                        f.write(f"    lw $t0, {cuad.arg1}\n")
                    f.write(f"    beqz $t0, {cuad.res}\n")

            f.write("\n    # Fin del programa\n")
            f.write("    li $v0, 10\n")
            f.write("    syscall\n")