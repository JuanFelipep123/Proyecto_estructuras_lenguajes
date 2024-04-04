from Gramatica import Gramatica
from TernaryTree import Ternary_Tree
from Graficador import graficador

class Gestor_Arbol_Derivacion:
    ternary = Ternary_Tree()
    grafico = graficador()
    grammar = Gramatica()

    def __init__(self):
        pass

    def create_tree(self, inicial, producciones, word):
        """
        Crea un árbol ternario a partir de una palabra y una gramática especificadas, y lo grafica.

        Parámetros:
            - inicial (str): Símbolo inicial de la gramática.
            - producciones (dict): Diccionario que contiene las producciones de la gramática.
            - word (str): Palabra para la cual se construirá el árbol.

        Retorna:
            - ternary_tree: El árbol ternario generado a partir de la palabra y la gramática.

        Si la palabra dada existe en la gramática especificada, este método crea un árbol ternario utilizando
        NLTK para generar un árbol de sintaxis y luego convierte este árbol en un árbol ternario. Posteriormente,
        grafica el árbol ternario resultante. Retorna el árbol ternario generado. Si la palabra no existe en la
        gramática, imprime un mensaje de advertencia y retorna None.
        """
        nltk_tree = self.grammar.generar_nltk_tree(producciones, inicial, word)
        if nltk_tree is not None:
            nltk_tree.pretty_print()     # Imprime el árbol de NLTK
            ternary_tree = self.ternary.nltk_tree_to_ternary_tree(nltk_tree)
            self.ternary.print_ternary_tree(ternary_tree)    # Imprime el árbol ternario
            self.grafico.graphic_ternary_tree(ternary_tree)
            return 'El arbol se creo correctamente'
        else:
            print('No se puede crear el árbol ya que la palabra no existe en la gramática')
            return None


""" 
------------------------- E J E M P L O ------------------------

if __name__ == '__main__':
    producciones = {
        'CN': [('FN', 'CN2')],
        'CN2': [('ox', 'FN', 'CN2'), ('',)],  # Lamnbda se debe poner como un caracter vacio -> ('') 
        'FN': [('tt',)]
    }
    print(producciones)
    arbol_derivacion = Gestor_Arbol_Derivacion()
    arbol_derivacion.create_tree('CN',producciones,'ttoxtt')
"""