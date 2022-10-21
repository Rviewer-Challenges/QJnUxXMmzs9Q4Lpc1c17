import Tiempo, Masa, Longitud, Tamaño_Datos

print("Bienvenidos al convertidor")

opcion = "vacio"

while opcion != "x":
   print("\nElige que desea convertir: A- Tiempo, B- Masa, C- Longitud, D - Tamaño de datos, X - Salir. ")
   opcion = input().lower()

   if opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d" and opcion != "x":
        while opcion != "a" or opcion != "b" or opcion != "c" or opcion != "d" or opcion != "x":
            opcion = input("La opcion que elegiste no es una de las recomendadas, por favor elija entra"
                           " A, B, C, D o X para salir: ").lower()

   if opcion == "a":
      while opcion != "e":
         opcion = input("\nElige la Medida de Tiempo que quieras comparar: milisegundos, segundos, minutos, horas,"
                        " dias, semanas, meses, años \no presione E para salir y elegir otra unidad: ").lower()

         if opcion == "milisegundos" or opcion == "milisegundo":
            unidad = input("Con que otra Medida de Tiempo quieres calcular los milisegundos?: ").lower()
            Tiempo.milisegundos(unidad)

         elif opcion == "segundos" or opcion == "segundo":
            unidad = input("Con que otra Medida de Tiempo quieres calcular los segundos?: ").lower()
            Tiempo.segundos(unidad)

         elif opcion == "minutos" or opcion == "minuto":
            unidad = input("con que otra Medida de Tiempo quieres calcular los minutos?: ").lower()
            Tiempo.minutos(unidad)

         elif opcion == "horas" or opcion == "hora":
            unidad = input("Con que otra Medida de Tiempo quieres calcular las horas?: ").lower()
            Tiempo.Horas(unidad)

         elif opcion == "dias" or opcion == "dia":
            unidad = input("Con que otra Medida de Tiempo quieres calcular los dias?: ").lower()
            Tiempo.Dias(unidad)

         elif opcion == "semanas" or opcion == "semana":
            unidad = input("Con que otra Medida de Tiempo quieres calcular las semanas?: ").lower()
            Tiempo.Semanas(unidad)

         elif opcion == "meses" or opcion == "mes":
            unidad = input("Con que otra Medida de Tiempo quieres calcular los meses?: ").lower()
            Tiempo.Meses(unidad)

         elif opcion == "años" or opcion == "año":
            unidad = input("Con que otra Medida de Tiempo quieres calcular los Años?: ").lower()
            Tiempo.Agno(unidad)

   if opcion == "b":
      while opcion != "e":
         opcion = input("Elige el tipo de Masa que quieras comparar: miligramo, gramo, kilogramo, "
                        "tonelada o presione E para salir y elegir otra unidad: ").lower()

         if opcion == "miligramo" or opcion == "miligramos":
            masa = input("Con que otro tipo de Masa quieres calcular los Miligramos?: ").lower()
            Masa.miligramo(masa)

         elif opcion == "gramo" or opcion == "gramos":
            masa = input("Con que otro tipo de Masa quieres calcular los Gramos?: ").lower()
            Masa.gramo(masa)

         elif opcion == "kilogramo" or opcion == "kilogramos":
            masa = input("Con que otro tipo de Masa quieres calcular los Kilogramos?: ").lower()
            Masa.kilogramo(masa)

         elif opcion == "tonelada" or opcion == "toneladas":
            masa = input("Con que otro tipo de Masa quieres calcular la Tonelada?: ").lower()
            Masa.tonelada(masa)

   if opcion == "c":
      while opcion != "e":
         opcion = input("Elige el tipo de Longitudes que quieras comparar: Yarda, Milla, Milimetro, Centimetro, Metro,"
                        "\n Kilometro o presione E para salir y elegir otra unidad: ").lower()

         if opcion == "yarda" or opcion == "yardas":
            medida = input("Con que otro tipo de Longitud quieres calcular las Yardas?: ").lower()
            Longitud.yarda(medida)

         elif opcion == "milla" or opcion == "millas":
            medida = input("Con que otro tipo de Longitud quieres calcular las Millas?: ").lower()
            Longitud.milla(medida)

         elif opcion == "milimetro" or opcion == "milimetros":
            medida = input("Con que otro tipo de Longitud quieres calcular los Milimetros?: ").lower()
            Longitud.milimetro(medida)

         elif opcion == "centimetro" or opcion == "centimetros":
            medida = input("Con que otro tipo de Longitud quieres calcular los Centimetros?: ").lower()
            Longitud.centimetro(medida)

         elif opcion == "metro" or opcion == "metros":
            medida = input("Con que otro tipo de Longitud quieres calcular los Metros?: ").lower()
            Longitud.metro(medida)

         elif opcion == "kilometro" or opcion == "kilometros":
            medida = input("Con que otro tipo de Longitud quieres calcular los Kilometros?: ").lower()
            Longitud.kilometro(medida)

   if opcion == "d":
      while opcion != "e":
         opcion = input("Elige el tipo de Tamaño de Datos que quieras calcular: Byte, Kilobyte, Megabyte,"
                        "\n Gigabyte, Terabyte o presione E para salir y elegir otra unidad: ").lower()

         if opcion == "byte":
            dato = input("Con que otro tipo de Tamaño de Datos quieres calcular los Byte?: ").lower()
            Tamaño_Datos.byte(dato)

         elif opcion == "kilobyte":
            dato = input("Con que otro tipo de Tamaño de Datos quieres calcular los Kilobyte?: ").lower()
            Tamaño_Datos.kilobyte(dato)

         elif opcion == "megabyte":
            dato = input("Con que otro tipo de Tamaño de Datos quieres calcular los Megabyte?: ").lower()
            Tamaño_Datos.megabyte(dato)

         elif opcion == "gigabyte":
            dato = input("Con que otro tipo de Tamaño de Datos quieres calcular los Gigabyte?: ").lower()
            Tamaño_Datos.gigabyte(dato)

         elif opcion == "terabyte":
            dato = input("Con que otro tipo de Tamaño de Datos quieres calcular los Terabyte?: ").lower()
            Tamaño_Datos.terabyte(dato)

print("Muchas gracias por usar el convertidor.")

print("Perfil de Linkedin: https://www.linkedin.com/in/adriel-ormaechea-151455230/")
