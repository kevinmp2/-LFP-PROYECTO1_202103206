from abc import ABC, abstractmethod

class Expresion(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    @abstractmethod 
    def operar(self, arbol):
        pass

    @abstractmethod
    def get_fila(self):
        return self.fila

    @abstractmethod
    def get_columna(self):
        return self.columna

