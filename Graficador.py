import matplotlib.pyplot as plt
from TernaryTree import Ternary_Tree 

class graficador:

    ternary = Ternary_Tree()

    def _plot_tree(self, tree, ax=None, parent_pos=None, depth=0, position=0, total_width=1.0, node_size=14):
        if ax is None:
            fig, ax = plt.subplots()

        if parent_pos is None:
            parent_pos = [0.5, 1.0]

        current_pos = [parent_pos[0] + position * total_width / 10, 1 - depth * 0.1]

        if tree.value.endswith('lambda'):
            node_color = 'lightblue'  # Nodos terminales que terminan en 'lambda'
        else:
            node_color = 'navy'  # Resto de nodos terminales y no terminales

        ax.add_patch(plt.Circle((current_pos[0], current_pos[1]), 0.03, color=node_color))  # Dibujar el nodo como un círculo

        ax.text(current_pos[0], current_pos[1], tree.value, ha='center', va='center',
                bbox=dict(facecolor=node_color, alpha=0.5), fontsize=node_size, color='white')

        if tree.children:
            num_children = len(tree.children)
            child_width = total_width / num_children
            start_position = current_pos[0] - total_width / 2 + child_width / 2
            for i, child in enumerate(tree.children):
                child_position = start_position + i * child_width
                ax.plot([current_pos[0], child_position], [current_pos[1], current_pos[1] - 0.1], 'k-')  # Línea desde el nodo padre al nodo hijo
                child_pos = [child_position, current_pos[1] - 0.1]
                self._plot_tree(child, ax, child_pos, depth + 1, i, child_width, node_size)  # Dibujar el nodo hijo

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

    def graphic_ternary_tree(self, tree, node_size=14):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.text(0.5, 1.1, "Este es el árbol de derivación de la palabra ingresada", ha='center', va='center', fontsize=16)
        self._plot_tree(tree, ax, node_size=node_size)
        plt.show()
