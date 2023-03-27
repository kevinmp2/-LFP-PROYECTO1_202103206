from operaciones_aritmeticas import *
from operaciones_trigonometricas import *
from errores import *
from lexema import *
from numero import Numero
import json

# Analizador lexico

# Patron, Lexema y Token

reservadas = {
    'ROperacion'       : 'Operacion',
    'Rvalor1'          : 'Valor1',
    'Rvalor2'          : 'Valor2',
    'Rsuma'            : 'Suma',
    'Rresta'           : 'Resta',
    'Rmultiplicacion'  : 'Multiplicacion',
    'Rdivision'        : 'Division',
    'Rpotencia'        : 'Potencia',
    'Rraiz'            : 'Raiz',
    'Rinverso'         : 'Inverso',
    'Rseno'            : 'Seno',
    'Rcoseno'          : 'Coseno',
    'Rtangente'        : 'Tangente',
    'Rmodulo'          : 'Modulo',
    'Rtexto'           : 'Texto',
    'Rcolorfondonodo'  : 'Color-Fondo-Nodo',
    'Rcolorfuentenodo' : 'Color-Fuente-Nodo',
    'Rcolorformanodo'  : 'Forma-Nodo',
    'coma'             : ',',
    'punto'            : '.',
    'dospuntos'        : ':',
    'corcheteizq'      : '[',
    'corchetederech'   : ']',
    'llaveizq'         : '{',
    'llavederech'      : '}',
}

# conversion de diccionario a lista

global lexemas
lexemas = list(reservadas.values())
global numero_de_lineas
global numero_de_columnas
global instrucciones
global lista_de_lexemas
global errores
global lista_de_errores


numero_de_lineas = 1
numero_de_columnas = 1
lista_de_lexemas = []
instruccion = []
errores = 0
lista_de_errores = []


def instruccion(cadena):
    global numero_de_lineas
    global numero_de_columnas
    global lista_de_lexemas

    lexema = ''
    puntero = 0

    while cadena:
        char = cadena[puntero]
        puntero += 1

        if char == '\"':
            lexema, cadena = creacion_lexema(cadena[puntero:])
            if lexema and cadena:
                numero_de_columnas += 1
                # Clase
                l = Lexema(lexema, numero_de_lineas, numero_de_columnas)

                # Agregamos el lexema a la lista de lexemas
                lista_de_lexemas.append(l)
                numero_de_columnas += len(lexema) + 1
                puntero = 0

        elif char.isdigit():
            token, cadena = creacion_numero(cadena)
            if token and cadena:
                numero_de_columnas += 1
                # Clase lexema
                n = Numero(token, numero_de_lineas, numero_de_columnas)
                # Agregamos el lexema a la lista de lexemas
                lista_de_lexemas.append(n)
                numero_de_columnas += len(str(token)) + 1
                puntero = 0

        elif char == '[' or char == ']':
            # Clase lexema
            c = Lexema(char, numero_de_lineas, numero_de_columnas)
            # Agregamos el lexema a la lista de lexemas
            lista_de_lexemas.append(c)
            numero_de_columnas += 1
            cadena = cadena[1:]
            puntero = 0

        elif char == '\t':
            numero_de_columnas += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            numero_de_lineas += 1
            numero_de_columnas = 1
        else:
            cadena = cadena[1:]
            puntero = 0
            numero_de_columnas += 1
    return lista_de_lexemas


def creacion_lexema(cadena):
    global numero_de_lineas
    global numero_de_columnas
    global lista_de_lexemas

    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None


def creacion_numero(cadena):
    numero = ''
    puntero = ''
    es_decimal = False

    for char in cadena:
        puntero += char
        if char == '.':
            es_decimal = True
        if char == '\"' or char == ' ' or char == '\n' or char == '\t' or char == ']':
            if es_decimal:
                return float(numero), cadena[len(puntero) - 1:]
            else:
                return int(numero), cadena[len(puntero) - 1:]
        else:
            numero += char
    return None, None


def operar():
    global lista_de_lexemas
    global instruccion

    operacion = ''

    n1 = ''
    n2 = ''

    while lista_de_lexemas:
        lexema = lista_de_lexemas.pop(0)
        if lexema.operar(None) == 'Operacion':
            operacion = lista_de_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_de_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_de_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()

        if operacion and n1 and n2:
            return Aritmetica(n1, n2, operacion, f'inicio: {operacion.get_fila()}: {operacion.get_columna()}', f'fin: {n2.get_fila()}: {n2.get_columna}')

        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return Trigonometricas(n1, operacion, f'inicio: {operacion.get_fila()}: {operacion.get_columna()}', f'fin: {n1.get_fila()}: {n1.get_columna()}')
    return None


def operacion_recursividad():
    instruccion = []

    while True:
        operacion = operar()
        if operacion:
            instruccion.append(operacion)
        else:
            break
    return instruccion


def anidar_arbol(indice, identificador, etiqueta_operacion, objeto_operacion):
    dot = ''
    if objeto_operacion:
        if type(objeto_operacion) == Numero:
            print(objeto_operacion.valor)
            dot += f'nodo_{indice}_{identificador}{etiqueta_operacion}[label = "{objeto_operacion.valor}"];\n'
        if type(objeto_operacion) == Trigonometricas:
            print(objeto_operacion.tipo_operacion.lexema)
            print(objeto_operacion.valor) 
            dot += f'nodo_{indice}_{identificador}{etiqueta_operacion}[label = "{objeto_operacion.tipo_operacion.lexema}\n{objeto_operacion.valor}"];\n'
            dot += anidar_arbol(indice,identificador + 1,etiqueta_operacion + "_angulo",objeto_operacion.lado_izquierdo)
            dot += f'nodo_{indice}_{identificador}{etiqueta_operacion} -> nodo_{indice}_{identificador + 1}{etiqueta_operacion}_angulo;\n'
        if type(objeto_operacion) == Aritmetica:
            print(objeto_operacion.tipo_operacion.lexema)
            print(objeto_operacion.valor)
            dot += f'nodo_{indice}_{identificador}{etiqueta_operacion}[label = "{objeto_operacion.tipo_operacion.lexema}\n{objeto_operacion.valor}"];\n'
            dot += anidar_arbol(indice,identificador + 1,etiqueta_operacion + "_izquierda",objeto_operacion.lado_izquierdo)
            dot += f'nodo_{indice}_{identificador}{etiqueta_operacion} -> nodo_{indice}_{identificador + 1}{etiqueta_operacion}_izquierda;\n'
            dot += anidar_arbol(indice,identificador + 1,etiqueta_operacion + "_derecho",objeto_operacion.lado_derecho)
            dot += f'nodo_{indice}_{identificador}{etiqueta_operacion} -> nodo_{indice}_{identificador + 1}{etiqueta_operacion}_derecho;\n'
    return dot
