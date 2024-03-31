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

        grammar1 = nltk.CFG.fromstring(g1)
        analyzer = nltk.ChartParser(grammar1)
        _, oracion = self.word_format(oracion, producciones, inicial, 0, inicial, '')
    
        
        oracion_parse = oracion.split()
        
        trees = analyzer.parse_one(oracion_parse)
        if trees:
            return Tree.fromstring(str(trees))
        else:
            return trees

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
                    
                    if word[position:position + len(part)] == part:
                        resultado += f'{part}' if part != '' else 'λ'
                        resultado += ' '
                        position += len(part)
                    else:
                        return position, resultado

        return position, resultado
