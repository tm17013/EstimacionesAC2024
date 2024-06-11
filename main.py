# autores: Kenia Stephannie Tepas Mazariego, Andrea Victoria Castro Jiménez
def menu():
    print("**********************************************")
    print("*    Bienvenido al Sistema de Estimaciones   *")
    print("*    Analisis de Costos Informaticos 2024    *")
    print("*  Creado por: Kenia Tepas y Victoria Castro *")
    print("**********************************************")
    print("\nElija una opción")
    print("1. Punto de Función")
    print("2. Casos de Uso")
    print("3. COSMIC")
    print("4. Salir")

#calculandotipodecomplejidadPF:
#clasificacionparaentradas:
def clasificar_complejidad_ee(datos_referenciados, registros_referenciados):
    if 1 <= datos_referenciados <= 4:
        if registros_referenciados <= 1:
            return "SIMPLE"
        elif registros_referenciados == 2:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 5 <= datos_referenciados <= 15:
        if registros_referenciados <= 1:
            return "SIMPLE"
        elif registros_referenciados == 2:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_referenciados >= 16
        if registros_referenciados <= 1:
            return "MEDIO"
        elif registros_referenciados == 2:
            return "COMPLEJO"
        else:
            return "COMPLEJO"
#clasificacionparasalidas:
def clasificar_complejidad_se(datos_referenciados, registros_referenciados):
    if 1 <= datos_referenciados <= 5:
        if registros_referenciados <= 1:
            return "SIMPLE"
        elif registros_referenciados <= 3:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 6 <= datos_referenciados <= 19:
        if registros_referenciados <= 1:
            return "SIMPLE"
        elif registros_referenciados <= 3:
            return "MEDIO"
        else:
            return "COMPLEJO"
    elif registros_referenciados <= 1:
        return "MEDIO"
    elif registros_referenciados <= 3:
        return "COMPLEJO"
    else:
        return "COMPLEJO"

#clasificacionparaconsultas:
def clasificar_complejidad_entrada(datos_referenciados, registros_referenciados):
    if 1 <= datos_referenciados <= 4:
        if registros_referenciados <= 1:
            return "SIMPLE"
        elif registros_referenciados == 2:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 5 <= datos_referenciados <= 15:
        if registros_referenciados <= 1:
            return "SIMPLE"
        elif registros_referenciados == 2:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_referenciados >= 16
        if registros_referenciados <= 1:
            return "MEDIO"
        elif registros_referenciados == 2:
            return "COMPLEJO"
        else:
            return "COMPLEJO"

def clasificar_complejidad_salida(datos_referenciados, registros_referenciados):
    if 1 <= datos_referenciados <= 5:
        if registros_referenciados <= 1:
            return "SIMPLE"
        elif registros_referenciados <= 3:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 6 <= datos_referenciados <= 19:
        if registros_referenciados <= 1:
            return "SIMPLE"
        elif registros_referenciados <= 3:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_referenciados >= 20
        if registros_referenciados <= 1:
            return "MEDIO"
        elif registros_referenciados <= 3:
            return "COMPLEJO"
        else:
            return "COMPLEJO"

def clasificar_complejidad_ce(tipo_clasificacion_entrada, tipo_clasificacion_salida):
    niveles_complejidad = ["SIMPLE", "MEDIO", "COMPLEJO"]
    indice_entrada = niveles_complejidad.index(tipo_clasificacion_entrada)
    indice_salida = niveles_complejidad.index(tipo_clasificacion_salida)
    return niveles_complejidad[max(indice_entrada, indice_salida)]

#clasificaciondeArchivos
def clasificar_complejidad_ali(datos_referenciados, registros_referenciados):
    if 1 <= datos_referenciados <= 19:
        if registros_referenciados == 1:
            return "SIMPLE"
        elif 2 <= registros_referenciados <= 5:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 20 <= datos_referenciados <= 50:
        if registros_referenciados == 1:
            return "SIMPLE"
        elif 2 <= registros_referenciados <= 5:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_elementales_referenciados >= 51
        if registros_referenciados == 1:
            return "MEDIO"
        elif 2 <= registros_referenciados <= 5:
            return "COMPLEJO"
        else:
            return "COMPLEJO"

