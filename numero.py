from abstraccion import Expresion

# Hereda del objeto expresion
class Numero(Expresion):
    def __init__(self, valor, fila, columna):
        self.valor = valor
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.valor
    
    def get_fila(self):
        return super().get_fila
    
    def get_columna(self):
        return super().get_columna
    
    