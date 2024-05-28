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
#clasificacionparaentradas:
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
#clasificacionparasalidas:
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

#clasificacionparaconsultas:
def clasificar_complejidad_entrada(datos_elementales_referenciados, registros_logicos_referenciados):
    if 1 <= datos_elementales_referenciados <= 4:
        if registros_logicos_referenciados <= 1:
            return "SIMPLE"
        elif registros_logicos_referenciados == 2:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 5 <= datos_elementales_referenciados <= 15:
        if registros_logicos_referenciados <= 1:
            return "SIMPLE"
        elif registros_logicos_referenciados == 2:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_elementales_referenciados >= 16
        if registros_logicos_referenciados <= 1:
            return "MEDIO"
        elif registros_logicos_referenciados == 2:
            return "COMPLEJO"
        else:
            return "COMPLEJO"

def clasificar_complejidad_salida(datos_elementales_referenciados, registros_logicos_referenciados):
    if 1 <= datos_elementales_referenciados <= 5:
        if registros_logicos_referenciados <= 1:
            return "SIMPLE"
        elif registros_logicos_referenciados <= 3:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 6 <= datos_elementales_referenciados <= 19:
        if registros_logicos_referenciados <= 1:
            return "SIMPLE"
        elif registros_logicos_referenciados <= 3:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_elementales_referenciados >= 20
        if registros_logicos_referenciados <= 1:
            return "MEDIO"
        elif registros_logicos_referenciados <= 3:
            return "COMPLEJO"
        else:
            return "COMPLEJO"

def clasificar_complejidad_consulta(tipo_clasificacion_entrada, tipo_clasificacion_salida):
    niveles_complejidad = ["SIMPLE", "MEDIO", "COMPLEJO"]
    indice_entrada = niveles_complejidad.index(tipo_clasificacion_entrada)
    indice_salida = niveles_complejidad.index(tipo_clasificacion_salida)
    return niveles_complejidad[max(indice_entrada, indice_salida)]

#clasificaciondeArchivos
def clasificar_complejidad_archivo_interno(datos_elementales_referenciados, registros_logic_referenciados):
    if 1 <= datos_elementales_referenciados <= 19:
        if registros_logic_referenciados == 1:
            return "SIMPLE"
        elif 2 <= registros_logic_referenciados <= 5:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 20 <= datos_elementales_referenciados <= 50:
        if registros_logic_referenciados == 1:
            return "SIMPLE"
        elif 2 <= registros_logic_referenciados <= 5:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_elementales_referenciados >= 51
        if registros_logic_referenciados == 1:
            return "MEDIO"
        elif 2 <= registros_logic_referenciados <= 5:
            return "COMPLEJO"
        else:
            return "COMPLEJO"

#clasificacionInterfaces
def clasificar_complejidad_archivo_interfaz(datos_elementales_referenciados, registros_logic_referenciados):
    if 1 <= datos_elementales_referenciados <= 19:
        if registros_logic_referenciados == 1:
            return "SIMPLE"
        elif 2 <= registros_logic_referenciados <= 5:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 20 <= datos_elementales_referenciados <= 50:
        if registros_logic_referenciados == 1:
            return "SIMPLE"
        elif 2 <= registros_logic_referenciados <= 5:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_elementales_referenciados >= 51
        if registros_logic_referenciados == 1:
            return "MEDIO"
        elif 2 <= registros_logic_referenciados <= 5:
            return "COMPLEJO"
        else:
            return "COMPLEJO"

