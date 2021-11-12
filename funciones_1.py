"""
    A continuación, se nombra la siguientes función utilizada en el proyecto.
    * hangdraw(intento)
"""
def hangdraw(intento):
    """
    Esta función recibe un parámetro entero 'intento' del 1 al 6 y dibuja la horca dependiendo el valor de 
    'intento'
    """

    # 'intento' puede ser cualquier valor del 1 al 6 y va aumentando según el usuario fallé al insertar
    # una letra en el 'guees'.
    if intento == 0:
        print(" ________________")  
        print("|____            |")
        print("|                |")
        print("|                |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 1:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|                |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 2:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|    |           |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 3:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|           |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 4:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|\          |")
        print("|                |")
        print("|                |")
        print("|________________|")
    elif intento == 5:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|\          |")
        print("|   /            |")
        print("|                |")
        print("|________________|")
    elif intento == 6:
        print(" ________________")
        print("|____            |")
        print("|    o           |")
        print("|   /|\          |")
        print("|   / \          |")
        print("|                |")
        print("|________________|")
