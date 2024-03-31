class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret



class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = set(productions.keys())

    def eliminate_left_recursion(self):
        for A in self.non_terminals:
            for i in range(len(self.productions[A])):
                if self.productions[A][i] and self.productions[A][i][0] == A:  # Agregar verificación
                    alpha = self.productions[A][i][1:]
                    self.productions[A].pop(i)
                    new_non_terminal = A + "'"
                    self.non_terminals.add(new_non_terminal)
                    for production in self.productions:
                        if production == A:
                            continue
                        self.productions[production].extend(
                            [p + (new_non_terminal,) for p in self.productions[A]]
                        )
                    self.productions[new_non_terminal] = [alpha + (new_non_terminal,), ('',)]

    def generate_parse_tree(self, word, productions, symbol, position):
        if position == len(word):
            return TreeNode(symbol)

        node = TreeNode(symbol)
        for production in productions.get(symbol, []):
            if word[position:].startswith(''.join(production)):
                child_position = position
                child = TreeNode(production)
                for part in production:
                    child_tree = self.generate_parse_tree(word, productions, part, child_position)
                    if child_tree is not None:
                        child.add_child(child_tree)
                        child_position += len(part)
                    else:
                        break
                else:
                    node.add_child(child)
        if not node.children:
            return None
        return node



    def check_word(self, word):
        tree = []
        if self.generate_tree(word, ('S',), tree):
            print("La palabra está en la gramática.")
            self.draw_tree(tree)
        else:
            print("La palabra no está en la gramática.")

    def draw_tree(self, tree):
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.DiGraph()
        for edge in tree:
            G.add_edge(str(edge[0]), str(edge[1]))

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True)
        plt.show()


def main():
    productions = {
        'S': [('A', 'B')],
        'A': [('a', 'A'), ('a')],
        'B': [('b', 'B'), ('b')]
    }
    productions2 = {
        'S': [('S', 'A')],
        'A': [('a')]
    }

    grammar = Grammar(productions)
    grammar.eliminate_left_recursion()
    r =grammar.generate_parse_tree('aaabb', productions, 'S', 0)

    print(r)

    print("Gramática después de eliminar la recursión izquierda:")
    print(grammar.productions)

    #word = input("Ingrese una palabra para verificar si está en la gramática: ")
    #grammar.check_word(word)


if __name__ == "__main__":
    main()