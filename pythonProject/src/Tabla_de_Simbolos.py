class TablaSimbolos:
    def __init__(self):
        self.pila_alcances = [{}]

    def crear_alcance(self):
        """Crea un nuevo nivel de alcance"""
        self.pila_alcances.append({})

    def salir_alcance(self):
        """Destruye el alcance actual)"""
        self.pila_alcances.pop()

    def definir(self, nombre, tipo_info):
        """Guarda una variable en el alcance actual"""
        scope = self.pila_alcances[-1]
        scope[nombre] = tipo_info
        print(f"DEBUG: Definida variable '{nombre}' de tipo '{tipo_info}' en alcance nivel {len(self.pila_alcances)}")

    def buscar(self, nombre):
        """Busca una variable. Empieza en el alcance actual y va subiendo hasta el global."""
        for scope in reversed(self.pila_alcances):
            if nombre in scope:
                return scope[nombre]
        return None # No encontrada