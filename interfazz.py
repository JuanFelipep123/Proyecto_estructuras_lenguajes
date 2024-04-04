import tkinter as tk
from tkinter import messagebox, simpledialog

def convertir_a_diccionario(gramatica):
    diccionario = {}
    lineas = gramatica.split('\n')
    for linea in lineas:
        if linea.strip():  
            partes = linea.split('->')
            no_terminal = partes[0].strip()
            producciones = partes[1].split('|')
            producciones_separadas = []
            for p in producciones:
                symbols = tuple(s.strip() for s in p)
                producciones_separadas.append(symbols)
            diccionario[no_terminal] = producciones_separadas
    return diccionario

class GramaticaInterface:
    def __init__(self, master):
        self.diccionario = {}
        self.master = master
        self.master.title("Convertir Gramática")

        texto_ejemplo = ("Ejemplo de gramática:\n"
                         "S ⟶ AaP          \n"
                         "P ⟶ b | c | d | e\n")
        
        self.ejemplo_var = tk.StringVar()
        self.ejemplo_var.set(texto_ejemplo)

        self.label_ejemplo = tk.Label(master, textvariable=self.ejemplo_var)
        self.label_ejemplo.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.label = tk.Label(master, text="Ingrese la gramática:")
        self.label.grid(row=1, column=0, columnspan=2)

        self.text_area = tk.Text(master, height=10, width=40)
        self.text_area.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.convert_button = tk.Button(master, text="Enviar", command=self.convertir)
        self.convert_button.grid(row=3, column=0, padx=5, pady=5, sticky='e')

        self.cancel_button = tk.Button(master, text="Cancelar", command=self.cancelar)
        self.cancel_button.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    def convertir(self):
        gramatica = self.text_area.get("1.0", tk.END)
        self.mostrar_resultado(gramatica)
        try:
            self.diccionario = convertir_a_diccionario(gramatica)
        except Exception as e:
            messagebox.showerror("Error", "Ocurrió un error al convertir la gramática:\n\n{}".format(e))

    def mostrar_resultado(self, gramatica):
        resultado = messagebox.askquestion("Resultado", "¿Esta seguro que La gramática esta correcta?\n\n{}".format(gramatica), icon='info')
        if resultado == 'yes':  # Si se hace clic en "Enviar"
            self.enviar_informacion()
        else:  # Si se hace clic en "Cancelar"
            pass
    def enviar_informacion(self):
        # Aquí puedes enviar la información al main o realizar cualquier otra acción que desees
        print("Enviando información al main...")

    def cancelar(self):
        self.text_area.delete("1.0", tk.END)
        self.diccionario = {}

def main():
    root = tk.Tk()
    app = GramaticaInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()