#calculo de PF no ajustados
def calcular_puntos_de_funcion_no_ajustados(entradas_externas, salidas_externas, consultas_externas, archivos_internos, archivos_externos):
    # Contadores para cada tipo de función
    total_ee_simple = 0
    total_ee_medio = 0
    total_ee_complejo = 0

    total_se_simple = 0
    total_se_medio = 0
    total_se_complejo = 0

    total_ce_simple = 0
    total_ce_medio = 0
    total_ce_complejo = 0

    total_ai_simple = 0
    total_ai_medio = 0
    total_ai_complejo = 0

    total_ae_simple = 0
    total_ae_medio = 0
    total_ae_complejo = 0

    # Contar y clasificar entradas externas
    for nombre, datos, registros, tipo_complejidad in entradas_externas:
        if tipo_complejidad == "SIMPLE":
            total_ee_simple += 1
        elif tipo_complejidad == "MEDIO":
            total_ee_medio += 1
        elif tipo_complejidad == "COMPLEJO":
            total_ee_complejo += 1

    # Contar y clasificar salidas externas
    for nombre, datos, registros, tipo_complejidad in salidas_externas:
        if tipo_complejidad == "SIMPLE":
            total_se_simple += 1
        elif tipo_complejidad == "MEDIO":
            total_se_medio += 1
        elif tipo_complejidad == "COMPLEJO":
            total_se_complejo += 1

    # Contar y clasificar consultas externas
    for nombre, entradas_DE, entradas_RL, tipo_clasificacion_entrada, salidas_DE, salidas_RL, tipo_clasificacion_salida, tipo_clasificacion_consulta in consultas_externas:
        if tipo_clasificacion_consulta == "SIMPLE":
            total_ce_simple += 1
        elif tipo_clasificacion_consulta == "MEDIO":
            total_ce_medio += 1
        elif tipo_clasificacion_consulta == "COMPLEJO":
            total_ce_complejo += 1

    # Contar y clasificar archivos lógicos internos
    for nombre, datos, registros in archivos_internos:
        tipo_complejidad_archivo = clasificar_complejidad_archivo_interno(datos, registros)
        if tipo_complejidad_archivo == "SIMPLE":
            total_ai_simple += 1
        elif tipo_complejidad_archivo == "MEDIO":
            total_ai_medio += 1
        elif tipo_complejidad_archivo == "COMPLEJO":
            total_ai_complejo += 1

    # Contar y clasificar archivos de interfaz externa
    for nombre, datos, registros in archivos_externos:
        tipo_complejidad_archivo = clasificar_complejidad_archivo_interfaz(datos, registros)
        if tipo_complejidad_archivo == "SIMPLE":
            total_ae_simple += 1
        elif tipo_complejidad_archivo == "MEDIO":
            total_ae_medio += 1
        elif tipo_complejidad_archivo == "COMPLEJO":
            total_ae_complejo += 1

    # Calcular los puntos de función no ajustados
    total_ee = (total_ee_simple * 3) + (total_ee_medio * 4) + (total_ee_complejo * 6)
    total_se = (total_se_simple * 4) + (total_se_medio * 5) + (total_se_complejo * 7)
    total_ce = (total_ce_simple * 3) + (total_ce_medio * 4) + (total_ce_complejo * 6)
    total_ai = (total_ai_simple * 7) + (total_ai_medio * 10) + (total_ai_complejo * 15)
    total_ae = (total_ae_simple * 5) + (total_ae_medio * 7) + (total_ae_complejo * 10)

    total = total_ee + total_se + total_ce + total_ai + total_ae
    return total


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
            tipo_clasificacion_entrada = clasificar_complejidad_entrada(entradas_DE_referenciados, entradas_RL_referenciados)
            salidas_DE_referenciados = int(input("Número de Datos Elementales Referenciados (Parte de Salida): "))
            salidas_RL_referenciados = int(input("Número de Registros Lógicos Referenciados (Parte de Salida): "))
            tipo_clasificacion_salida = clasificar_complejidad_salida(salidas_DE_referenciados, salidas_RL_referenciados)
            tipo_clasificacion_consulta = clasificar_complejidad_consulta(tipo_clasificacion_entrada, tipo_clasificacion_salida)
            consultas_externas.append((nombre, entradas_DE_referenciados, entradas_RL_referenciados, tipo_clasificacion_entrada, salidas_DE_referenciados, salidas_RL_referenciados, tipo_clasificacion_salida, tipo_clasificacion_consulta))



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
           #punto_de_funcion()
           entradas_externas, salidas_externas, consultas_externas, archivos_internos, archivos_externos = punto_de_funcion()
           print("\nClasificación por Tipo de Complejidad:")
           if entradas_externas:
                print("\nResumen Entradas Externas:")
                for i, entrada in enumerate(entradas_externas):
                    nombre, datos, registros, tipo_complejidad = entrada
                    print(f"{i+1}. Nombre: {nombre}, Datos: {datos}, Registros: {registros}, Complejidad: {tipo_complejidad}")
            
           if salidas_externas:
                print("\nResumen Salidas Externas:")
                for i, salida in enumerate(salidas_externas):
                    nombre, datos, registros, tipo_complejidad = salida
                    print(f"{i+1}. Nombre: {nombre}, Datos: {datos}, Registros: {registros}, Complejidad: {tipo_complejidad}")
            
           if consultas_externas:
                print("\nResumen Consultas Externas:")
                for i, consulta in enumerate(consultas_externas):
                    nombre, entradas_DE, entradas_RL, tipo_clasificacion_entrada, salidas_DE, salidas_RL, tipo_clasificacion_salida, tipo_clasificacion_consulta = consulta
                    print(f"{i+1}. Nombre: {nombre} ")
                    print(f"   Entrada - Datos: {entradas_DE}, Registros: {entradas_RL}, Complejidad: {tipo_clasificacion_entrada}")
                    print(f"   Salida - Datos: {salidas_DE}, Registros: {salidas_RL}, Complejidad: {tipo_clasificacion_salida}")
                    print(f"   Complejidad Final: {tipo_clasificacion_consulta}")
          
           if archivos_internos:
                print("\nResumen Archivos Lógicos Internos:")
                for i, archivo in enumerate(archivos_internos):
                    nombre, datos, registros = archivo
                    tipo_complejidad_archivo = clasificar_complejidad_archivo_interno(datos, registros)
                    print(f"{i+1}. Nombre: {nombre}, Datos: {datos}, Registros: {registros}, Complejidad: {tipo_complejidad_archivo}")
            
           if archivos_externos:
                print("\nResumen Archivos de Interfaz Externa:")
                for i, archivo in enumerate(archivos_externos):
                    nombre, datos, registros = archivo
                    tipo_complejidad_archivo = clasificar_complejidad_archivo_interfaz(datos, registros)
                    print(f"{i+1}. Nombre: {nombre}, Datos: {datos}, Registros: {registros}, Complejidad: {tipo_complejidad_archivo}")


# Calcular puntos de función no ajustados
           puntos_no_ajustados = calcular_puntos_de_funcion_no_ajustados(entradas_externas, salidas_externas, consultas_externas, archivos_internos, archivos_externos)
           print("\nCalculando Puntos de Función No Ajustados...")
           print("Puntos de Función No Ajustados:", puntos_no_ajustados)

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

