def miligramo(unidad1):
    if unidad1 == "gramo" or unidad1 == "gramos":
        n1 = float(input("Ingrese el valor de los Miligramo: "))
        return print(f"{n1} Miligramo equivale a:", n1/1000, "Gramos")

    elif unidad1 == "kilogramo" or unidad1 == "kilogramos":
        n1 = float(input("Ingrese el valor de los Miligramo: "))
        return print(f"{n1} Miligramo equivale a:", n1 / 1e+6, "Kilogramo")

    elif unidad1 == "tonelada" or unidad1 == "toneladas":
        n1 = float(input("Ingrese el valor de los Miligramo: "))
        return print(f"{n1} Miligramo equivale a:", n1 / 1e+9, "Tonelada")


def gramo(unidad1):
    if unidad1 == "miligramo" or unidad1 == "miligramos":
        n1 = float(input("Ingrese el valor de los Gramo: "))
        return print(f"{n1} Gramo equivale a:", n1 * 1000, "Miligramo")

    elif unidad1 == "kilogramo" or unidad1 == "kilogramos":
        n1 = float(input("Ingrese el valor de los Gramo: "))
        return print(f"{n1} Gramo equivale a:", n1 / 1000, "Kilogramo")

    elif unidad1 == "tonelada" or unidad1 == "toneladas":
        n1 = float(input("Ingrese el valor de los Gramo: "))
        return print(f"{n1} Gramo equivale a:", n1 / 1e+6, "Tonelada")


def kilogramo(unidad1):
    if unidad1 == "miligramo" or unidad1 == "miligramos":
        n1 = float(input("Ingrese el valor de los Kilogramo: "))
        return print(f"{n1} Kilogramo equivale a:", n1 * 1e+6, "Miligramos")

    elif unidad1 == "gramo" or unidad1 == "gramos":
        n1 = float(input("Ingrese el valor de los Kilogramo: "))
        return print(f"{n1} Kilogramo equivale a:", n1 * 1000, "Gramo")

    elif unidad1 == "tonelada" or unidad1 == "toneladas":
        n1 = float(input("Ingrese el valor de los Kilogramo: "))
        return print(f"{n1} Kilogramo equivale a:", n1 / 1000, "Tonelada")


def tonelada(unidad1):
    if unidad1 == "miligramo" or unidad1 == "miligramos":
        n1 = float(input("Ingrese el valor de los Tonelada: "))
        return print(f"{n1} Tonelada equivale a:", n1 * 1e+9, "Miligramos")

    elif unidad1 == "gramo" or unidad1 == "gramos":
        n1 = float(input("Ingrese el valor de los Tonelada: "))
        return print(f"{n1} Tonelada equivale a:", n1 * 1e+6, "Gramo")

    elif unidad1 == "kilogramo" or unidad1 == "kilogramos":
        n1 = float(input("Ingrese el valor de los Tonelada: "))
        return print(f"{n1} Tonelada equivale a:", n1 * 1000, "Kilogramo")
