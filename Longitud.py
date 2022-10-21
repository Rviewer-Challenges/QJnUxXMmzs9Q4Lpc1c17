def yarda(unidad1):
    if unidad1 == "milla" or unidad1 == "millas":
        n1 = float(input("Ingrese el valor de los Yarda: "))
        return print(f"{n1} Yarda equivale a:", n1/1760, "Milla")

    elif unidad1 == "milimetro" or unidad1 == "milimetros":
        n1 = float(input("Ingrese el valor de los Yarda: "))
        return print(f"{n1} Yarda equivale a:", n1 * 914.4, "Milimetro")

    elif unidad1 == "centimetro" or unidad1 == "centimetros":
        n1 = float(input("Ingrese el valor de los Yarda: "))
        return print(f"{n1} Yarda equivale a:", n1 * 91.44, "Centimetro")

    elif unidad1 == "metro" or unidad1 == "metros":
        n1 = float(input("Ingrese el valor de los Yarda: "))
        return print(f"{n1} Yarda equivale a:", n1 / 1.094, "Metro")

    elif unidad1 == "kilometro" or unidad1 == "kilometros":
        n1 = float(input("Ingrese el valor de los Yarda: "))
        return print(f"{n1} Yarda equivale a:", n1 / 1094, "Kilometro")


def milla(unidad1):
    if unidad1 == "yarda" or unidad1 == "yardas":
        n1 = float(input("Ingrese el valor de los Milla: "))
        return print(f"{n1} Milla equivale a:", n1*1760, "Yarda")

    elif unidad1 == "milimetro" or unidad1 == "milimetros":
        n1 = float(input("Ingrese el valor de los Milla: "))
        return print(f"{n1} Milla equivale a:", n1 * 1.609e+6, "Milimetro")

    elif unidad1 == "centimetro" or unidad1 == "centimetros":
        n1 = float(input("Ingrese el valor de los Milla: "))
        return print(f"{n1} Milla equivale a:", n1 * 160900, "Centimetro")

    elif unidad1 == "metro" or unidad1 == "metros":
        n1 = float(input("Ingrese el valor de los Milla: "))
        return print(f"{n1} Milla equivale a:", n1 * 1609, "Metro")

    elif unidad1 == "kilometro" or unidad1 == "kilometros":
        n1 = float(input("Ingrese el valor de los Milla: "))
        return print(f"{n1} Milla equivale a:", n1 * 1.609, "Kilometro")


def milimetro(unidad1):
    if unidad1 == "yarda" or unidad1 == "yardas":
        n1 = float(input("Ingrese el valor de los Milimetro: "))
        return print(f"{n1} Milimetro equivale a:", n1/914.4, "Yarda")

    elif unidad1 == "milla" or unidad1 == "millas":
        n1 = float(input("Ingrese el valor de los Milimetro: "))
        return print(f"{n1} Milimetro equivale a:", n1 / 1.609e+6, "Milla")

    elif unidad1 == "centimetro" or unidad1 == "centimetros":
        n1 = float(input("Ingrese el valor de los Milimetro: "))
        return print(f"{n1} Milimetro equivale a:", n1 / 10, "Centimetro")

    elif unidad1 == "metro" or unidad1 == "metros":
        n1 = float(input("Ingrese el valor de los Milimetro: "))
        return print(f"{n1} Milimetro equivale a:", n1/1000, "Metro")

    elif unidad1 == "kilometro" or unidad1 == "kilometros":
        n1 = float(input("Ingrese el valor de los Milimetro: "))
        return print(f"{n1} Milimetro equivale a:", n1 / 1e+6, "Kilometro")


def centimetro(unidad1):
    if unidad1 == "yarda" or unidad1 == "yardas":
        n1 = float(input("Ingrese el valor de los Centimetro: "))
        return print(f"{n1} Centimetro equivale a:", n1/91.44, "Yarda")

    elif unidad1 == "milla" or unidad1 == "millas":
        n1 = float(input("Ingrese el valor de los Centimetro: "))
        return print(f"{n1} Centimetro equivale a:", n1 / 160900, "Milla")

    elif unidad1 == "milimetro" or unidad1 == "milimetros":
        n1 = float(input("Ingrese el valor de los Centimetro: "))
        return print(f"{n1} Centimetro equivale a:", n1 * 10, "Milimetro")

    elif unidad1 == "metro" or unidad1 == "metros":
        n1 = float(input("Ingrese el valor de los Centimetro: "))
        return print(f"{n1} Centimetro equivale a:", n1/100, "Metro")

    elif unidad1 == "kilometro" or unidad1 == "kilometros":
        n1 = float(input("Ingrese el valor de los Centimetro: "))
        return print(f"{n1} Centimetro equivale a:", n1 / 100000, "Kilometro")


def metro(unidad1):
    if unidad1 == "yarda" or unidad1 == "yardas":
        n1 = float(input("Ingrese el valor de los Metro: "))
        return print(f"{n1} Metro equivale a:", n1*1.094, "Yarda")

    elif unidad1 == "milla" or unidad1 == "millas":
        n1 = float(input("Ingrese el valor de los Metro: "))
        return print(f"{n1} Metro equivale a:", n1 / 1609, "Milla")

    elif unidad1 == "milimetro" or unidad1 == "milimetros":
        n1 = float(input("Ingrese el valor de los Metro: "))
        return print(f"{n1} Metro equivale a:", n1 * 1000, "Milimetro")

    elif unidad1 == "centimetro" or unidad1 == "centimetros":
        n1 = float(input("Ingrese el valor de los Metro: "))
        return print(f"{n1} Metro equivale a:", n1*100, "Centimetro")

    elif unidad1 == "kilometro" or unidad1 == "kilometros":
        n1 = float(input("Ingrese el valor de los Metro: "))
        return print(f"{n1} Metro equivale a:", n1 / 1000, "Kilometro")


def kilometro(unidad1):
    if unidad1 == "yarda" or unidad1 == "yardas":
        n1 = float(input("Ingrese el valor de los Kilometro: "))
        return print(f"{n1} Kilometro equivale a:", n1*1094, "Yarda")

    elif unidad1 == "milla" or unidad1 == "millas":
        n1 = float(input("Ingrese el valor de los Kilometro: "))
        return print(f"{n1} Kilometro equivale a:", n1 / 1.609, "Milla")

    elif unidad1 == "milimetro" or unidad1 == "milimetros":
        n1 = float(input("Ingrese el valor de los Kilometro: "))
        return print(f"{n1} Kilometro equivale a:", n1 * 1e+6, "Milimetro")

    elif unidad1 == "centimetro" or unidad1 == "centimetros":
        n1 = float(input("Ingrese el valor de los Kilometro: "))
        return print(f"{n1} Kilometro equivale a:", n1*100000, "Centimetro")

    elif unidad1 == "metro" or unidad1 == "metros":
        n1 = float(input("Ingrese el valor de los Kilometro: "))
        return print(f"{n1} Kilometro equivale a:", n1 * 1000, "Metro")



