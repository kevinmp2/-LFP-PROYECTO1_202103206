from abstraccion import Expresion
from math import *

class Trigonometricas(Expresion):
    def __init__(self, lado_izquierdo, tipo_operacion, fila, columna):
        self.lado_izquierdo = lado_izquierdo
        self.tipo_operacion = tipo_operacion
        self.angulo = 0
        self.valor = 0
        super().__init__(fila, columna)

    def append(self):
        global cadena
        return cadena
    
    def vaciar(self):
        global cadena
        cadena = ''

    def operar(self, arbol):
        lado_izquierdo_value = ''

        global cadena
        global contador

        if self.lado_izquierdo != None:
            lado_izquierdo_value = self.lado_izquierdo.operar(arbol)
            operacion = self.tipo_operacion.operar(arbol)

        if self.tipo_operacion.operar(arbol) == 'Seno':
            self.angulo = lado_izquierdo_value
            resultado = sin((lado_izquierdo_value * (pi/180)))
            self.valor = resultado
            return resultado
        
        if self.tipo_operacion.operar(arbol) == 'Coseno':
            self.angulo = lado_izquierdo_value
            resultado = cos((lado_izquierdo_value * (pi/180)))
            self.valor = resultado
            return resultado
        
        if self.tipo_operacion.operar(arbol) == 'Tangente':
            self.angulo = lado_izquierdo_value
            resultado = tan((lado_izquierdo_value * (pi/180)))
            self.valor = resultado
            return resultado
        else:
            return None
        
    def get_fila(self):
        return super().get_fila
    
    def get_columna(self):
        return super().get_columna