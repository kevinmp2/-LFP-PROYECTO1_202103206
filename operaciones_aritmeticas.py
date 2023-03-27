from abstraccion import Expresion

global cadena 
cadena = ''
global contador
contador = 0

class Aritmetica(Expresion):
    def __init__(self, lado_izquierdo, lado_derecho, tipo_operacion, fila , columna):
        self.lado_izquierdo = lado_izquierdo
        self.lado_derecho = lado_derecho 
        self.tipo_operacion = tipo_operacion
        self.valor = 0
        super().__init__(fila, columna)
    
    def append(self):
        global cadena
        return cadena
    
    def vaciar(self):
        global cadena
        cadena = ''
    
    def operar(self, arbol):
        operacion = ''
        lado_izquierdo_value = ''
        lado_derecho_value = ''

        global cadena
        global contador
        
        if self.lado_izquierdo != None:
            lado_izquierdo_value = self.lado_izquierdo.operar(arbol)
            operacion = self.tipo_operacion.operar(arbol)

        if self.lado_derecho != None:
            lado_derecho_value = self.lado_derecho.operar(arbol)
            operacion = self.tipo_operacion.operar(arbol)

        if self.tipo_operacion.operar(arbol) == 'Suma':
            resultado = lado_izquierdo_value + lado_derecho_value
            self.valor = resultado
            return resultado
        
        elif self.tipo_operacion.operar(arbol) == 'Resta':
            resultado = lado_izquierdo_value - lado_derecho_value
            self.valor = resultado
            return resultado
        
        elif self.tipo_operacion.operar(arbol) == 'Multiplicacion':
            resultado = lado_izquierdo_value * lado_derecho_value
            self.valor = resultado
            return resultado
        
        elif self.tipo_operacion.operar(arbol) == 'Division':
            resultado = lado_izquierdo_value / lado_derecho_value
            self.valor = resultado
            return resultado
        
        elif self.tipo_operacion.operar(arbol) == 'Modulo':
            resultado = lado_izquierdo_value % lado_derecho_value
            self.valor = resultado
            return resultado
        
        elif self.tipo_operacion.operar(arbol) == 'Potencia':
            resultado = lado_izquierdo_value ** lado_derecho_value
            self.valor = resultado
            return resultado
        
        elif self.tipo_operacion.operar(arbol) == 'Raiz':
            resultado = lado_izquierdo_value ** (1/lado_derecho_value)
            self.valor = resultado
            return resultado
        
        elif self.tipo_operacion.operar(arbol) == 'Inverso':
            resultado = (1/lado_izquierdo_value) 
            return resultado
        else:
            return 0
    
    def get_fila(self):
        return super().get_fila
    
    def get_columna(self):
        return super().get_columna