def milisegundos(unidad2):
    if unidad2 == "segundos" or unidad2 == "segundo":
        n1 = float(input("Ingrese el valor de los Milisegundos: "))
        return print(f"{n1} Milisegundos equivale a:", n1/1000, "segundos")

    elif unidad2 == "minutos" or unidad2 == "minuto":
        n1 = float(input("Ingrese el valor de los Milisegundos: "))
        return print(f"{n1} Milisegundos equivale a:", n1 / 60000, "Minutos")

    elif unidad2 == "horas" or unidad2 == "hora":
        n1 = float(input("Ingrese el valor de los Milisegundos: "))
        return print(f"{n1} Milisegundos equivale a:", n1 / 3.6e+6, "Horas")

    elif unidad2 == "dias" or unidad2 == "dia":
        n1 = float(input("Ingrese el valor de los Milisegundos: "))
        return print(f"{n1} Milisegundos equivale a:", n1 / 8.64e+7, "Dias")

    elif unidad2 == "semanas" or unidad2 == "semana":
        n1 = float(input("Ingrese el valor de los Milisegundos: "))
        return print(f"{n1} Milisegundos equivale a:", n1 / 6.048e+8, "Semanas")

    elif unidad2 == "mes" or unidad2 == "meses":
        n1 = float(input("Ingrese el valor de los Milisegundos: "))
        return print(f"{n1} Milisegundos equivale a:", n1 / 2.628e+9, "Mes")

    elif unidad2 == "año" or unidad2 == "años":
        n1 = float(input("Ingrese el valor de los Milisegundos: "))
        return print(f"{n1} Milisegundos equivale a:", n1 /3.154e+10, "Año/s")


def segundos(unidad2):
    if unidad2 == "milisegundos" or unidad2 == "milisegundo":
        n1 = float(input("Ingrese el valor de los segundos: "))
        return print(f"{n1} Segundos equivale a:", n1 * 1000, "Milisegundos")

    elif unidad2 == "minutos" or unidad2 == "minuto":
        n1 = float(input("Ingrese el valor de los Segundos: "))
        return print(f"{n1} Segundos equivale a:", n1 / 60, "Minutos")

    elif unidad2 == "horas" or unidad2 == "hora":
        n1 = float(input("Ingrese el valor de los Segundos: "))
        return print(f"{n1} Segundos equivale a:", n1 / 3600, "Horas")

    elif unidad2 == "dias" or unidad2 == "dia":
        n1 = float(input("Ingrese el valor de los Segundos: "))
        return print(f"{n1} Segundos equivale a:", n1 / 86400, "Dias")

    elif unidad2 == "semanas" or unidad2 == "semana":
        n1 = float(input("Ingrese el valor de los Segundos: "))
        return print(f"{n1} Segundos equivale a:", n1 / 604800, "Semanas")

    elif unidad2 == "mes" or unidad2 == "meses":
        n1 = float(input("Ingrese el valor de los Segundos: "))
        return print(f"{n1} Segundos equivale a:", n1 / 2.628e+6, "Mes")

    elif unidad2 == "año" or unidad2 == "años":
        n1 = float(input("Ingrese el valor de los Segundos: "))
        return print(f"{n1} Segundos equivale a:", n1 / 3.154e+7, "Año/s")


def minutos(unidad2):
    if unidad2 == "milisegundos" or unidad2 == "milisegundo":
        n1 = float(input("Ingrese el valor de los Minutos: "))
        return print(f"{n1} Minutos equivale a:", n1 * 60000, "Milisegundos")

    elif unidad2 == "segundos" or unidad2 == "segundo":
        n1 = float(input("Ingrese el valor de los Minutos: "))
        return print(f"{n1} Minutos equivale a:", n1 * 60, "Segundos")

    elif unidad2 == "horas" or unidad2 == "hora":
        n1 = float(input("Ingrese el valor de los Minutos: "))
        return print(f"{n1} Minutos equivale a:", n1 / 60, "Horas")

    elif unidad2 == "dias" or unidad2 == "dia":
        n1 = float(input("Ingrese el valor de los Minutos: "))
        return print(f"{n1} Minutos equivale a:", n1 / 1440, "Dias")

    elif unidad2 == "semanas" or unidad2 == "semana":
        n1 = float(input("Ingrese el valor de los Minutos: "))
        return print(f"{n1} Minutos equivale a:", n1 / 10080, "Semanas")

    elif unidad2 == "mes" or unidad2 == "meses":
        n1 = float(input("Ingrese el valor de los Minutos: "))
        return print(f"{n1} Minutos equivale a:", n1 / 43800, "Mes")

    elif unidad2 == "año" or unidad2 == "años":
        n1 = float(input("Ingrese el valor de los Minutos: "))
        return print(f"{n1} Minutos equivale a:", n1 / 525600, "Año/s")


