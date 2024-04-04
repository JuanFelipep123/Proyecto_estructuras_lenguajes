import tkinter as tk
from tkinter import messagebox
from Gramatica import Gramatica
from OperationGrammar import Operation_Grammar
import OperationGrammar
from GestorArbolDerivacion import Gestor_Arbol_Derivacion

#
# Este código crea una ventana de Tkinter donde el usuario puede ingresar 
# la gramática en el formato estándar (cada producción separada por | y cada símbolo no terminal seguido de ->)
#

""" 

------------------------------- E J E M P L O -----------------------

S->AB
A->aA|a
B->bB|b

S->AB
A->a|b
B->BC|CD
C->c|d
D->d

S->AaP
P->b|c|d|e
A->a

CN->FNCN2
CN2->oxFNCN2|λ
FN->tt
"""

class GramaticaInterface:
    def __init__(self, master):
        self.diccionario = {}
        self.word = ''
        self.grammar = Gramatica()
        self.hecho_dict = False
        self.hecho_word = False
        self.master = master
        self.master.title("Convertir Gramática")

        texto_ejemplo = ("Ejemplo de gramática:\n"
                         "S ⟶ AaP          \n"
                         "P ⟶ b | c | d | e\n")
        
        self.ejemplo_var = tk.StringVar()
        self.ejemplo_var.set(texto_ejemplo)

        self.label_ejemplo = tk.Label(master, textvariable=self.ejemplo_var)
        self.label_ejemplo.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

        self.label_palabra = tk.Label(master, text="Ingrese una palabra:")
        self.label_palabra.grid(row=1, column=0, padx=(10,5), pady=5)

        self.entry_palabra = tk.Entry(master)
        self.entry_palabra.grid(row=1, column=1, padx=(0,5), pady=5)

        self.save_word_button = tk.Button(master, text="Ingresar", command=self.guardar_palabra)
        self.save_word_button.grid(row=1, column=2, padx=(0,10), pady=5, sticky="w")

        self.label = tk.Label(master, text="Ingrese la gramática:")
        self.label.grid(row=2, column=0, columnspan=3)

        self.text_area = tk.Text(master, height=10, width=40)
        self.text_area.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        self.convert_button = tk.Button(master, text="Enviar", command=self.convertir)
        self.convert_button.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

    def convertir(self):
        gramatica = self.text_area.get("1.0", tk.END)
        self.diccionario = self.grammar.convertir_a_diccionario(gramatica)
        self.hecho_dict = True
        if(self.hecho_dict and self.hecho_word):
            self.evaluar_condicion()

    def guardar_palabra(self):
        self.word = self.entry_palabra.get()
        self.hecho_word = True
        if(self.hecho_dict and self.hecho_word):
            self.evaluar_condicion()
            

    def evaluar_condicion(self):
        try:
            condicion = self._init(self.diccionario,self.word)
            if condicion:
                messagebox.showinfo("Info", f"{condicion}")
        except(Exception):
            messagebox.showerror("Error", "El arbol no se pudo crear porque la palabra no existe")

    
    def _init(self,dict_gramatica, word):
        grammar = Operation_Grammar(dict_gramatica)
        if grammar.is_left_factored(dict_gramatica):


            inicio_gramatica = next(iter(grammar.productions))

            new_grammar = OperationGrammar.eliminar_recursion(dict_gramatica)
            

            
            arbol_derivacion = Gestor_Arbol_Derivacion()
           
            arbol_ternario = arbol_derivacion.create_tree(inicio_gramatica,new_grammar,word)
            return arbol_ternario
        elif not grammar.is_left_factored(dict_gramatica) :
            return 'La Gramatica no se encuentra factorizada'


