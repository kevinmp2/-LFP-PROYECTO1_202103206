from abstraccion import Expresion

class Lexema(Expresion):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.lexema

    def get_fila(self):
        return super().get_fila
    
    def get_columna(self):
        return super().get_columna
    
    
    
    