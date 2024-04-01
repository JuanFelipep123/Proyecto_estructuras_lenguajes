class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = set(productions.keys())

    #
    # Método para verificar si una gramática está factorizada por la izquierda
    #
    def is_left_factored(grammar):
        for non_terminal, productions in grammar.items():
            prefixes = set()  # Conjunto para almacenar los prefijos comunes
            for production in productions:
                if not production:
                    continue  # Si la producción está vacía, pasamos a la siguiente iteración
                prefix = production[0]  # El primer símbolo de cada producción
                if prefix in prefixes:
                    return False  # Si encontramos un prefijo común, la gramática no está factorizada por la izquierda
                prefixes.add(prefix)
        return True  # Si no encontramos prefijos comunes en ningún símbolo no terminal, la gramática está factorizada por la izquierda

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

    def generate_tree(self, word, node, tree):
        if not word:
            return True
        if not node:
            return False
        if node[0] in self.non_terminals:
            for production in self.productions[node[0]]:
                if self.generate_tree(word, production + tuple(node[1:]), tree):  # Convertir node[1:] a tupla
                    tree.append((node, production))
                    return True
            return False
        elif node[0] == word[0]:
            return self.generate_tree(word[1:], node[1:], tree)
        else:
            return False


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
        'A': [('a', 'A'), ('')],
        'B': [('b', 'B'), ('')]
    }

    grammar = Grammar(productions)
    grammar.eliminate_left_recursion()

    print("Gramática después de eliminar la recursión izquierda:")
    print(grammar.productions)

    word = input("Ingrese una palabra para verificar si está en la gramática: ")
    grammar.check_word(word)


if __name__ == "__main__":
    main()
    