def Horas(unidad2):
    if unidad2 == "milisegundos" or unidad2 == "milisegundo":
        n1 = float(input("Ingrese el valor de los horas: "))
        return print(f"{n1} Horas equivale a:", n1 * 3.6e+6, "Milisegundos")

    elif unidad2 == "segundos" or unidad2 == "segundo":
        n1 = float(input("Ingrese el valor de los Horas: "))
        return print(f"{n1} Horas equivale a:", n1 * 3600, "Segundos")

    elif unidad2 == "minutos" or unidad2 == "minuto":
        n1 = float(input("Ingrese el valor de los Horas: "))
        return print(f"{n1} Horas equivale a:", n1 * 60, "Minutos")

    elif unidad2 == "dias" or unidad2 == "dia":
        n1 = float(input("Ingrese el valor de los Horas: "))
        return print(f"{n1} Horas equivale a:", n1 / 24, "Dias")

    elif unidad2 == "semanas" or unidad2 == "semana":
        n1 = float(input("Ingrese el valor de los Horas: "))
        return print(f"{n1} Horas equivale a:", n1 / 168, "Semanas")

    elif unidad2 == "mes" or unidad2 == "meses":
        n1 = float(input("Ingrese el valor de los Horas: "))
        return print(f"{n1} Horas equivale a:", n1 / 730, "Mes")

    elif unidad2 == "año" or unidad2 == "años":
        n1 = float(input("Ingrese el valor de los Horas: "))
        return print(f"{n1} Horas equivale a:", n1 / 8760, "Año/s")


def Dias(unidad2):
    if unidad2 == "milisegundos" or unidad2 == "milisegundo":
        n1 = float(input("Ingrese el valor de los Dias: "))
        return print(f"{n1} Dias equivale a:", n1 * 8.64e+7, "Milisegundos")

    elif unidad2 == "segundos" or unidad2 == "segundo":
        n1 = float(input("Ingrese el valor de los Dias: "))
        return print(f"{n1} Dias equivale a:", n1 * 86400, "Segundos")

    elif unidad2 == "minutos" or unidad2 == "minuto":
        n1 = float(input("Ingrese el valor de los Dias: "))
        return print(f"{n1} Dias equivale a:", n1 * 1440, "Horas")

    elif unidad2 == "horas" or unidad2 == "hora":
        n1 = float(input("Ingrese el valor de los Dias: "))
        return print(f"{n1} Dias equivale a:", n1 * 24, "Horas")

    elif unidad2 == "semanas" or unidad2 == "semana":
        n1 = float(input("Ingrese el valor de los Dias: "))
        return print(f"{n1} Dias equivale a:", n1 / 7, "Semanas")

    elif unidad2 == "mes" or unidad2 == "meses":
        n1 = float(input("Ingrese el valor de los Dias: "))
        return print(f"{n1} Dias equivale a:", n1 / 30.417, "Mes")

    elif unidad2 == "año" or unidad2 == "años":
        n1 = float(input("Ingrese el valor de los Dias: "))
        return print(f"{n1} Dias equivale a:", n1 / 365, "Año/s")


