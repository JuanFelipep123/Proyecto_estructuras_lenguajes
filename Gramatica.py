from nltk.tree import Tree
import nltk
from TernaryTree import Ternary_Tree

class Gramatica:
    ternary = Ternary_Tree()
    
    def __init__(self):
       pass

    def producciones_a_gramatica(self, producciones):
        """
        Convierte un conjunto de producciones en una representación de gramática.

        Parámetros:
        - producciones (dict): Diccionario que contiene las producciones de la gramática.

        Retorna:
        - str: Representación de la gramática generada.

        Este método toma un diccionario de producciones y lo convierte en una cadena de texto
        que representa una gramática, siguiendo la convención de notación de producción de Backus-Naur (BNF).
        """
        gramatica = ""
        for non_terminal, production_rules in producciones.items():
            gramatica += f"{non_terminal} -> "
            for i, rule in enumerate(production_rules):
                if i > 0:
                    gramatica += " | "
                gramatica += " ".join([f"'{symbol}'" if symbol.islower() else symbol for symbol in rule])
            gramatica += "\n"
        return gramatica
    

    def generar_nltk_tree(self, producciones, inicial, oracion):
        """
        Genera un árbol de análisis sintáctico para una oración dada utilizando la gramática proporcionada.

        Parámetros:
        - producciones (dict): Diccionario que contiene las producciones de la gramática.
        - inicial (str): Símbolo inicial de la gramática.
        - oracion (str): Oración que se analizará sintácticamente.

        Retorna:
        - nltk.tree.Tree or None: Árbol de análisis sintáctico generado para la oración, o None si la oración no es válida según la gramática.

        Este método genera un árbol de análisis sintáctico para una oración dada utilizando la gramática especificada.
        Primero convierte las producciones en una representación de gramática, luego intenta generar un árbol de análisis
        sintáctico utilizando el analizador sintáctico de NLTK. Si la oración no es válida según la gramática, retorna None.
        """
        g1 = self.producciones_a_gramatica(producciones)
        print(g1)
        grammar1 = nltk.CFG.fromstring(g1)
        analyzer = nltk.ChartParser(grammar1)
        print(oracion)
        _, oracion_refact = self.word_format(oracion, producciones, inicial, 0, inicial, '')
    
        oracion_parse = oracion_refact.split()
        print('oracion ',oracion_parse)
        trees = analyzer.parse_one(oracion_parse)

        condicion = oracion_parse if oracion_parse else oracion == ''


        if trees and condicion:
            return Tree.fromstring(str(trees))
        else:
            return None

    def word_format(self, word, productions, symbol, position, inicial, resultado):
        """
        Formatea una palabra utilizando las producciones de una gramática.

        Parámetros:
        - word (str): Palabra que se generará a partir de las producciones.
        - productions (dict): Diccionario que contiene las producciones de la gramática.
        - symbol (str): Símbolo actual que se está procesando.
        - position (int): Posición actual en la palabra.
        - inicial (str): Símbolo inicial de la gramática.
        - resultado (str): Cadena de caracteres que representa la palabra generada hasta el momento.

        Retorna:
        - int, str: Nueva posición y resultado actualizado.

        Este método convierte las producciones de una gramática en una cadena de caracteres que representa una palabra.
        Utiliza recursión para expandir cada símbolo no terminal en sus producciones correspondientes.
        """
        if position >= len(word):
            return position, resultado

        for production in productions[symbol]:
            for part in production:
                if part in productions:
                    
                    new_position, resultado = self.word_format(word, productions, part, position, inicial, resultado)
                    position = new_position
                else:
                    print(word[position:position + len(part)], word, part)
                    if word[position:position + len(part)] == part:
                        resultado += f'{part}'
                        resultado += ' '
                        position += len(part)
                        print(resultado)
                    else:
                        return position, resultado

        return position, resultado



    def convertir_a_diccionario(self,gramatica):
        diccionario = {}
        lineas = gramatica.split('\n')
        lista = self._lista_no_terminales(lineas)
        for linea in lineas:
            if linea.strip():  # Ignorar líneas en blanco
                partes = linea.split('->')
                no_terminal = partes[0].strip()
                producciones = partes[1].split('|')
                listaProduciones = []
                for cadena in producciones:
                    if cadena != 'λ':
                        cadena2 = self._cadena_factorizada(lista,cadena)
                        listaProduciones.append(cadena2)
                    else:
                        listaProduciones.append([''])
                print(listaProduciones)
                lista_tuplas = [tuple(sublista) for sublista in listaProduciones]
                diccionario[no_terminal] = lista_tuplas
        return diccionario


    def _lista_no_terminales(self,lineas):
        lista = []
        for linea in lineas:
            if linea.strip():
                partes = linea.split('->')
                no_terminal = partes[0].strip()
                lista.append(no_terminal)
        return lista


    def _cadena_factorizada(self,lista,cadena):
        for i in lista:
            coincidencias = sum(1 for elemento in lista if i in elemento)
        
            if coincidencias <2:
                position = cadena.find(i)
            else:
                position,i = self._encontrar_mejor(lista,i,cadena)
            replace = f' {i} '
            if position != -1:
                cadena = cadena.replace(i,replace)
        return cadena.split()



    def _encontrar_mejor(self,lista,no_terminal,cadena):
        lista_coincidencias = []
        for lis in lista:
            if lis in cadena:
                lista_coincidencias.append(lis)

        
        if lista_coincidencias:
            cadena_mas_grande = max(lista_coincidencias, key=lambda x: len(x))
            return cadena.find(cadena_mas_grande), cadena_mas_grande
        else:
            return -1, no_terminal