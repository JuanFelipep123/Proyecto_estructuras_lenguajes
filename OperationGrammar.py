class Operation_Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = set(productions.keys())


#
    # Método para verificar si una gramática está factorizada por la izquierda
    #
    def is_left_factored(self,grammar):
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
        new_grammar = {}
        non_terminals = list(self.productions.keys())

        for A in non_terminals:
            productions_A = self.productions[A]
            new_A = A + "2"
            alpha_productions = []
            beta_productions = []

            for production in productions_A:
                if production.startswith(A):
                    alpha_productions.append(production[len(A):])
                else:
                    beta_productions.append(production)

            if alpha_productions:
                new_grammar[A] = [beta + new_A for beta in beta_productions]
                new_grammar[new_A] = [alpha + new_A for alpha in alpha_productions] + [' ']
            else:
                new_grammar[A] = productions_A

        return new_grammar
    
########################################################################################################################
    
    def convert_to_string_lists(grammar_dict):
        converted_dict = {}
        for key, value in grammar_dict.items():
            converted_key = ''.join(key)
            converted_value = [''.join(item) for item in value]
            converted_dict[converted_key] = converted_value
        return converted_dict

    def convert_to_tuple_lists(productions_dict, terminals):
        converted_dict = {}
        
        #Función para particionar la cadena en no terminales y terminales
        def partition_string(string, terminals, non_terminals):
            partitions = []
            current_partition = ""
            i = 0
            while i < len(string):
                found = False
                #Buscar las claves primero con las claves con más caracteres
                for non_terminal in sorted(non_terminals, key=len, reverse=True):
                    if string[i:].startswith(non_terminal):
                        partitions.append(current_partition)
                        current_partition = ""
                        partitions.append(non_terminal)
                        i += len(non_terminal)
                        found = True
                        break
                if not found:
                    #Particionar en terminales si no se encuentra un no terminal
                    for terminal in terminals:
                        if string[i:].startswith(terminal):
                            partitions.append(current_partition)
                            current_partition = ""
                            partitions.append(terminal)
                            i += len(terminal)
                            found = True
                            break
                if not found:
                    current_partition += string[i]
                    i += 1
            partitions.append(current_partition)
            return partitions
        
        #Obtener la lista de no terminales
        non_terminals = list(productions_dict.keys())
        
        #Convertir cada producción a tuplas de caracteres particionando la cadena
        for key, value in productions_dict.items():
            converted_value = []
            for item in value:
                tuple_item = tuple(partition_string(item, terminals, non_terminals))
                #Eliminar espacios extra
                tuple_item = tuple(filter(lambda x: x != '', tuple_item))
                converted_value.append(tuple_item)
            converted_dict[key] = converted_value
        return converted_dict

    def get_terminals(grammar):
        terminals = set()

        for productions in grammar.values():
            for production in productions:
                for symbol in production:
                    if symbol.islower() or symbol.isdigit() or symbol == "'":
                        terminals.add(symbol)

        return list(terminals)
    
    def get_first_key(dictionary):
        first_key = next(iter(dictionary.keys()), None)
        return first_key

def eliminar_recursion(dict_gramatica):
    terminales = Operation_Grammar.get_terminals(dict_gramatica)
    grammar = Operation_Grammar(Operation_Grammar.convert_to_string_lists(dict_gramatica))
    new_grammar = grammar.eliminate_left_recursion()
    new_grammar = Operation_Grammar.convert_to_tuple_lists(new_grammar,terminales)
    print(terminales)
    print(new_grammar)
    return new_grammar