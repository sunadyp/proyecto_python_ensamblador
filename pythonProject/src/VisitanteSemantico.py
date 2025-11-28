from PythonSubsetVisitor import PythonSubsetVisitor
from Tabla_de_Simbolos import TablaSimbolos

class VisitanteSemantico(PythonSubsetVisitor):
    def __init__(self):
        self.tabla_simbolos = TablaSimbolos()

    # --- Visitante del Programa Principal ---
    def visitProgram(self, ctx):
        self.visitChildren(ctx)

    # --- Visitante de Definición de Funciones ---
    def visitFunctionDef(self, ctx):
        nombre_funcion = ctx.ID().getText()
        self.tabla_simbolos.definir(nombre_funcion, 'FUNCION')

        self.tabla_simbolos.crear_alcance()

        if ctx.parameterList():
            for param in ctx.parameterList().ID():
                nombre_parametro = param.getText()
                self.tabla_simbolos.definir(nombre_parametro, 'PARAMETRO')

        self.visit(ctx.block())
        self.tabla_simbolos.salir_alcance()

    # --- Visitante de Asignaciones ---
    def visitAssignmentStmt(self, ctx):
        nombre_variable = ctx.ID().getText()

        # Primero visitamos la expresión para validar que las variables usadas existan
        self.visit(ctx.expression())

        self.tabla_simbolos.definir(nombre_variable, 'ENTERO')

    # --- Visitante de Identificadores en Expresiones ---
    def visitId(self, ctx):
        nombre_variable = ctx.getText()

        info_tipo = self.tabla_simbolos.buscar(nombre_variable)

        # 1. Verificamos existencia
        if info_tipo is None:
            linea = ctx.start.line
            raise Exception(f"Error Semántico en línea {linea}: La variable '{nombre_variable}' no ha sido definida.")

        # 2. Verificamos que NO sea una función usada sin paréntesis
        if info_tipo == 'FUNCION':
            linea = ctx.start.line
            raise Exception(
                f"Error Semántico en línea {linea}: '{nombre_variable}' es una función, no una variable. ¿Olvidaste los paréntesis ()?")

        return self.visitChildren(ctx)