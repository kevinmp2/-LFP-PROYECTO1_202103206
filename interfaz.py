from fileinput import filename
from tkinter import filedialog
import tkinter as tk
from tkinter.filedialog import askopenfilename
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from analizador import anidar_arbol, instruccion, operacion_recursividad
from errores import *

global numero_errores 
global lista_de_errores 

numero_errores = 0
lista_de_errores = []



class Pantalla_Principal():
    def __init__(self):
        ventana = Tk()
        ventana.title('Proyecto - 1')
        ventana.geometry("1000x500+560+240")
        ventana.configure(bg = 'firebrick1')
        titulo = tk.Label(ventana, text = 'Analizador \n Lexico', bg=ventana['bg'], fg = 'black', font = ('italic', 20, 'bold'), highlightbackground=ventana['bg'])
        titulo.pack(side=tk.TOP, padx=10, pady= 10)
        self.botones(ventana)

        
        
        # Menu
        #menu = Menu(ventana)
        #ventana.config(menu = menu)
        #menu_opciones = Menu(menu)
        #menu.add_cascade(label = 'Menu Principal', menu = menu_opciones)

    def botones(self, ventana):
        #Botones
        boton_abrir = Button(ventana, command = self.abrir_archivo, text = 'Abrir Archivo', cursor= 'hand2', bg = 'steelblue2', width= 12, height= 2, font= ('corabad', 10 , 'bold'))
        boton_abrir.place(x = 40, y = 90)

        boton_guardar = Button(ventana, text = 'Guardar', cursor= 'hand2', bg = 'steelblue2', width= 15, height= 2, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 27, y = 145)

        boton_analizar = Button(ventana, command = self.analizar, text = 'Analizar', cursor= 'hand2', bg = 'steelblue2', width= 12, height= 2, font= ('corabad', 10 , 'bold'))
        boton_analizar.place(x = 40, y = 200)

        boton_errores = Button(ventana, command= self.errores, text = 'Errores', cursor= 'hand2', bg = 'steelblue2', width= 12, height= 2, font= ('corabad', 10 , 'bold'))
        boton_errores.place(x = 40, y = 255)

        boton_salir = Button(ventana, command = ventana.destroy, text = 'Salir', cursor= 'hand2', bg = 'steelblue2', width= 12, height= 2, font= ('corabad', 10 , 'bold'))
        boton_salir.place(x = 40, y = 310)

        boton_manual_usuario = Button(ventana, command=lambda: webbrowser.open(r'C:\Users\patzan\Desktop\Manual de usuario.pdf'), text = 'Manual De Usuario', cursor= 'hand2', bg = 'steelblue2', width= 15, height= 2, font= ('corabad', 10 , 'bold'))
        boton_manual_usuario.place(x = 835, y = 145)

        boton_manual_tecnico = Button(ventana, command=lambda: webbrowser.open(r'C:\Users\patzan\Desktop\Manual tecnico.pdf'), text = 'Manual Tecnico', cursor= 'hand2', bg = 'steelblue2', width= 15, height= 2, font= ('corabad', 10 , 'bold'))
        boton_manual_tecnico.place(x = 835, y = 200)

        boton_temas_ayuda = Button(ventana, command=lambda: webbrowser.open(r'C:\Users\patzan\Desktop\Datos.pdf'), text = 'Temas De Ayuda', cursor= 'hand2', bg = 'steelblue2', width= 15, height= 2, font= ('corabad', 10 , 'bold'))
        boton_temas_ayuda.place(x = 835, y = 255)
        
        global area_texto
        area_texto = scrolledtext.ScrolledText(ventana, width = 74, height = 20)
        area_texto.place(x = 190, y = 85)
        
        
        ventana.mainloop()  


    def abrir_archivo(self):
        x = ''
        Tk().withdraw()
        try:
            filename = askopenfilename(title = 'Seleccione un archivo', filetype = [('Archivos', f'*.json')])
            with open(filename, encoding= 'utf-8') as infile:
                x = infile.read()
        except:
            print('Ingrese un archivo correcto')
            return
        
        self.texto = x
        global area_texto
        area_texto.insert('1.02', x)
        
    def analizar(self):
        global area_texto
        texto = area_texto.get('1.0', END)
        instruccion(texto)
        respuestas = operacion_recursividad()
        #empezar con el graphviz
        cadena = "digraph G {\n"
    
        for r2 in respuestas:
            r2 = r2.vaciar()
            break

        for respuesta in respuestas:
            respuesta.operar(None)

        for r in range(len(respuestas)):
            cadena += anidar_arbol(r, 0, "", respuestas[r])
            print()
            print()

        cadena += "}"
        archivo = open("resultado.dot", "w")
        archivo.write(cadena)
        archivo.close()
        from os import system
        from os import system, startfile
        system('dot.exe -Tpdf resultado.dot -o Resultado_202103206.pdf')
        system('Resultado_202103206.pdf')
    
    def area_texto(self):
        area = Tk()
        area.title('Editar')
        texto = Text(area)
        texto.pack()
        texto.config(width=30, height=10, font=("Consolas",12), padx=15, pady=15, selectbackground="red")
        area.mainloop()

    # def documentacion(self):
    #     archivo = filedialog.askopenfilename(title = 'ayuda', initialdir = 'C:/',  filetypes = (('Todos los archivos', '*.*'),))
    #     if archivo:
    #         webbrowser.open_new_tab(archivo)
              
    def errores(self):
        global area_texto
        lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', ':', '[', ']', '{', '}', '"', ' ', '-']
        texto = (area_texto.get('1.0', END)).lower()

        lineas = texto.split('\n')

        contador = 0

        archivo = open('Errores_202103206.txt', 'w')
        archivo.write('{')
        coma = ','
        for i, linea in enumerate(lineas):
            cadena = linea.split()
            for j, cadena in enumerate(linea):
                if cadena not in lista:
                    contador += 1
                    #print(f"No.{contador}: Carácter '{cadena}' no está en la lista. Fila: {i+1}, Columna: {j+1}")
                    archivo.write(
                                f'''
                                {{
                                    "No." : {contador},
                                        "Descripcion": {{
                                            "Lexema" : "{cadena}",
                                            "Tipo" : "Error",
                                            "Fila" : {i+1}
                                            "Columna" : {j+1}
                                        }}           
                                    }}{coma}
                                '''
                    )
        archivo.write('}')
        archivo.close()
        webbrowser.open('Errores_202103206.txt')

ventana = Pantalla_Principal()