#clasificacionInterfaces
def clasificar_complejidad_aie(datos_referenciados, registros_referenciados):
    if 1 <= datos_referenciados <= 19:
        if registros_referenciados == 1:
            return "SIMPLE"
        elif 2 <= registros_referenciados <= 5:
            return "SIMPLE"
        else:
            return "MEDIO"
    elif 20 <= datos_referenciados <= 50:
        if registros_referenciados == 1:
            return "SIMPLE"
        elif 2 <= registros_referenciados <= 5:
            return "MEDIO"
        else:
            return "COMPLEJO"
    else:  # datos_referenciados >= 51
        if registros_referenciados == 1:
            return "MEDIO"
        elif 2 <= registros_referenciados <= 5:
            return "COMPLEJO"
        else:
            return "COMPLEJO"

#calculo de PF no ajustados
def pf_no_ajustados(entradas_externas, salidas_externas, consultas_externas, archivos_internos, archivos_externos):
    #variables
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

    #cuenta y clasifica las entradas
    for nombre, datos, registros, tipo_complejidad in entradas_externas:
        if tipo_complejidad == "SIMPLE":
            total_ee_simple += 1
        elif tipo_complejidad == "MEDIO":
            total_ee_medio += 1
        elif tipo_complejidad == "COMPLEJO":
            total_ee_complejo += 1

    #cuenta y clasifica las salidas
    for nombre, datos, registros, tipo_complejidad in salidas_externas:
        if tipo_complejidad == "SIMPLE":
            total_se_simple += 1
        elif tipo_complejidad == "MEDIO":
            total_se_medio += 1
        elif tipo_complejidad == "COMPLEJO":
            total_se_complejo += 1

    #cuenta y clasifica las consultas
    for nombre, entradas_DE, entradas_RL, tipo_clasificacion_entrada, salidas_DE, salidas_RL, tipo_clasificacion_salida, tipo_clasificacion_consulta in consultas_externas:
        if tipo_clasificacion_consulta == "SIMPLE":
            total_ce_simple += 1
        elif tipo_clasificacion_consulta == "MEDIO":
            total_ce_medio += 1
        elif tipo_clasificacion_consulta == "COMPLEJO":
            total_ce_complejo += 1

    #cuenta y clasifica los ali
    for nombre, datos, registros in archivos_internos:
        tipo_complejidad_archivo = clasificar_complejidad_ali(datos, registros)
        if tipo_complejidad_archivo == "SIMPLE":
            total_ai_simple += 1
        elif tipo_complejidad_archivo == "MEDIO":
            total_ai_medio += 1
        elif tipo_complejidad_archivo == "COMPLEJO":
            total_ai_complejo += 1

    #cuenta y clasifica los aie
    for nombre, datos, registros in archivos_externos:
        tipo_complejidad_archivo = clasificar_complejidad_aie(datos, registros)
        if tipo_complejidad_archivo == "SIMPLE":
            total_ae_simple += 1
        elif tipo_complejidad_archivo == "MEDIO":
            total_ae_medio += 1
        elif tipo_complejidad_archivo == "COMPLEJO":
            total_ae_complejo += 1

    #calculo los puntos de función no ajustados
    total_ee = (total_ee_simple * 3) + (total_ee_medio * 4) + (total_ee_complejo * 6)
    total_se = (total_se_simple * 4) + (total_se_medio * 5) + (total_se_complejo * 7)
    total_ce = (total_ce_simple * 3) + (total_ce_medio * 4) + (total_ce_complejo * 6)
    total_ai = (total_ai_simple * 7) + (total_ai_medio * 10) + (total_ai_complejo * 15)
    total_ae = (total_ae_simple * 5) + (total_ae_medio * 7) + (total_ae_complejo * 10)

    total = total_ee + total_se + total_ce + total_ai + total_ae
    return total

