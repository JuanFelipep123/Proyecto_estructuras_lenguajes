def cadena_factorizada(lista, cadena):
    for elemento in lista:
        position = cadena.find(elemento)
        replace = f' {elemento} '
        if position != -1:
            # Verificar si la ocurrencia está rodeada por caracteres que no forman parte de una palabra
            if (position == 0 or not cadena[position - 1].isalnum()) and \
               (position + len(elemento) == len(cadena) or not cadena[position + len(elemento)].isalnum()):
                cadena = cadena.replace(elemento, replace)
    return cadena.split()

# Ejemplo de uso
lista = ['CN', 'CN2', 'FN']
cadena = 'CN2ttFN'
resultado = cadena_factorizada(lista, cadena)
print(resultado)

print(lista.count('CN'))