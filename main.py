# autores: Kenia Stephannie Tepas Mazariego, Victoria Castro
def mostrar_menu():
    print("Bienvenido al Sistema de Estimaciones")
    print("Analisis de Costos Informaticos 2024")
    print("Creado por: Kenia Tepas y Victoria Castro")
    print("Elija una opción")
    print("1. Punto de Función")
    print("2. Casos de Uso")
    print("3. COSMIC")
    print("4. Salir")

#calculandotipodecomplejidadPF:
def clasificar_complejidad_entrada_externa(datos_elementales_referenciados, registros_logic_referenciados):
    if 1 <= datos_elementales_referenciados <= 4:
        if registros_logic_referenciados <= 1:
            return "SIMPLE"
        elif registros_logic_referenciados == 2:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 5 <= datos_elementales_referenciados <= 15:
        if registros_logic_referenciados <= 1:
            return "SIMPLE"
        elif registros_logic_referenciados == 2:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_elementales_referenciados >= 16
        if registros_logic_referenciados <= 1:
            return "MEDIO"
        elif registros_logic_referenciados == 2:
            return "COMPLEJO"
        else:
            return "COMPLEJO"

def clasificar_complejidad_salida_externa(datos_elementales_referenciados, registros_logic_referenciados):
    if 1 <= datos_elementales_referenciados <= 5:
        if registros_logic_referenciados <= 1:
            return "SIMPLE"
        elif registros_logic_referenciados <= 3:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 6 <= datos_elementales_referenciados <= 19:
        if registros_logic_referenciados <= 1:
            return "SIMPLE"
        elif registros_logic_referenciados <= 3:
            return "MEDIO"
        else:
            return "COMPLEJO"
    elif registros_logic_referenciados <= 1:
        return "MEDIO"
    elif registros_logic_referenciados <= 3:
        return "COMPLEJO"
    else:
        return "COMPLEJO"



#metodo punto de funcion
def punto_de_funcion():
    print("Has seleccionado Punto de Función")
    # Aquí puedes agregar la lógica para Punto de Función
    print("Por favor, ingresa la siguiente información:")

      # Solicitar el número de entradas externas
    num_entradas_externas = int(input("Número de entradas externas: "))
    entradas_externas = []
    if num_entradas_externas > 0:
        # Recopilar información para cada entrada externa
        for i in range(num_entradas_externas):
            print(f"\nEntrada Externa {i+1}:")
            nombre = input("Nombre: ")
            datos_elementales_referenciados = int(input("Número de Datos Elementales Referenciados: "))
            registros_logic_referenciados = int(input("Número de Registros Lógicos Referenciados: "))
            tipo_clasificacion = clasificar_complejidad_entrada_externa(datos_elementales_referenciados, registros_logic_referenciados)
            entradas_externas.append((nombre, datos_elementales_referenciados, registros_logic_referenciados, tipo_clasificacion))

    # Solicitar el número de salidas externas
    num_salidas_externas = int(input("\nNúmero de salidas externas: "))
    salidas_externas = []
    if num_salidas_externas > 0:
        # Recopilar información para cada salida externa
        for i in range(num_salidas_externas):
            print(f"\nSalida Externa {i+1}:")
            nombre = input("Nombre: ")
            datos_elementales_referenciados = int(input("Número de Datos Elementales Referenciados: "))
            registros_logic_referenciados = int(input("Número de Registros Lógicos Referenciados: "))
            tipo_clasificacion = clasificar_complejidad_salida_externa(datos_elementales_referenciados, registros_logic_referenciados)
            salidas_externas.append((nombre, datos_elementales_referenciados, registros_logic_referenciados, tipo_clasificacion))
   
   
    # Solicitar el número de consultas externas
    num_consultas_externas = int(input("\nNúmero de consultas externas: "))
    consultas_externas = []
    if num_consultas_externas > 0:
        # Recopilar información para cada consulta externa
        for i in range(num_consultas_externas):
            print(f"\nConsulta Externa {i+1}:")
            nombre = input("Nombre: ")
            entradas_DE_referenciados = int(input("Número de Datos Elementales Referenciados (Parte de Entrada): "))
            entradas_RL_referenciados = int(input("Número de Registros Lógicos Referenciados (Parte de Entrada): "))
            salidas_DE_referenciados = int(input("Número de Datos Elementales Referenciados (Parte de Salida): "))
            salidas_RL_referenciados = int(input("Número de Registros Lógicos Referenciados (Parte de Salida): "))
            consultas_externas.append((nombre, entradas_DE_referenciados, entradas_RL_referenciados, salidas_DE_referenciados, salidas_RL_referenciados))

    # Solicitar el número de archivos lógicos internos
    num_archivos_internos = int(input("\nNúmero de archivos lógicos internos: "))
    archivos_internos = []
    if num_archivos_internos > 0:
        # Recopilar información para cada archivo lógico interno
        for i in range(num_archivos_internos):
            print(f"\nArchivo Lógico Interno {i+1}:")
            nombre = input("Nombre: ")
            datos_elementales_referenciados = int(input("Número de Datos Elementales Referenciados: "))
            registros_logic_referenciados = int(input("Número de Registros Lógicos Referenciados: "))
            archivos_internos.append((nombre, datos_elementales_referenciados, registros_logic_referenciados))

    # Solicitar el número de archivos de interfaz externa
    num_archivos_externos = int(input("\nNúmero de archivos de interfaz externa: "))
    archivos_externos = []
    if num_archivos_externos > 0:
        # Recopilar información para cada archivo de interfaz externa
        for i in range(num_archivos_externos):
            print(f"\nArchivo de Interfaz Externa {i+1}:")
            nombre = input("Nombre: ")
            datos_elementales_referenciados = int(input("Número de Datos Elementales Referenciados: "))
            registros_logic_referenciados = int(input("Número de Registros Lógicos Referenciados: "))
            archivos_externos.append((nombre, datos_elementales_referenciados, registros_logic_referenciados))


    return entradas_externas, salidas_externas, consultas_externas, archivos_internos, archivos_externos

##fin de metodo punto de funcion



def casos_de_uso():
    print("Has seleccionado Casos de Uso")
    # Aquí puedes agregar la lógica para Casos de Uso

def cosmic():
    print("Has seleccionado COSMIC")
    # Aquí puedes agregar la lógica para COSMIC

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
           punto_de_funcion()
           


        elif opcion == "2":
            casos_de_uso()
        elif opcion == "3":
            cosmic()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()

