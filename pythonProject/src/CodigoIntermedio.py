from PythonSubsetVisitor import PythonSubsetVisitor


class Cuadruplo:
    def __init__(self, op, arg1, arg2, res):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.res = res

    def __repr__(self):
        return f"({self.op}, {self.arg1}, {self.arg2}, {self.res})"


class VisitanteIntermedio(PythonSubsetVisitor):
    def __init__(self):
        self.cuadruplos = []
        self.contador_temporales = 0
        self.contador_etiquetas = 0

    def nuevo_temporal(self):
        self.contador_temporales += 1
        return f"T{self.contador_temporales}"

    def nueva_etiqueta(self):
        """Genera etiquetas para saltos (GOTO): L1, L2..."""
        self.contador_etiquetas += 1
        return f"L{self.contador_etiquetas}"

    # --- MANEJO DE VALORES ---

    def visitNumber(self, ctx):
        # Si vemos un número, simplemente retornamos su texto (ej: "5")
        return ctx.getText()

    def visitId(self, ctx):
        # Si vemos una variable, retornamos su nombre (ej: "x")
        return ctx.getText()

    def visitStringLiteral(self, ctx):
        # Devuelve el texto con comillas
        return ctx.getText()

    # --- OPERACIONES ARITMÉTICAS ---

    def visitMulDiv(self, ctx):
        # 1. Visitar hijos recursivamente para obtener sus direcciones
        izq = self.visit(ctx.expression(0))  # Lado izquierdo
        der = self.visit(ctx.expression(1))  # Lado derecho

        # 2. Crear temporal para guardar resultado
        temporal = self.nuevo_temporal()

        # 3. Obtener operador (* o /)
        op = ctx.getChild(1).getText()

        # 4. Generar Cuádruplo
        self.cuadruplos.append(Cuadruplo(op, izq, der, temporal))

        # 5. Retornar el nombre del temporal para que lo use el padre
        return temporal

    def visitAddSub(self, ctx):
        izq = self.visit(ctx.expression(0))
        der = self.visit(ctx.expression(1))
        temporal = self.nuevo_temporal()
        op = ctx.getChild(1).getText()
        self.cuadruplos.append(Cuadruplo(op, izq, der, temporal))
        return temporal

    # --- ASIGNACIÓN ---

    def visitAssignmentStmt(self, ctx):
        nombre_variable = ctx.ID().getText()

        # Visitamos la expresión de la derecha para obtener el valor/temporal final
        valor = self.visit(ctx.expression())

        # Generamos cuádruplo de asignación
        self.cuadruplos.append(Cuadruplo('=', valor, None, nombre_variable))

    # --- PRINT ---
    def visitPrintStmt(self, ctx):
        valor = self.visit(ctx.expression())
        self.cuadruplos.append(Cuadruplo('PRINT', valor, None, None))

    # --- PARÉNTESIS ---
    def visitParens(self, ctx):
        # Simplemente visitamos la expresión de adentro y devolvemos su resultado.
        return self.visit(ctx.expression())

    # --- COMPARACIONES (>, <, ==) ---
    def visitRelational(self, ctx):
        izq = self.visit(ctx.expression(0))
        der = self.visit(ctx.expression(1))
        temporal = self.nuevo_temporal()
        op = ctx.getChild(1).getText()  # >, <, ==

        self.cuadruplos.append(Cuadruplo(op, izq, der, temporal))
        return temporal

    # --- IF STATEMENT ---
    def visitIfStmt(self, ctx):
        # if expresion : statement (else : statement)?

        # 1. Evaluar la condición
        condicion = self.visit(ctx.expression())

        # 2. Generar etiqueta para SALIR (o ir al else)
        etiqueta_falso = self.nueva_etiqueta()  # L1

        # 3. Generar salto
        self.cuadruplos.append(Cuadruplo('IF_FALSE', condicion, None, etiqueta_falso))

        # 4. Generar el código del bloque verdadero
        self.visit(ctx.statement(0))

        # Revisar si hay else
        if len(ctx.statement()) > 1:
            etiqueta_fin = self.nueva_etiqueta()

            # Al terminar el bloque True, saltamos al final para no ejecutar el Else
            self.cuadruplos.append(Cuadruplo('GOTO', None, None, etiqueta_fin))

            self.cuadruplos.append(Cuadruplo('LABEL', None, None, etiqueta_falso))

            self.visit(ctx.statement(1))

            # Ponemos la etiqueta del final
            self.cuadruplos.append(Cuadruplo('LABEL', None, None, etiqueta_fin))
        else:
            # Si no hay else, simplemente ponemos la etiqueta de salida aquí
            self.cuadruplos.append(Cuadruplo('LABEL', None, None, etiqueta_falso))

    # --- WHILE STATEMENT ---
    def visitWhileStmt(self, ctx):
        etiqueta_inicio = self.nueva_etiqueta()
        etiqueta_fin = self.nueva_etiqueta()

        # 1. Poner etiqueta de inicio
        self.cuadruplos.append(Cuadruplo('LABEL', None, None, etiqueta_inicio))

        condicion = self.visit(ctx.expression())

        # 3. Si es falso, salimos del ciclo
        self.cuadruplos.append(Cuadruplo('IF_FALSE', condicion, None, etiqueta_fin))

        # 4. Ejecutar el cuerpo del ciclo
        self.visit(ctx.statement())

        # 5. Volver al inicio automáticamente
        self.cuadruplos.append(Cuadruplo('GOTO', None, None, etiqueta_inicio))

        # 6. Etiqueta de salida
        self.cuadruplos.append(Cuadruplo('LABEL', None, None, etiqueta_fin))