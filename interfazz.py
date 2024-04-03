import tkinter as tk
from tkinter import messagebox
import main as Main
from Gramatica import Gramatica

#
# Este código crea una ventana de Tkinter donde el usuario puede ingresar 
# la gramática en el formato estándar (cada producción separada por | y cada símbolo no terminal seguido de ->)
#

""" 
S->AB
A->aA|a
B->bB|b


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
        try:
            self.diccionario = self.grammar.convertir_a_diccionario(gramatica)
            self.hecho_dict = True
            if(self.hecho_dict and self.hecho_word):
                Main.main(self.diccionario,self.word)
            messagebox.showinfo("Resultado", "La gramática se ha convertido correctamente:\n\n{}".format(self.diccionario))
        except Exception as e:
            messagebox.showerror("Error", "Ocurrió un error al convertir la gramática:\n\n{}".format(e))

    def guardar_palabra(self):
        self.word = self.entry_palabra.get()
        self.hecho_word = True
        if(self.hecho_dict and self.hecho_word):
            Main.main(self.diccionario,self.word)
        messagebox.showinfo("Ingresar", f"La palabra '{self.word}' ha sido guardada con éxito.")




if __name__ == "__main__":
    root = tk.Tk()
    app = GramaticaInterface(root)
    root.mainloop()

