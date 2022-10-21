def byte(unidad1):
    if unidad1 == "kilobyte":
        n1 = float(input("Ingrese el valor de los Byte: "))
        return print(f"{n1} Byte equivale a:", n1/1000, "Kilobyte")

    elif unidad1 == "megabyte":
        n1 = float(input("Ingrese el valor de los Byte: "))
        return print(f"{n1} Byte equivale a:", n1 / 1e+6, "Megabyte")

    elif unidad1 == "gigabyte":
        n1 = float(input("Ingrese el valor de los Byte: "))
        return print(f"{n1} Byte equivale a:", n1 / 1e+9, "Gigabyte")

    elif unidad1 == "terabyte":
        n1 = float(input("Ingrese el valor de los Byte: "))
        return print(f"{n1} Byte equivale a:", n1/1e+12, "Terabyte")


def kilobyte(unidad1):
    if unidad1 == "byte":
        n1 = float(input("Ingrese el valor de los Kilobyte: "))
        return print(f"{n1} Kilobyte equivale a:", n1*1000, "Byte")

    elif unidad1 == "megabyte":
        n1 = float(input("Ingrese el valor de los Kilobyte: "))
        return print(f"{n1} Kilobyte equivale a:", n1 / 1000, "Megabyte")

    elif unidad1 == "gigabyte":
        n1 = float(input("Ingrese el valor de los Kilobyte: "))
        return print(f"{n1} Kilobyte equivale a:", n1 / 1e+6, "Gigabyte")

    elif unidad1 == "terabyte":
        n1 = float(input("Ingrese el valor de los Kilobyte: "))
        return print(f"{n1} Kilobyte equivale a:", n1/1e+9, "Terabyte")


def megabyte(unidad1):
    if unidad1 == "byte":
        n1 = float(input("Ingrese el valor de los Megabyte: "))
        return print(f"{n1} Megabyte equivale a:", n1*1e+6, "Byte")

    elif unidad1 == "kilobyte":
        n1 = float(input("Ingrese el valor de los Megabyte: "))
        return print(f"{n1} Megabyte equivale a:", n1 * 1000, "Kilobyte")

    elif unidad1 == "gigabyte":
        n1 = float(input("Ingrese el valor de los Megabyte: "))
        return print(f"{n1} Megabyte equivale a:", n1 / 1000, "Gigabyte")

    elif unidad1 == "terabyte":
        n1 = float(input("Ingrese el valor de los Megabyte: "))
        return print(f"{n1} Megabyte equivale a:", n1/1e+6, "Terabyte")


def gigabyte(unidad1):
    if unidad1 == "byte":
        n1 = float(input("Ingrese el valor de los Gigabyte: "))
        return print(f"{n1} Gigabyte equivale a:", n1*1e+9, "Byte")

    elif unidad1 == "kilobyte":
        n1 = float(input("Ingrese el valor de los Gigabyte: "))
        return print(f"{n1} Gigabyte equivale a:", n1 * 1e+6, "Kilobyte")

    elif unidad1 == "megabyte":
        n1 = float(input("Ingrese el valor de los Gigabyte: "))
        return print(f"{n1} Gigabyte equivale a:", n1 * 1000, "Megabyte")

    elif unidad1 == "terabyte":
        n1 = float(input("Ingrese el valor de los Gigabyte: "))
        return print(f"{n1} Gigabyte equivale a:", n1/1000, "Terabyte")


def terabyte(unidad1):
    if unidad1 == "byte":
        n1 = float(input("Ingrese el valor de los Terabyte: "))
        return print(f"{n1} Terabyte equivale a:", n1*1e+12, "Byte")

    elif unidad1 == "kilobyte":
        n1 = float(input("Ingrese el valor de los Terabyte: "))
        return print(f"{n1} Terabyte equivale a:", n1 * 1e+9, "Kilobyte")

    elif unidad1 == "megabyte":
        n1 = float(input("Ingrese el valor de los Terabyte: "))
        return print(f"{n1} Terabyte equivale a:", n1 * 1e+6, "Megabyte")

    elif unidad1 == "gigabyte":
        n1 = float(input("Ingrese el valor de los Terabyte: "))
        return print(f"{n1} Terabyte equivale a:", n1*1000, "Gigabyte")
