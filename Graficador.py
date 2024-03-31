import matplotlib.pyplot as plt
from TernaryTree import Ternary_Tree 

class graficador:

    ternary = Ternary_Tree()

    def _plot_tree(self, tree, ax=None, parent_pos=None, depth=0, position=0, total_width=1.0):
        """
        Función interna para trazar recursivamente un árbol ternario.

        Parámetros:
        - tree (Ternary_Tree.Node): Nodo del árbol ternario que se trazará.
        - ax (matplotlib.axes.Axes): Objeto de ejes de Matplotlib en el que se trazará el árbol.
        - parent_pos (list): Posición del nodo padre.
        - depth (int): Profundidad actual del nodo en el árbol.
        - position (int): Posición del nodo dentro de sus hermanos.
        - total_width (float): Ancho total del área de trazado.

        Esta función traza recursivamente un árbol ternario en el objeto de ejes de Matplotlib especificado.
        Se utiliza para trazar los nodos del árbol, las conexiones entre los nodos y las etiquetas de los nodos.
        """
        if ax is None:
            fig, ax = plt.subplots()

        if parent_pos is None:
            parent_pos = [0.5, 1.0]

        current_pos = [parent_pos[0] + position * total_width / 2, 1 - depth * 1.5]
        
        if parent_pos is not None:
            ax.plot([parent_pos[0], current_pos[0]], [parent_pos[1], current_pos[1]], 'k-')

        ax.text(current_pos[0], current_pos[1], tree.value, ha='center', va='center',
                bbox=dict(facecolor='lightgray', alpha=0.5), fontsize=14)

        if tree.children:
            num_children = len(tree.children)
            child_width = total_width / num_children
            start_position = current_pos[0] - total_width / 2
            for i, child in enumerate(tree.children):
                child_position = start_position + (i + 0.5) * child_width
                self._plot_tree(child, ax, current_pos, depth + 1, i, child_width)

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

    
    def graphic_ternary_tree(self, tree):
        """
        Grafica un árbol ternario utilizando Matplotlib.

        Parámetros:
        - tree (Ternary_Tree.Node): Nodo raíz del árbol ternario que se trazará.

        Esta función crea una figura de Matplotlib y llama a la función interna _plot_tree
        para trazar recursivamente el árbol ternario especificado en la figura.
        """
        fig, ax = plt.subplots(figsize=(4, 3))
        self._plot_tree(tree, ax)
        plt.show()