#calculodeFactordeAjuste
def calcular_factor_ajuste():
    print("Por favor, responde las siguientes preguntas utilizando una escala del 0 al 5:")
    preguntas = [
        "1. ¿El sistema requiere respaldo y recuperación confiables?",
        "2. ¿Se requieren comunicaciones de datos especializadas para transferir información hacia o desde la aplicación?",
        "3. ¿Existen funciones de procesamiento distribuidas?",
        "4. ¿El desempeño es crucial?",
        "5. ¿El sistema correrá en un entorno operativo existente enormemente utilizado?",
        "6. ¿El sistema requiere entrada de datos en línea?",
        "7. ¿La entrada de datos en línea requiere que la transacción de entrada se construya sobre múltiples pantallas u operaciones?",
        "8. ¿Los ALI se actualizan en línea?",
        "9. ¿Las entradas, salidas, archivos o consultas son complejos?",
        "10. ¿El procesamiento interno es complejo?",
        "11. ¿El código se diseña para ser reutilizable?",
        "12. ¿La conversión y la instalación se incluyen en el diseño?",
        "13. ¿El sistema se diseña para instalaciones múltiples en diferentes organizaciones?",
        "14. ¿La aplicación se diseña para facilitar el cambio y su uso por parte del usuario?"
    ]

    factor_ajuste = 0
    for pregunta in preguntas:
        respuesta = int(input(f"{pregunta} (0 a 5): "))
        factor_ajuste += respuesta

    return factor_ajuste

#calcularPFA
def pfa(puntos_no_ajustados, factor_ajuste):
    #fórmula para calcular los puntos de función ajustados
    puntos_funcion_ajustados = puntos_no_ajustados * (0.65 + (0.01 * factor_ajuste))
    return puntos_funcion_ajustados

