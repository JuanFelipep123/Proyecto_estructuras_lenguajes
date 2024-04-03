from GestorArbolDerivacion import Gestor_Arbol_Derivacion
import tkinter as tk
from tkinter import messagebox

from interfazz import GramaticaInterface


class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = set(productions.keys())

    def eliminate_left_recursion(self):
        new_grammar = {}
        non_terminals = list(self.productions.keys())

        for A in non_terminals:
            productions_A = self.productions[A]
            new_A = A + "2"
            alpha_productions = []
            beta_productions = []

            for production in productions_A:
                if production.startswith(A):
                    alpha_productions.append(production[len(A):])
                else:
                    beta_productions.append(production)

            if alpha_productions:
                new_grammar[A] = [beta + new_A for beta in beta_productions]
                new_grammar[new_A] = [alpha + new_A for alpha in alpha_productions] + [' ']
            else:
                new_grammar[A] = productions_A

        return new_grammar

def convert_to_string_lists(grammar_dict):
    converted_dict = {}
    for key, value in grammar_dict.items():
        converted_key = ''.join(key)
        converted_value = [''.join(item) for item in value]
        converted_dict[converted_key] = converted_value
    return converted_dict

def convert_to_tuple_lists(productions_dict, terminals):
    converted_dict = {}
    
    # Función para particionar la cadena en no terminales y terminales
    def partition_string(string, terminals, non_terminals):
        partitions = []
        current_partition = ""
        i = 0
        while i < len(string):
            found = False
            # Buscar las claves primero con las claves con más caracteres
            for non_terminal in sorted(non_terminals, key=len, reverse=True):
                if string[i:].startswith(non_terminal):
                    partitions.append(current_partition)
                    current_partition = ""
                    partitions.append(non_terminal)
                    i += len(non_terminal)
                    found = True
                    break
            if not found:
                # Particionar en terminales si no se encuentra un no terminal
                for terminal in terminals:
                    if string[i:].startswith(terminal):
                        partitions.append(current_partition)
                        current_partition = ""
                        partitions.append(terminal)
                        i += len(terminal)
                        found = True
                        break
            if not found:
                current_partition += string[i]
                i += 1
        partitions.append(current_partition)
        return partitions
    
    # Obtener la lista de no terminales
    non_terminals = list(productions_dict.keys())
    
    # Convertir cada producción a tuplas de caracteres particionando la cadena
    for key, value in productions_dict.items():
        converted_value = []
        for item in value:
            tuple_item = tuple(partition_string(item, terminals, non_terminals))
            # Eliminar espacios extra
            tuple_item = tuple(filter(lambda x: x != '', tuple_item))
            converted_value.append(tuple_item)
        converted_dict[key] = converted_value
    return converted_dict

def get_terminals(grammar):
    terminals = set()

    for productions in grammar.values():
        for production in productions:
            for symbol in production:
                if symbol.islower() or symbol.isdigit() or symbol == "'":
                    terminals.add(symbol)

    return list(terminals)
def get_first_key(dictionary):
    first_key = next(iter(dictionary.keys()), None)
    return first_key

def main(dict_gramatica):
    print(dict_gramatica)
    terminales = get_terminals(dict_gramatica)
    grammar = Grammar(convert_to_string_lists(dict_gramatica))
    new_grammar = grammar.eliminate_left_recursion()
    new_grammar = convert_to_tuple_lists(new_grammar,terminales)
    print(new_grammar)
    inicio_gramatica = get_first_key(new_grammar)
    word = input("Ingrese una palabra para verificar si está en la gramática: ")

    # Creacion del arbol de derivacion
    arbol_derivacion = Gestor_Arbol_Derivacion()
    #Devuelve el arbol ternario
    #arbol_ternario = arbol_derivacion.create_tree(inicio_gramatica,new_grammar,word)


if __name__ == "__main__":
    root = tk.Tk()
    app = GramaticaInterface(root)
    main(app.diccionario)
    root.mainloop()