import tkinter as tk
from tkinter import messagebox
#
# Este código crea una ventana de Tkinter donde el usuario puede ingresar 
# la gramática en el formato estándar (cada producción separada por | y cada símbolo no terminal seguido de ->)
#
def convertir_a_diccionario(gramatica):
    diccionario = {}
    lineas = gramatica.split('\n')
    for linea in lineas:
        if linea.strip():  # Ignorar líneas en blanco
            partes = linea.split('->')
            no_terminal = partes[0].strip()
            producciones = partes[1].split('|')
            # Separar cada producción en una lista de símbolos
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
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def convertir(self):
        gramatica = self.text_area.get("1.0", tk.END)
        try:
            self.diccionario = convertir_a_diccionario(gramatica)
            print(self.diccionario)
            messagebox.showinfo("Resultado", "La gramática se ha convertido correctamente:\n\n{}".format(self.diccionario))
        except Exception as e:
            messagebox.showerror("Error", "Ocurrió un error al convertir la gramática:\n\n{}".format(e))

def main():
    root = tk.Tk()
    app = GramaticaInterface(root)
    root.mainloop()

#if __name__ == "__main__":
  #  main()