#metodo punto de funcion
def punto_de_funcion():
    print("Has seleccionado Punto de Función")
    #informacion de dominios
    print("Por favor, ingresa la siguiente información:")
      #número de entradas externas
    num_entradas_externas = int(input("Número de entradas externas: "))
    entradas_externas = []
    if num_entradas_externas > 0:
        #información para cada entrada externa
        for i in range(num_entradas_externas):
            print(f"\nEntrada Externa {i+1}:")
            nombre = input("Nombre: ")
            datos_referenciados = int(input("Número de Datos Elementales Referenciados: "))
            registros_referenciados = int(input("Número de Registros Lógicos Referenciados: "))
            tipo_clasificacion = clasificar_complejidad_ee(datos_referenciados, registros_referenciados)
            entradas_externas.append((nombre, datos_referenciados, registros_referenciados, tipo_clasificacion))

    #número de salidas externas
    num_salidas_externas = int(input("\nNúmero de salidas externas: "))
    salidas_externas = []
    if num_salidas_externas > 0:
        #información para cada salida externa
        for i in range(num_salidas_externas):
            print(f"\nSalida Externa {i+1}:")
            nombre = input("Nombre: ")
            datos_referenciados = int(input("Número de Datos Elementales Referenciados: "))
            registros_referenciados = int(input("Número de Registros Lógicos Referenciados: "))
            tipo_clasificacion = clasificar_complejidad_se(datos_referenciados, registros_referenciados)
            salidas_externas.append((nombre, datos_referenciados, registros_referenciados, tipo_clasificacion))
   
   
    #número de consultas externas
    num_consultas_externas = int(input("\nNúmero de consultas externas: "))
    consultas_externas = []
    if num_consultas_externas > 0:
        #información para cada consulta externa
        for i in range(num_consultas_externas):
            print(f"\nConsulta Externa {i+1}:")
            nombre = input("Nombre: ")
            entradas_DE_referenciados = int(input("Número de Datos Elementales Referenciados (Parte de Entrada): "))
            entradas_RL_referenciados = int(input("Número de Registros Lógicos Referenciados (Parte de Entrada): "))
            tipo_clasificacion_entrada = clasificar_complejidad_entrada(entradas_DE_referenciados, entradas_RL_referenciados)
            salidas_DE_referenciados = int(input("Número de Datos Elementales Referenciados (Parte de Salida): "))
            salidas_RL_referenciados = int(input("Número de Registros Lógicos Referenciados (Parte de Salida): "))
            tipo_clasificacion_salida = clasificar_complejidad_salida(salidas_DE_referenciados, salidas_RL_referenciados)
            tipo_clasificacion_consulta = clasificar_complejidad_ce(tipo_clasificacion_entrada, tipo_clasificacion_salida)
            consultas_externas.append((nombre, entradas_DE_referenciados, entradas_RL_referenciados, tipo_clasificacion_entrada, salidas_DE_referenciados, salidas_RL_referenciados, tipo_clasificacion_salida, tipo_clasificacion_consulta))



    #número de archivos lógicos internos
    num_archivos_internos = int(input("\nNúmero de archivos lógicos internos: "))
    archivos_internos = []
    if num_archivos_internos > 0:
        #información para cada archivo lógico interno
        for i in range(num_archivos_internos):
            print(f"\nArchivo Lógico Interno {i+1}:")
            nombre = input("Nombre: ")
            datos_referenciados = int(input("Número de Datos Elementales Referenciados: "))
            registros_referenciados = int(input("Número de Registros Lógicos Referenciados: "))
            archivos_internos.append((nombre, datos_referenciados, registros_referenciados))

    #número de archivos de interfaz externa
    num_archivos_externos = int(input("\nNúmero de archivos de interfaz externa: "))
    archivos_externos = []
    if num_archivos_externos > 0:
        #información para cada archivo de interfaz externa
        for i in range(num_archivos_externos):
            print(f"\nArchivo de Interfaz Externa {i+1}:")
            nombre = input("Nombre: ")
            datos_referenciados = int(input("Número de Datos Elementales Referenciados: "))
            registros_referenciados = int(input("Número de Registros Lógicos Referenciados: "))
            archivos_externos.append((nombre, datos_referenciados, registros_referenciados))


    return entradas_externas, salidas_externas, consultas_externas, archivos_internos, archivos_externos

##FIN de metodo punto de funcion


