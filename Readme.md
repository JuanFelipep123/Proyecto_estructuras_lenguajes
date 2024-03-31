# Parte del Proyecto de Construcción y Graficación de Árboles de Derivación Gramatical

Esta parte consiste en una herramienta para construir y graficar árboles de derivación gramatical a partir de una gramática y una palabra dada. La herramienta utiliza la librería NLTK (Natural Language Toolkit) para manipular gramáticas y generar árboles sintácticos.

## Ejemplo de Uso

```python


# Definición de producciones
producciones = {
    'CN': [('FN', 'CN2')],
    'CN2': [('ox', 'FN', 'CN2'), ('')], 
    'FN': [('tt',)]
}

# Creación de instancias
arbol_derivacion = Gestor_Arbol_Derivacion()

# Construir y graficar el árbol de derivación
arbol_derivacion.create_tree('CN',producciones,'ttoxtt')
```

## Producciones de Ejemplo

```python
producciones = {
    'S': [('A', 'B')],
    'A': [('a', 'A'), ('a')],
    'B': [('b','B'), ('b')]
}

producciones = {
    'CN': [('FN', 'CN2')],
    'CN2': [('ox', 'FN', 'CN2'), ('')], 
    'FN': [('tt',)]
}
```

## Requisitos

Este proyecto requiere la instalación de las siguientes librerías de Python:

- NLTK: Librería para procesamiento de lenguaje natural. Se puede instalar utilizando pip:
  
  ```
  pip install nltk
  ```

- Matplotlib: Librería para graficación en Python. Se puede instalar utilizando pip:

  ```
  pip install matplotlib
  ```



## Estructura del Proyecto

El proyecto está dividido en los siguientes archivos:

- `Gramatica.py`: Contiene la implementación de la clase `Gramatica` para manipular gramáticas.
- `TernaryTree.py`: Contiene la implementación de la clase `Ternary_Tree` para representar y manipular árboles ternarios.
- `Graficador.py`: Contiene la implementación de la clase `graficador` para graficar árboles ternarios.
- `GestorArbolDerivacion.py`: Punto de entrada del programa donde se realizan las pruebas y se muestra el ejemplo de uso.
