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

    def generate_tree(self, word, node, tree):
        if not word:
            return True
        if not node:
            return False
        if node[0] in self.non_terminals:
            for production in self.productions[node[0]]:
                if self.generate_tree(word, tuple(production) + tuple(node[1:]), tree):  # Convertir node[1:] a tupla
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
def creacion_de_diccionarios(lista, matriz):
    diccionario = {}
    for clave, datos in zip(lista, matriz):
        diccionario[clave] = datos
    return diccionario

def eliminar_recursion(diccionario):
    visitado = set()

    def dfs(clave, camino):
        if clave in camino:
            diccionario[clave] = [valor for valor in diccionario[clave] if valor != clave]
            return

        if clave in visitado:
            return

        visitado.add(clave)

        for valores in diccionario.get(clave, []):
            for valor in valores:
                dfs(valor, camino + [clave])

    def dfs_indirecta(clave, camino, diccionario):
        if clave in camino:
            diccionario[camino[-1]] = [v for v in diccionario[camino[-1]] if v != clave]
            return

        camino.append(clave)

        for valor in diccionario.get(clave, []):
            dfs_indirecta(valor, camino, diccionario)

        camino.pop()

    for clave in diccionario:
        dfs(clave, [])
        visitado.clear()
        dfs_indirecta(clave, [], diccionario)

    return diccionario


def main():
    lista_claves = ['S', 'A', 'B','C','D']
    matriz_datos = [
    [('A', 'B'),('S')],
    [('a', 'A'),('B'),('A'),('C')],
    [('b', 'B'),('A'),('B')],
    [('c', 'C'),('D'),('A')],
    [('d', 'D'),('A'),('C')]
    ]   

    diccionario_resultante = creacion_de_diccionarios(lista_claves, matriz_datos)

    # Llamar a la función para eliminar recursión en el diccionario
    productions_corregido = eliminar_recursion(diccionario_resultante)

    grammar = Grammar(productions_corregido)
    grammar.eliminate_left_recursion()

    print("Gramática después de eliminar la recursión izquierda:")
    print(grammar.productions)

    word = input("Ingrese una palabra para verificar si está en la gramática: ")
    grammar.check_word(word)


if __name__ == "__main__":
    main()
    