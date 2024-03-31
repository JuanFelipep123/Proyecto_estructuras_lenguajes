from Tree import TreeNode
from nltk.tree import Tree

class Ternary_Tree:

    def nltk_tree_to_ternary_tree(self, nltk_tree):
        """
        Convierte un árbol de NLTK en un árbol ternario.

        Parámetros:
        - nltk_tree (nltk.tree.Tree): Árbol de NLTK que se convertirá en un árbol ternario.

        Retorna:
        - TreeNode: Raíz del árbol ternario resultante.

        Este método toma un árbol de NLTK y lo convierte en un árbol ternario, donde cada nodo puede tener hasta tres hijos.
        """
        
        if nltk_tree is None:
            return None

        
        if hasattr(nltk_tree, 'label'):
            root = TreeNode(nltk_tree.label())  
        else:
            root = TreeNode(nltk_tree) 



        
        if hasattr(nltk_tree, 'label'):
            for child in nltk_tree:
                if hasattr(child, 'label'):
                    
                    if child == Tree(child.label(), []):
                        child = Tree(child.label(), ['λ'])
                
                child_node = self.nltk_tree_to_ternary_tree(child)
                root.children.append(child_node)

        return root

    def print_ternary_tree(self, root, indent=0):
        """
        Imprime recursivamente un árbol ternario.

        Parámetros:
        - root (TreeNode): Raíz del árbol ternario que se imprimirá.
        - indent (int): Nivel de indentación para la impresión.

        Este método imprime recursivamente un árbol ternario comenzando desde la raíz.
        """
        if root is not None:
            print(" " * indent + root.value) 
            for child in root.children:
                
                self.print_ternary_tree(child, indent + 2)

     