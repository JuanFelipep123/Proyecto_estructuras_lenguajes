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
        Crea un árbol ternario y lo grafica según la gramática proporcionada.

        Parámetros:
        - inicial (str): Símbolo inicial de la gramática.
        - producciones (dict): Diccionario que contiene las producciones de la gramática.
        - word (str): Palabra para la cual se construirá el árbol.

        Este método crea un árbol ternario a partir de la palabra dada y la gramática especificada.
        Luego, grafica el árbol generado.
        """
        nltk_tree = self.grammar.generar_nltk_tree(producciones,inicial,word)
        if nltk_tree is not None:
            nltk_tree.pretty_print()     # imprime el nltk_tree
            ternary_tree = self.ternary.nltk_tree_to_ternary_tree(nltk_tree)
            self.ternary.print_ternary_tree(ternary_tree)    # imprime el arbol ternario
            self.grafico.graphic_ternary_tree(ternary_tree)
        else:
            print('No se puede crear el arbol ya que la palabra no existe en la gramatica')


if __name__ == '__main__':
    producciones = {
        'CN': [('FN', 'CN2')],
        'CN2': [('ox', 'FN', 'CN2'), ('')],  # Lamnbda se debe poner como un caracter vacio -> ('') 
        'FN': [('tt',)]
    }
    arbol_derivacion = Gestor_Arbol_Derivacion()
    arbol_derivacion.create_tree('CN',producciones,'ttoxtt')