#INICIO CASO DE USO
def casos_de_uso():
    print("Has seleccionado Casos de Uso")
    #se itera la informacion  de los actores de caso de uso
    num_actores = int(input("\nNúmero de actores: "))
    peso_actores = []
    
    for i in range(num_actores):  
        peso_actores.append(int(input(f"Peso del actor {i+1} (1.Simple, 2.Medio, 3.Complejo): ")))
        
    total_peso_actores = sum(peso_actores)
    
    #se itera la informacion de los casos de uso
    num_casos_uso = int(input("\nNúmero de casos de uso: "))
    peso_casos_uso = []
    
    for i in range(num_casos_uso):
        num_transacciones = int(input(f"¿Cuántas transacciones tiene el caso de uso {i+1}? -> "))
        if num_transacciones < 4:
            peso_casos_uso.append(5)
        elif num_transacciones < 8:
            peso_casos_uso.append(10)
        else:
            peso_casos_uso.append(15)  

    total_peso_casos_uso = sum(peso_casos_uso)

    #calculo de punto de casos de uso no ajustados
    puntos_casos_uso_no_ajustados = total_peso_actores +  total_peso_casos_uso

    #Factores Técnicos (TCF)
    print("\nIngresa los valores de los factores técnicos (0-5):\n")
    factores_tecnicos = [
        ("1. Sistema distribuido", 2),
        ("2. Rendimiento o tiempo de respuesta", 1),
        ("3. Eficiencia del usuario final", 1),
        ("4. Procesamiento interno complejo", 1),
        ("5. El código debe ser reutilizable", 1),
        ("6. Facilidad de instalación", 0.5),
        ("7. Facilidad de uso", 0.5),
        ("8. Portabilidad", 2),
        ("9. Facilidad de cambio", 1),
        ("10. Concurrencia", 1),
        ("11. Características especiales de seguridad", 1),
        ("12. Provee acceso directo a terceras partes", 1),
        ("13. Se requiere facilidades especiales de entrenamiento a usuario", 1)
    ]
    total_factores_tecnicos = 0

    for factor, peso in factores_tecnicos:
        valor = int(input(f"{factor}: "))
        total_factores_tecnicos += valor * peso

    tcf = 0.6 + (0.01 * total_factores_tecnicos)

    #Factores Ambientales (ECF)
    print("\nIngresa los valores de los factores ambientales (1-5):\n")
    factores_ambientales = [
        ("1. Familiaridad con el modelo de proyecto utilizado", 1.5),
        ("2. Personal tiempo parcial", -1),
        ("3. Capacidad del analista líder", 0.5),
        ("4. Experiencia en la aplicación", 0.5),
        ("5. Experiencia en orientación a objetos", 1),
        ("6. Motivación", 1),
        ("7. Dificultad del lenguaje de programación", -1),
        ("8. Estabilidad de los requerimientos", 2)
    ]
    total_factores_ambientales = 0

    for factor, peso in factores_ambientales:
        valor = int(input(f"{factor}: "))
        total_factores_ambientales += valor * peso

    ecf = 1.4 + (-0.03 * total_factores_ambientales)

    #calculo de puntos de caso de uso ajustados (UCP)
    ucp = puntos_casos_uso_no_ajustados * tcf * ecf
        
    #los resultados
    print("\nResultados:")
    print(f"\nPeso de los actores(UAW): {total_peso_actores}\nPeso de los casos de uso(UUCW): {total_peso_casos_uso}\nPuntos de Casos de Uso No Ajustados(UUCP): {puntos_casos_uso_no_ajustados}")
    print(f"Total de Factores Técnicos: {total_factores_tecnicos}")
    print(f"TCF (Factor de Complejidad Técnica): {tcf}")
    print(f"Total de Factores Ambientales: {total_factores_ambientales}")
    print(f"ECF (Factor de Complejidad Ambiental): {ecf:.4f}")
    print(f"Puntos de Caso de Uso Ajustados (UCP): {ucp:.4f}\n")

#FIN CASO DE USO

#INICIO METODO COSMIC
def cosmic():
    print("Has seleccionado COSMIC")
    #solicitando datos del usuario para las funciones funcionales
    funciones = {
    "entradas": 0,
    "salidas": 0,
    "lecturas": 0,
    "escrituras": 0
    }

    for tipo in funciones:
        while True:
            try:
                cantidad = int(input(f"Número de {tipo.capitalize()}: "))
                funciones[tipo] = cantidad
                break
            except ValueError:
                print("Entrada no válida. Inténtalo de nuevo.")

    #calcular el tamaño total en CFP
    cfp_total = sum(funciones.values())
    
    print(f"\nTamaño total del software en Puntos de Función COSMIC (CFP): {cfp_total}")
    #duracion del proyecto
    while True:
        respuesta_cpf = input("\n¿Desea conocer la duración del proyecto en meses? (s/n): ").lower()
        if respuesta_cpf in ['s', 'n']:
            break
        else:
            print("Opción no válida, por favor ingrese 's' para SI o 'n' para NO.")

    if respuesta_cpf == "s":
        while True:
            try:
                cfp_historico = int(input("Ingrese el histórico de CFP mensual promedio: "))
                break
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número.")
        duracion_proyecto = cfp_total/cfp_historico

        print(f"\nLa duración del proyecto es de {round(duracion_proyecto,3)} meses\n")
