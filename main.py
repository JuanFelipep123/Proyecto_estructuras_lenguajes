from GestorArbolDerivacion import Gestor_Arbol_Derivacion


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
    [('b', 'B'),('A'),('B'),('')],
    [('c', 'C'),('D'),('A'),('')],
    [('d', 'D'),('A'),('C'),('')]
    ]   

    diccionario_resultante = creacion_de_diccionarios(lista_claves, matriz_datos)
    print(diccionario_resultante)

    # Llamar a la función para eliminar recursión en el diccionario
    productions_corregido = eliminar_recursion(diccionario_resultante)

    grammar = Grammar(productions_corregido)
    grammar.eliminate_left_recursion()

    print("Gramática después de eliminar la recursión izquierda:")
    print(grammar.productions)

    word = input("Ingrese una palabra para verificar si está en la gramática: ")
    inicio_gramatica = input("Ingrese el inicio de la gramatica: ")

    # Creacion del arbol de derivacion
    arbol_derivacion = Gestor_Arbol_Derivacion()
    #Devuelve el arbol ternario
    arbol_ternario = arbol_derivacion.create_tree(inicio_gramatica,productions_corregido,word)


if __name__ == "__main__":
    main()
    