def Semanas(unidad2):
    if unidad2 == "milisegundos" or unidad2 == "milisegundo":
        n1 = float(input("Ingrese el valor de los Semanas: "))
        return print(f"{n1} Semanas equivale a:", n1 * 6.048e+8, "Milisegundos")

    elif unidad2 == "segundos" or unidad2 == "segundo":
        n1 = float(input("Ingrese el valor de los Semanas: "))
        return print(f"{n1} Semanas equivale a:", n1 * 604800, "Segundos")

    elif unidad2 == "minutos" or unidad2 == "minuto":
        n1 = float(input("Ingrese el valor de los Semanas: "))
        return print(f"{n1} Semanas equivale a:", n1 * 10080, "Minutos")

    elif unidad2 == "horas" or unidad2 == "hora":
        n1 = float(input("Ingrese el valor de los Semanas: "))
        return print(f"{n1} Semanas equivale a:", n1 * 168, "Horas")

    elif unidad2 == "dias" or unidad2 == "dia":
        n1 = float(input("Ingrese el valor de los Semanas: "))
        return print(f"{n1} Semanas equivale a:", n1 * 7, "Dias")

    elif unidad2 == "mes" or unidad2 == "meses":
        n1 = float(input("Ingrese el valor de los Semanas: "))
        return print(f"{n1} Semanas equivale a:", n1 / 4.345, "Mes")

    elif unidad2 == "año" or unidad2 == "años":
        n1 = float(input("Ingrese el valor de los Semanas: "))
        return print(f"{n1} Semanas equivale a:", n1 / 52.143, "Año/s")


def Meses(unidad2):
    if unidad2 == "milisegundos" or unidad2 == "milisegundo":
        n1 = float(input("Ingrese el valor de los Meses: "))
        return print(f"{n1} Meses equivale a:", n1 * 2.628e+9, "Milisegundos")

    elif unidad2 == "segundos" or unidad2 == "segundo":
        n1 = float(input("Ingrese el valor de los Meses: "))
        return print(f"{n1} Meses equivale a:", n1 * 2.628e+6, "Segundos")

    elif unidad2 == "minutos" or unidad2 == "minuto":
        n1 = float(input("Ingrese el valor de los Mes: "))
        return print(f"{n1} Meses equivale a:", n1 * 43800, "Minutos")

    elif unidad2 == "horas" or unidad2 == "hora":
        n1 = float(input("Ingrese el valor de los Meses: "))
        return print(f"{n1} Meses equivale a:", n1 * 730, "Horas")

    elif unidad2 == "dias" or unidad2 == "dia":
        n1 = float(input("Ingrese el valor de los Meses: "))
        return print(f"{n1} Meses equivale a:", n1 * 30.417, "Dias")

    elif unidad2 == "semanas" or unidad2 == "semana":
        n1 = float(input("Ingrese el valor de los Meses: "))
        return print(f"{n1} Meses equivale a:", n1 * 4.345, "Semanas")

    elif unidad2 == "año" or unidad2 == "años":
        n1 = float(input("Ingrese el valor de los Meses: "))
        return print(f"{n1} Meses equivale a:", n1 / 12, "Año/s")


def Agno(unidad2):
    if unidad2 == "milisegundos" or unidad2 == "milisegundo":
        n1 = float(input("Ingrese el valor de los Años: "))
        return print(f"{n1} Años equivale a:", n1 * 3.154e+10, "Milisegundos")

    elif unidad2 == "segundos" or unidad2 == "segundo":
        n1 = float(input("Ingrese el valor de los Años: "))
        return print(f"{n1} Años equivale a:", n1 * 3.154e+7, "Segundos")

    elif unidad2 == "minutos" or unidad2 == "minuto":
        n1 = float(input("Ingrese el valor de los Años: "))
        return print(f"{n1} Años equivale a:", n1 * 525600, "Minutos")

    elif unidad2 == "horas" or unidad2 == "hora":
        n1 = float(input("Ingrese el valor de los Años: "))
        return print(f"{n1} Años equivale a:", n1 * 8760, "Horas")

    elif unidad2 == "dias" or unidad2 == "dia":
        n1 = float(input("Ingrese el valor de los Años: "))
        return print(f"{n1} Años equivale a:", n1 * 365, "Dias")

    elif unidad2 == "semanas" or unidad2 == "semana":
        n1 = float(input("Ingrese el valor de los Años: "))
        return print(f"{n1} Años equivale a:", n1 * 52.143, "Semanas")

    elif unidad2 == "mes" or unidad2 == "meses":
        n1 = float(input("Ingrese el valor de los Años: "))
        return print(f"{n1} Años equivale a:", n1 * 12, "Meses")