#FIN METODO COSMIC

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
           #punto_de_funcion()
           entradas_externas, salidas_externas, consultas_externas, archivos_internos, archivos_externos = punto_de_funcion()
           print("\nCLASIFICACIÓN POR TIPO DE COMPLEJIDAD:")
           if entradas_externas:
                print("\nResumen de Entradas Externas (EE):")
                for i, entrada in enumerate(entradas_externas):
                    nombre, datos, registros, tipo_complejidad = entrada
                    print(f"{i+1}. Nombre: {nombre}, Datos: {datos}, Registros: {registros}, Complejidad: {tipo_complejidad}")
            
           if salidas_externas:
                print("\nResumen de Salidas Externas(SE):")
                for i, salida in enumerate(salidas_externas):
                    nombre, datos, registros, tipo_complejidad = salida
                    print(f"{i+1}. Nombre: {nombre}, Datos: {datos}, Registros: {registros}, Complejidad: {tipo_complejidad}")
            
           if consultas_externas:
                print("\nResumen de Consultas Externas(CE):")
                for i, consulta in enumerate(consultas_externas):
                    nombre, entradas_DE, entradas_RL, tipo_clasificacion_entrada, salidas_DE, salidas_RL, tipo_clasificacion_salida, tipo_clasificacion_consulta = consulta
                    print(f"{i+1}. Nombre: {nombre} ")
                    print(f"   Entrada - Datos: {entradas_DE}, Registros: {entradas_RL}, Complejidad: {tipo_clasificacion_entrada}")
                    print(f"   Salida - Datos: {salidas_DE}, Registros: {salidas_RL}, Complejidad: {tipo_clasificacion_salida}")
                    print(f"   Complejidad Final: {tipo_clasificacion_consulta}")
          
           if archivos_internos:
                print("\nResumen de Archivos Lógicos Internos(ALI):")
                for i, archivo in enumerate(archivos_internos):
                    nombre, datos, registros = archivo
                    tipo_complejidad_archivo = clasificar_complejidad_ali(datos, registros)
                    print(f"{i+1}. Nombre: {nombre}, Datos: {datos}, Registros: {registros}, Complejidad: {tipo_complejidad_archivo}")
            
           if archivos_externos:
                print("\nResumen de Archivos de Interfaz Externa(AIE):")
                for i, archivo in enumerate(archivos_externos):
                    nombre, datos, registros = archivo
                    tipo_complejidad_archivo = clasificar_complejidad_aie(datos, registros)
                    print(f"{i+1}. Nombre: {nombre}, Datos: {datos}, Registros: {registros}, Complejidad: {tipo_complejidad_archivo}")


           # Calcular puntos de función no ajustados
           puntos_no_ajustados = pf_no_ajustados(entradas_externas, salidas_externas, consultas_externas, archivos_internos, archivos_externos)
           print("\nCalculando Puntos de Función No Ajustados...")
           print("Puntos de Función No Ajustados:", puntos_no_ajustados)
           print("\n")

           # Calcular factor de ajuste
           factor_ajuste = calcular_factor_ajuste()
           print("\nCalculando Total de Factor de Ajuste...")
           print("Total de Factor de Ajuste:", factor_ajuste)
           factor_ajuste_nuevo = (factor_ajuste * 0.01)+ 0.65
           print("\nCalculando Factor de Ajuste...")
           print("Factor de Ajuste:", factor_ajuste_nuevo)
           print("\n")

           # Calcular puntos de función ajustados
           puntos_funcion_ajustados = pfa(puntos_no_ajustados, factor_ajuste)
           print("Calculando Puntos de Función Ajustados...")
           print("Puntos de Función Ajustados:", puntos_funcion_ajustados)
           print("\n")

        elif opcion == "2":
            casos_de_uso()
        elif opcion == "3":
            cosmic()
        elif opcion == "4":
            print("Saliendo del programa.Vuelve pronto.")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción que si sea válida.")

if __name__ == "__main__":
    main()

